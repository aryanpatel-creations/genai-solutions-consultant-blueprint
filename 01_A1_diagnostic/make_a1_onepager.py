import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

# Styling constants
NAVY = "#0f172a"
BLUE = "#1e40af"
LIGHT_BLUE = "#dbeafe"
GREY = "#64748b"
LIGHT_GREY = "#f8fafc"
BORDER_GREY = "#cbd5e1"
GREEN = "#15803d"
LIGHT_GREEN = "#dcfce7"
RED = "#b91c1c"
LIGHT_RED = "#fee2e2"

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)
PDF_PATH = os.path.join(OUTPUT_DIR, "A1_onepager.pdf")
PNG_PATH = os.path.join(OUTPUT_DIR, "A1_onepager.png")

def build_a1_onepager():
    # A4 landscape: 11.69 x 8.27 inches
    fig = plt.figure(figsize=(11.69, 8.27), dpi=300)
    fig.patch.set_facecolor("#ffffff")

    # 1. Header & Action Title
    fig.text(0.04, 0.94, "80% of Complaints Stem from 10 Core Issues; Knowledge & Policy Gaps, Not Frontline Agents, Drive Delay",
             fontsize=15, weight="bold", color=NAVY)
    fig.text(0.04, 0.91, "Kestrel Bank Retail Grievance Diagnostic (Lean Six Sigma DMAIC) · Empirical CFPB Data (24-Month Window, N=346,481)",
             fontsize=9.5, color=GREY, style="italic")

    # 2. Left Column: Top - Pareto Chart
    ax_pareto = fig.add_axes([0.04, 0.52, 0.44, 0.35])
    df_clean = pd.read_csv(os.path.join(os.path.dirname(__file__), "complaints_clean.csv"), dtype=str)
    counts = df_clean["Issue"].value_counts().head(8)
    cum_pct = 100 * counts.cumsum() / len(df_clean)
    
    # Shorten labels for clean display
    short_labels = [
        "Managing account",
        "Purchase dispute",
        "Incorrect report info",
        "Getting credit card",
        "Closing account",
        "Lender/fee charge",
        "Other terms/probs",
        "Funds low problems"
    ]
    
    bars = ax_pareto.barh(range(len(counts)), counts.values[::-1], color="#2563eb", height=0.65)
    ax_pareto.set_yticks(range(len(counts)))
    ax_pareto.set_yticklabels(short_labels[::-1], fontsize=8, color=NAVY)
    ax_pareto.set_xlabel("Number of Complaints", fontsize=8, color=GREY)
    ax_pareto.set_title("Pareto Analysis: Top Complaint Issues (10 of 20 = 80%)", fontsize=10, weight="bold", color=NAVY, loc="left")
    ax_pareto.spines["top"].set_visible(False)
    ax_pareto.spines["right"].set_visible(False)
    ax_pareto.spines["left"].set_color(BORDER_GREY)
    ax_pareto.spines["bottom"].set_color(BORDER_GREY)
    ax_pareto.tick_params(axis="both", labelsize=7.5)

    for i, (bar, pct) in enumerate(zip(bars, cum_pct.values[::-1])):
        val = bar.get_width()
        ax_pareto.text(val + 1500, bar.get_y() + bar.get_height()/2, f"{val:,.0f} ({pct:.0f}% cum)",
                       va="center", ha="left", fontsize=7, color=GREY)

    # 3. Left Column: Bottom - Baseline KPI Table
    ax_kpi = fig.add_axes([0.04, 0.08, 0.44, 0.38])
    ax_kpi.axis("off")
    ax_kpi.set_title("Empirical Baseline Performance Metrics", fontsize=10, weight="bold", color=NAVY, loc="left")

    kpi_data = [
        ["Complaints in 24m Window", "346,481", "Measured", "CFPB Data (Sept 2024 - Aug 2026)"],
        ["Average Volume / Month", "14,437", "Measured", "CFPB Stand-in (Assumed 40k Indian scale)"],
        ["Timely Response Rate", "99.3%", "Measured", "Intake is NOT the bottleneck"],
        ["Median Routing Lag", "0.0 days", "Measured", "Tickets routed instantly to queues"],
        ["Customer Relief Rate", "24.8%", "Measured", "13.1% monetary + 11.8% non-monetary"],
        ["Digital / Web Intake Share", "91.3%", "Measured", "Digital channel dominance"],
        ["Narratives Available", "45.1%", "Measured", "156,333 complaints with full text"],
        ["Baseline Handle Time (AHT)", "25.0 min", "Assumed", "Operations baseline to be validated"],
        ["Loaded Agent Cost", "₹400 / hr", "Assumed", "Fully loaded seat & IT overhead"]
    ]
    
    table = ax_kpi.table(cellText=kpi_data, colLabels=["Metric", "Value", "Type", "Operational Insight"],
                         loc="center", cellLoc="left", colWidths=[0.38, 0.16, 0.18, 0.48])
    table.auto_set_font_size(False)
    table.set_fontsize(7.5)
    table.scale(1, 1.45)
    
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor(BORDER_GREY)
        if row == 0:
            cell.set_facecolor(LIGHT_BLUE)
            cell.set_text_props(weight="bold", color=BLUE)
        else:
            if row % 2 == 1:
                cell.set_facecolor("#ffffff")
            else:
                cell.set_facecolor(LIGHT_GREY)

    # 4. Right Column: Top - Tagged Root-Cause Breakdown
    ax_rc = fig.add_axes([0.52, 0.65, 0.44, 0.22])
    ax_rc.axis("off")
    ax_rc.set_title("Root-Cause Defect Taxonomy (100 Tagged Sample)", fontsize=10, weight="bold", color=NAVY, loc="left")

    rc_data = [
        ["Process Deficiencies", "56%", "Knowledge retrieval lag (8 min AHT) & misrouting bounce across teams"],
        ["System & Ledger Friction", "25%", "Batch posting delays, multi-month dispute chronology assembly"],
        ["Policy Bottlenecks", "15%", "Rigid fee waiver thresholds; lack of frontline discretionary authority"],
        ["Information & Transparency", "3%", "Opaque statement descriptors triggering unneeded billing disputes"],
        ["Frontline People / Tone", "1%", "Agent rudeness is minimal; defects stem from broken systems & rules"]
    ]
    t_rc = ax_rc.table(cellText=rc_data, colLabels=["Defect Category", "% Share", "Root Mechanism Identified"],
                       loc="center", cellLoc="left", colWidths=[0.32, 0.14, 0.54])
    t_rc.auto_set_font_size(False)
    t_rc.set_fontsize(7.5)
    t_rc.scale(1, 1.35)
    for (row, col), cell in t_rc.get_celld().items():
        cell.set_edgecolor(BORDER_GREY)
        if row == 0:
            cell.set_facecolor("#f1f5f9")
            cell.set_text_props(weight="bold", color=NAVY)

    # 5. Right Column: Middle - Non-AI Quick Wins (Zero Tech Debt)
    ax_non_ai = fig.add_axes([0.52, 0.37, 0.44, 0.24])
    ax_non_ai.axis("off")
    ax_non_ai.set_title("High-Impact Non-AI Quick Wins (Eliminate ~18% Volume Upfront)", fontsize=10, weight="bold", color=NAVY, loc="left")

    non_ai_data = [
        ["1. Frontline Waiver Matrix", "Grant Tier-1 agents discretionary waiver limit (up to ₹1,500)"],
        ["2. CRM Issue Categorization", "Standardize CRM dispute tags to match top 10 Pareto categories"],
        ["3. Unified Knowledge Custodian", "Appoint single owner under Nodal Officer for monthly policy sync"],
        ["4. Proactive Billing Alerts", "SMS/Push notification 48 hrs prior to annual card fee debit"],
        ["5. Single-Click Closure", "Self-service mobile account cancellation removing branch friction"]
    ]
    t_nai = ax_non_ai.table(cellText=non_ai_data, colLabels=["Lean Operational Fix", "Targeted Defect & Expected Effect"],
                            loc="center", cellLoc="left", colWidths=[0.38, 0.62])
    t_nai.auto_set_font_size(False)
    t_nai.set_fontsize(7.5)
    t_nai.scale(1, 1.35)
    for (row, col), cell in t_nai.get_celld().items():
        cell.set_edgecolor(BORDER_GREY)
        if row == 0:
            cell.set_facecolor(LIGHT_GREEN)
            cell.set_text_props(weight="bold", color=GREEN)

    # 6. Right Column: Bottom - AI Opportunity Scope & Governance
    ax_ai = fig.add_axes([0.52, 0.08, 0.44, 0.25])
    ax_ai.axis("off")
    ax_ai.set_title("AI Scope Boundaries: Recommended Tools vs Prohibited Autonomous Actions", fontsize=10, weight="bold", color=NAVY, loc="left")

    ai_data = [
        ["Policy RAG Assistant", "Recommended", "Semantic search across RBI circulars with section citations (38% tags)"],
        ["Semantic Triage", "Recommended", "Auto-predict queue destination to eliminate misrouting (27% tags)"],
        ["Chronology Summarizer", "Recommended", "Extract multi-event dispute timeline via MCP tools (17% tags)"],
        ["Response Drafter", "Recommended", "Pre-draft empathetic letters with compliance checklist for human review"],
        ["Autonomous Dispatch", "PROHIBITED", "Never send unreviewed model outputs to customers (RB-IOS violation)"],
        ["Automated Denial", "PROHIBITED", "Dispute rejections require human officer sign-off under RBI FREE-AI"]
    ]
    t_ai = ax_ai.table(cellText=ai_data, colLabels=["Intervention", "Status", "Governance Rule & Value"],
                       loc="center", cellLoc="left", colWidths=[0.32, 0.18, 0.50])
    t_ai.auto_set_font_size(False)
    t_ai.set_fontsize(7.5)
    t_ai.scale(1, 1.25)
    for (row, col), cell in t_ai.get_celld().items():
        cell.set_edgecolor(BORDER_GREY)
        if row == 0:
            cell.set_facecolor(LIGHT_BLUE)
            cell.set_text_props(weight="bold", color=BLUE)
        elif row in [5, 6]:
            if col == 1:
                cell.set_text_props(weight="bold", color=RED)
                cell.set_facecolor(LIGHT_RED)

    # 7. Footer: Professional Consulting Note
    fig.text(0.04, 0.03, "Data Note: Stand-in CFPB consumer data (Sept 2024 - Aug 2026). Resolution timestamps are not in the raw data; handling time (25m) and agent cost (₹400/hr) are labelled assumptions. Kestrel Bank is a fictional entity.",
             fontsize=7.5, color=GREY, style="italic")

    # Save outputs
    with PdfPages(PDF_PATH) as pdf:
        pdf.savefig(fig, bbox_inches="tight")
    plt.savefig(PNG_PATH, bbox_inches="tight")
    plt.close()
    print(f"A1 Executive One-Pager saved to:\n - {PDF_PATH}\n - {PNG_PATH}")

if __name__ == "__main__":
    build_a1_onepager()
