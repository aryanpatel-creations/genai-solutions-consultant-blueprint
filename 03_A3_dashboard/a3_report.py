"""Static version of the dashboard: one PDF page per audience, for people who will not run code.

Run:  python a3_report.py    ->  outputs/A3_AI_Value_Report.pdf  (+ one PNG per page)
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import kpis

BLUE, GREEN, PURPLE, RED, GREY = "#2a78d6", "#1a9a6c", "#5b49c9", "#c0392b", "#52514e"
FX = kpis.ASSUMPTIONS["fx_inr_per_usd"]
F = kpis.fmt
os.makedirs("outputs", exist_ok=True)
df = kpis.load_events("data/ai_event_log.csv")
weekly = kpis.weekly(df)


def page(title, question, tiles, note):
    """A4-landscape page: title, four KPI tiles, two chart areas, a note at the bottom."""
    fig = plt.figure(figsize=(11.69, 8.27))
    fig.text(0.04, 0.94, title, fontsize=18, weight="bold")
    fig.text(0.04, 0.905, f"{question}   ·   Kestrel Bank (fictional) · simulated 90-day pilot",
             fontsize=10, color=GREY)
    for i, (label, value) in enumerate(tiles):
        x = 0.04 + i * 0.235
        fig.patches.append(plt.Rectangle((x, 0.74), 0.215, 0.13, transform=fig.transFigure,
                                         facecolor="#f2f5fa", edgecolor="none"))
        fig.text(x + 0.012, 0.835, label, fontsize=9.5, color=GREY)
        fig.text(x + 0.012, 0.765, value, fontsize=20, weight="bold")
    fig.text(0.04, 0.03, note, fontsize=8.5, color=GREY)
    return fig, fig.add_axes([0.06, 0.12, 0.52, 0.55]), fig.add_axes([0.66, 0.12, 0.31, 0.55])


def style(ax, title):
    ax.set_title(title, loc="left", fontsize=11, weight="bold")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.tick_params(labelsize=8)


pages = []

# 1 Executive
fig, a, b = page(
    "1 · Executive (CFO)", "Is this paying for itself?",
    [("AI cost", F(kpis.ai_cost_inr(df), "inr")),
     ("Realised value", F(kpis.realised_value_inr(df), "inr")),
     ("Net value", F(kpis.net_value_inr(df), "inr")),
     ("Cost per run", F(kpis.cost_per_run_inr(df), "inr2"))],
    "Net value covers model usage only; run team, hosting and build costs are in the A2 business case.")
cum = kpis.cumulative_net_value(df)
a.plot(cum["date"], cum["cumulative_net_value_inr"] / 1e5, color=BLUE, lw=2)
style(a, "Cumulative net value (₹ lakh)")
by_uc = df.groupby("use_case")["cost_usd"].sum().sort_values() * FX
b.barh(by_uc.index, by_uc.values, color=[BLUE, GREEN, PURPLE][: len(by_uc)])
style(b, "AI cost by use case (₹)")
pages.append(fig)

# 2 Operations
fig, a, b = page(
    "2 · Operations (COO)", "Is it making the team faster?",
    [("Hours saved", F(kpis.hours_saved(df), "num")),
     ("Runs per day", F(kpis.runs_per_day(df), "num")),
     ("Acceptance rate", F(kpis.acceptance_rate(df), "pct")),
     ("Human escalation", F(kpis.human_escalation_rate(df), "pct"))],
    "Hours saved: full saving when accepted, half when edited, -0.5 min when rejected. "
    "Target handle time 25 → 19 min.")
a.bar(weekly["week_start"], weekly["hours_saved"], width=5, color=GREEN)
style(a, "Hours saved by week")
accepted = df["agent_outcome"].isin(["Accepted", "Edited"])
acc = accepted.groupby(df["team"]).mean().sort_values()
b.barh(acc.index, acc.values, color=GREEN)
b.axvline(0.8, color=RED, ls="--", lw=1)
b.set_xlim(0, 1)
style(b, "Acceptance rate by team (target 80%)")
pages.append(fig)

# 3 Risk
fig, a, b = page(
    "3 · Risk & Compliance (CRO)", "Is it safe?",
    [("Override rate", F(kpis.override_rate(df), "pct")),
     ("Guardrail flags", F(kpis.guardrail_flag_rate(df), "pct")),
     ("PII blocks", F(kpis.pii_blocks(df), "int")),
     ("P95 latency", F(kpis.p95_latency_s(df), "num2") + " s")],
    "Override rate above 15% for two weeks triggers a review. "
    "PII blocks mean the masking control worked.")
a.plot(weekly["week_start"], weekly["override_rate"] * 100, marker="o", color=PURPLE)
a.axhline(15, color=RED, ls="--", lw=1)
a.set_ylim(0, 20)
style(a, "Override rate by week (%)")
flags = df[df["guardrail_flag"] != "No flag"]["guardrail_flag"].value_counts().sort_values()
b.barh(flags.index, flags.values, color=PURPLE)
style(b, "Guardrail flags by type")
pages.append(fig)

# 4 Sponsor
fig, a, b = page(
    "4 · Sponsor (Head of Customer Service)", "Are people using it?",
    [("Active agents", F(kpis.active_agents(df), "int")),
     ("Adoption", F(kpis.adoption_pct(df), "pct")),
     ("Runs per agent", F(kpis.runs_per_agent(df), "num")),
     ("Teams live", F(kpis.teams_live(df), "int"))],
    "Adoption % divides by all 120 pilot agents, so read it at total level.")
a.plot(weekly["week_start"], weekly["active_agents"], marker="o", color=BLUE)
style(a, "Active agents by week")
runs = df.groupby("team").size().sort_values()
b.barh(runs.index, runs.values, color=BLUE)
style(b, "Runs by team")
pages.append(fig)

# 5 KPI dictionary
table = kpis.kpi_table(df)[["KPI", "Value", "Owner", "Threshold", "Status"]]
fig = plt.figure(figsize=(11.69, 8.27))
fig.text(0.04, 0.94, "KPI dictionary", fontsize=18, weight="bold")
ax = fig.add_axes([0.04, 0.06, 0.92, 0.84])
ax.axis("off")
t = ax.table(cellText=table.values, colLabels=table.columns, loc="upper left", cellLoc="left")
t.auto_set_font_size(False)
t.set_fontsize(9)
t.scale(1, 1.6)
pages.append(fig)

with PdfPages("outputs/A3_AI_Value_Report.pdf") as pdf:
    for i, f in enumerate(pages, start=1):
        pdf.savefig(f)
        f.savefig(f"outputs/A3_page{i}.png", dpi=150)
        plt.close(f)
print("Saved outputs/A3_AI_Value_Report.pdf and 5 PNG pages")
