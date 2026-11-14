"""A3 AI Value Dashboard (Streamlit + Plotly).

Run:  streamlit run dashboard.py     then open the address it prints (usually http://localhost:8501)
"""
import pandas as pd
import plotly.express as px
import streamlit as st
import kpis

st.set_page_config(page_title="AI Value Dashboard · Kestrel Bank", layout="wide")
COLOURS = {"Triage & routing": "#2a78d6", "Draft reply": "#5b49c9",
           "Policy knowledge Q&A": "#1a9a6c"}
FX = kpis.ASSUMPTIONS["fx_inr_per_usd"]
F = kpis.fmt


@st.cache_data
def load() -> tuple[pd.DataFrame, pd.DataFrame]:
    return kpis.load_events("data/ai_event_log.csv"), pd.read_csv("data/baseline_targets.csv")


events, targets = load()

# ---------- sidebar filters (the Power BI "slicers") ----------
st.sidebar.header("Filters")
first, last = events["date"].min().date(), events["date"].max().date()
dates = st.sidebar.date_input("Date range", (first, last), min_value=first, max_value=last)
full_range = isinstance(dates, (tuple, list)) and len(dates) == 2
start, end = dates if full_range else (first, last)      # ignore half-picked ranges
teams = st.sidebar.multiselect("Team", sorted(events["team"].unique()))
use_cases = st.sidebar.multiselect("Use case", sorted(events["use_case"].unique()))
df = kpis.filter_events(events, start, end, teams, use_cases)
a = kpis.ASSUMPTIONS
st.sidebar.caption(
    "Simulated data: first 90 days of Phase 2 for Kestrel Bank, a fictional bank. "
    f"Assumptions shared with A2: ₹{a['agent_cost_per_hour']}/hour, "
    f"{a['realisation']:.0%} realisation, ₹{a['fx_inr_per_usd']} per USD.")

st.title("Is the complaints AI working?")
st.caption("Kestrel Bank (fictional) · AI assistant pilot · simulated data")
if df.empty:
    st.warning("No data for these filters. Widen the date range or clear a filter.")
    st.stop()
weekly = kpis.weekly(df)


def cards(items):
    """Up to four KPI tiles in a row: (label, value, help text)."""
    for col, (label, value, help_text) in zip(st.columns(len(items)), items):
        col.metric(label, value, help=help_text)


exec_tab, ops_tab, risk_tab, sponsor_tab, dict_tab = st.tabs(
    ["1 · Executive (CFO)", "2 · Operations (COO)", "3 · Risk & Compliance",
     "4 · Sponsor", "KPI dictionary"])

with exec_tab:
    st.subheader("Is this paying for itself?")
    cards([("AI cost", F(kpis.ai_cost_inr(df), "inr"), "Model usage cost"),
           ("Realised value", F(kpis.realised_value_inr(df), "inr"),
            "Hours saved × ₹/hour × realisation"),
           ("Net value", F(kpis.net_value_inr(df), "inr"), "Realised value minus AI cost"),
           ("Cost per run", F(kpis.cost_per_run_inr(df), "inr2"), "AI cost ÷ runs")])
    left, right = st.columns([3, 2])
    cum = kpis.cumulative_net_value(df)
    left.plotly_chart(px.line(cum, x="date", y="cumulative_net_value_inr",
                              title="Cumulative net value (₹)",
                              labels={"cumulative_net_value_inr": "₹", "date": ""}))
    by_uc = (df.groupby("use_case")["cost_usd"].sum() * FX).reset_index(name="ai_cost_inr")
    fig = px.bar(by_uc, x="ai_cost_inr", y="use_case", orientation="h", color="use_case",
                 color_discrete_map=COLOURS, title="AI cost by use case (₹)",
                 labels={"ai_cost_inr": "₹", "use_case": ""})
    right.plotly_chart(fig.update_layout(showlegend=False))
    st.info("Net value here covers model usage only. The run team, hosting and the build cost are "
            "in the A2 business case (base-case payback 18 months, including fewer Ombudsman "
            "escalations).")

