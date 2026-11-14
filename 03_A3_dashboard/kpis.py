"""A3 KPI layer: every dashboard number comes from one small, tested function here.

The functions take the (filtered) event log and return one number, so the same definitions
are used by the Streamlit dashboard, the static PDF report and the tests.
"""
import pandas as pd

# Assumptions shared with the A2 business case (keep them identical)
ASSUMPTIONS = {
    "fx_inr_per_usd": 88,          # INR per USD
    "agent_cost_per_hour": 400,    # loaded agent cost, INR
    "realisation": 0.5,            # share of saved time that becomes money
    "pilot_agents": 120,           # agents in the pilot (all four teams)
}


def load_events(path: str = "data/ai_event_log.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["date"] = pd.to_datetime(df["date"])
    df["week_start"] = df["date"] - pd.to_timedelta(df["date"].dt.dayofweek, unit="D")   # Monday
    return df


def filter_events(df, start=None, end=None, teams=None, use_cases=None) -> pd.DataFrame:
    """Same job as Power BI slicers. Empty or None means 'no filter'."""
    mask = pd.Series(True, index=df.index)
    if start is not None:
        mask &= df["date"] >= pd.Timestamp(start)
    if end is not None:
        mask &= df["date"] <= pd.Timestamp(end)
    if teams:
        mask &= df["team"].isin(teams)
    if use_cases:
        mask &= df["use_case"].isin(use_cases)
    return df[mask]


def _share(mask: pd.Series) -> float:
    return float(mask.mean()) if len(mask) else 0.0      # 0 instead of an error on empty data


# ---------- cost and value (CFO) ----------
def ai_runs(df) -> int:
    return int(len(df))

def ai_cost_inr(df) -> float:
    return float(df["cost_usd"].sum() * ASSUMPTIONS["fx_inr_per_usd"])

def cost_per_run_inr(df) -> float:
    return ai_cost_inr(df) / ai_runs(df) if len(df) else 0.0

def hours_saved(df) -> float:
    return float(df["minutes_saved"].sum() / 60)

def realised_value_inr(df) -> float:
    return hours_saved(df) * ASSUMPTIONS["agent_cost_per_hour"] * ASSUMPTIONS["realisation"]

def net_value_inr(df) -> float:
    """Model usage only; the run team, hosting and build costs are in the A2 business case."""
    return realised_value_inr(df) - ai_cost_inr(df)


# ---------- quality and risk (CRO) ----------
def acceptance_rate(df) -> float:
    return _share(df["agent_outcome"].isin(["Accepted", "Edited"]))

def override_rate(df) -> float:
    return _share(df["agent_outcome"].eq("Rejected"))

def guardrail_flag_rate(df) -> float:
    return _share(df["guardrail_flag"].ne("No flag"))

def pii_blocks(df) -> int:
    return int(df["guardrail_flag"].eq("PII blocked").sum())

def human_escalation_rate(df) -> float:
    return _share(df["escalated_to_human"].eq("Yes"))

def p95_latency_s(df) -> float:
    """95th percentile; same method as Excel PERCENTILE.INC and DAX PERCENTILE.INC."""
    return float(df["latency_ms"].quantile(0.95) / 1000) if len(df) else 0.0


# ---------- adoption (sponsor) ----------
def active_agents(df) -> int:
    return int(df["agent_id"].nunique())

def adoption_pct(df) -> float:
    return active_agents(df) / ASSUMPTIONS["pilot_agents"]

def runs_per_agent(df) -> float:
    return ai_runs(df) / active_agents(df) if len(df) else 0.0

def runs_per_day(df) -> float:
    return ai_runs(df) / df["date"].nunique() if len(df) else 0.0

def teams_live(df) -> int:
    return int(df["team"].nunique())


# ---------- trends ----------
def weekly(df) -> pd.DataFrame:
    g = df.groupby("week_start")
    out = pd.DataFrame({
        "runs": g.size(),
        "ai_cost_inr": g["cost_usd"].sum() * ASSUMPTIONS["fx_inr_per_usd"],
        "hours_saved": g["minutes_saved"].sum() / 60,
        "acceptance_rate": g["agent_outcome"].apply(lambda s: s.isin(["Accepted", "Edited"]).mean()),
        "override_rate": g["agent_outcome"].apply(lambda s: s.eq("Rejected").mean()),
        "active_agents": g["agent_id"].nunique(),
    })
    return out.reset_index()


def cumulative_net_value(df) -> pd.DataFrame:
    """Daily net value, then a running total (the CFO's 'is it paying for itself?' line)."""
    daily = df.groupby("date").agg(cost_usd=("cost_usd", "sum"), minutes=("minutes_saved", "sum"))
    value = daily["minutes"] / 60 * ASSUMPTIONS["agent_cost_per_hour"] * ASSUMPTIONS["realisation"]
    cost = daily["cost_usd"] * ASSUMPTIONS["fx_inr_per_usd"]
    return (value - cost).cumsum().rename("cumulative_net_value_inr").reset_index()


# ---------- KPI dictionary: definition, owner and the threshold that triggers action ----------
KPI_DICTIONARY = [
    # name, function, format, page, owner, definition, threshold (direction, value)
    ("AI cost (INR)", ai_cost_inr, "inr", "Executive", "AI product owner",
     "Sum of model cost per run x FX rate", None),
    ("Realised value (INR)", realised_value_inr, "inr", "Executive", "Head of Customer Service",
     "Hours saved x agent cost per hour x realisation factor", None),
    ("Net value (INR)", net_value_inr, "inr", "Executive", "CFO",
     "Realised value minus AI cost (model usage only)", (">=", 0)),
    ("Cost per run (INR)", cost_per_run_inr, "inr2", "Executive", "AI product owner",
     "AI cost / AI runs", ("<=", 2.0)),
    ("Hours saved", hours_saved, "num", "Operations", "Operations head",
     "Sum of minutes saved / 60 (rejected answers count -0.5 min)", None),
    ("Runs per day", runs_per_day, "num", "Operations", "Operations head",
     "AI runs / days with activity", None),
    ("Acceptance rate", acceptance_rate, "pct", "Operations", "Team leads",
     "Accepted or edited / all runs", (">=", 0.80)),
    ("Human escalation rate", human_escalation_rate, "pct", "Risk", "Principal Nodal Officer",
     "Runs sent to a supervisor / all runs", ("<=", 0.08)),
    ("Override rate", override_rate, "pct", "Risk", "Chief Risk Officer",
     "Rejected by the agent / all runs; above 15% for two weeks triggers a review", ("<=", 0.15)),
    ("Guardrail flag rate", guardrail_flag_rate, "pct", "Risk", "Compliance",
     "Runs with any guardrail flag / all runs", ("<=", 0.05)),
    ("PII blocks", pii_blocks, "int", "Risk", "IT security",
     "Runs where masking blocked personal data (a working control, not a leak)", None),
    ("P95 latency (s)", p95_latency_s, "num2", "Risk", "IT",
     "95th percentile time to answer", ("<=", 5.0)),
    ("Active agents", active_agents, "int", "Sponsor", "Head of Customer Service",
     "Distinct agents who used the AI", None),
    ("Adoption %", adoption_pct, "pct", "Sponsor", "Head of Customer Service",
     "Active agents / 120 pilot agents (read at total level)", (">=", 0.60)),
    ("Runs per agent", runs_per_agent, "num", "Sponsor", "Team leads",
     "AI runs / active agents", None),
    ("Teams live", teams_live, "int", "Sponsor", "Head of Customer Service",
     "Distinct teams using the AI", None),
]


def fmt(value, kind: str) -> str:
    if kind == "inr":
        return f"₹{value / 1e5:,.2f} lakh" if abs(value) >= 1e5 else f"₹{value:,.0f}"
    return {"inr2": f"₹{value:,.2f}", "pct": f"{value:.1%}", "int": f"{value:,.0f}",
            "num": f"{value:,.0f}", "num2": f"{value:,.2f}"}[kind]


def kpi_table(df) -> pd.DataFrame:
    rows = []
    for name, fn, kind, page, owner, definition, rule in KPI_DICTIONARY:
        v = fn(df)
        status = "—"
        if rule:
            op, limit = rule
            status = "On target" if (v >= limit if op == ">=" else v <= limit) else "Action needed"
        rows.append({"KPI": name, "Value": fmt(v, kind), "Page": page, "Owner": owner,
                     "Definition": definition,
                     "Threshold": f"{rule[0]} {rule[1]}" if rule else "—", "Status": status})
    return pd.DataFrame(rows)