with ops_tab:
    st.subheader("Is it making the team faster?")
    cards([("Hours saved", F(kpis.hours_saved(df), "num"), "Rejected answers count as -0.5 min"),
           ("Runs per day", F(kpis.runs_per_day(df), "num"), "AI runs ÷ active days"),
           ("Acceptance rate", F(kpis.acceptance_rate(df), "pct"),
            "Accepted or edited ÷ runs; target ≥ 80%"),
           ("Human escalation", F(kpis.human_escalation_rate(df), "pct"),
            "Sent to a supervisor ÷ runs")])
    left, right = st.columns([3, 2])
    left.plotly_chart(px.bar(weekly, x="week_start", y="hours_saved", title="Hours saved by week",
                             labels={"week_start": "Week starting", "hours_saved": "Hours"}))
    accepted = df["agent_outcome"].isin(["Accepted", "Edited"])
    by_team = accepted.groupby(df["team"]).mean().reset_index(name="acceptance")
    fig = px.bar(by_team, x="acceptance", y="team", orientation="h", range_x=[0, 1],
                 title="Acceptance rate by team", labels={"acceptance": "", "team": ""})
    fig.add_vline(x=0.80, line_dash="dash", annotation_text="target 80%")
    right.plotly_chart(fig.update_xaxes(tickformat=".0%"))
    aht = targets.set_index("metric").loc["Avg handle time (min)"]
    st.caption(f"Baseline handle time {aht['baseline']:.0f} min → target {aht['target']:.0f} min "
               f"({aht['source']}).")

with risk_tab:
    st.subheader("Is it safe?")
    cards([("Override rate", F(kpis.override_rate(df), "pct"),
            "Rejected ÷ runs; review if > 15% for 2 weeks"),
           ("Guardrail flags", F(kpis.guardrail_flag_rate(df), "pct"), "Any safety flag ÷ runs"),
           ("PII blocks", F(kpis.pii_blocks(df), "int"),
            "Masking stopped personal data: a working control"),
           ("P95 latency", F(kpis.p95_latency_s(df), "num2") + " s",
            "95% of answers are faster than this")])
    left, right = st.columns([3, 2])
    fig = px.line(weekly, x="week_start", y="override_rate", markers=True,
                  title="Override rate by week",
                  labels={"week_start": "Week starting", "override_rate": ""})
    fig.add_hline(y=0.15, line_dash="dash", line_color="#c0392b",
                  annotation_text="review threshold 15%")
    left.plotly_chart(fig.update_yaxes(tickformat=".0%", rangemode="tozero"))
    flags = df[df["guardrail_flag"] != "No flag"]
    right.markdown("**Guardrail flags by type and use case**")
    right.dataframe(pd.crosstab(flags["guardrail_flag"], flags["use_case"]))

with sponsor_tab:
    st.subheader("Are people using it?")
    cards([("Active agents", F(kpis.active_agents(df), "int"), "Distinct agents using the AI"),
           ("Adoption", F(kpis.adoption_pct(df), "pct"),
            "Active ÷ 120 pilot agents; read at total level"),
           ("Runs per agent", F(kpis.runs_per_agent(df), "num"), "AI runs ÷ active agents"),
           ("Teams live", F(kpis.teams_live(df), "int"), "Teams using the AI")])
    left, right = st.columns([3, 2])
    left.plotly_chart(px.line(weekly, x="week_start", y="active_agents", markers=True,
                              title="Active agents by week",
                              labels={"week_start": "Week starting", "active_agents": "Agents"}))
    mix = df.groupby(["team", "use_case"]).size().reset_index(name="runs")
    right.plotly_chart(px.bar(mix, x="runs", y="team", color="use_case", orientation="h",
                              color_discrete_map=COLOURS, title="Runs by team and use case",
                              labels={"runs": "Runs", "team": "", "use_case": ""}))

with dict_tab:
    st.subheader("KPI dictionary")
    st.caption("Every number on this dashboard: definition, owner and the threshold that triggers "
               "action.")
    st.dataframe(kpis.kpi_table(df), hide_index=True)
