import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

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
PDF_PATH = os.path.join(OUTPUT_DIR, "A2_one_pager.pdf")
PNG_PATH = os.path.join(OUTPUT_DIR, "A2_one_pager.png")

def build_a2_onepager():
    fig = plt.figure(figsize=(11.69, 8.27), dpi=300)
    fig.patch.set_facecolor("#ffffff")

    # 1. Header & Action Title
    fig.text(0.04, 0.94, "GenAI Investment Pays Back in 18 Months with ₹127.5L NPV; Adoption Drives 80% of Business Case Risk",
             fontsize=14.5, weight="bold", color=NAVY)
    fig.text(0.04, 0.91, "Kestrel Bank Grievance Operations Business Case (3-Year Horizon, 40,000 Complaints/Month Scale) · Verified Financial Model",
             fontsize=9.5, color=GREY, style="italic")

    # 2. Top Left: Scenario Comparison Table
    ax_sc = fig.add_axes([0.04, 0.60, 0.44, 0.28])
    ax_sc.axis("off")
    ax_sc.set_title("Financial Return Across 3 Operating Scenarios", fontsize=10, weight="bold", color=NAVY, loc="left")

    sc_table_data = [
        ["Adoption Target", "55%", "80%", "90%"],
        ["Labour Realisation Factor", "35%", "50%", "65%"],
        ["Escalation Reduction", "8%", "15%", "22%"],
        ["3-Year Full NPV", "-₹68.0 Lakh", "+₹127.5 Lakh", "+₹324.6 Lakh"],
        ["3-Year Hard NPV", "-₹123.3 Lakh", "-₹23.4 Lakh", "+₹75.6 Lakh"],
        ["Capital Payback (Full)", "Not in 3 yrs", "1.50 yrs (18 mos)", "1.05 yrs (13 mos)"],
        ["3-Year Return on Investment", "-27.0%", "+85.9%", "+197.1%"],
        ["Token Cost per Complaint", "₹2.12", "₹2.12", "₹2.12"],
        ["Token Share of 3-Yr Cost", "5.8%", "8.2%", "9.1%"]
    ]
    
    t_sc = ax_sc.table(cellText=sc_table_data, colLabels=["Financial Metric", "Worst Case", "Base Case", "Best Case"],
                       loc="center", cellLoc="center", colWidths=[0.38, 0.20, 0.21, 0.21])
    t_sc.auto_set_font_size(False)
    t_sc.set_fontsize(7.5)
    t_sc.scale(1, 1.35)
    
    for (row, col), cell in t_sc.get_celld().items():
        cell.set_edgecolor(BORDER_GREY)
        if row == 0:
            cell.set_facecolor(LIGHT_BLUE)
            cell.set_text_props(weight="bold", color=BLUE)
        elif row == 4: # Full NPV
            if col == 2:
                cell.set_facecolor(LIGHT_GREEN)
                cell.set_text_props(weight="bold", color=GREEN)
            elif col == 1:
                cell.set_facecolor(LIGHT_RED)
                cell.set_text_props(weight="bold", color=RED)
            elif col == 3:
                cell.set_facecolor(LIGHT_GREEN)
                cell.set_text_props(weight="bold", color=GREEN)
        elif row == 6: # Payback Full
            if col == 2:
                cell.set_text_props(weight="bold", color=NAVY)

    # 3. Bottom Left: Cash Flow Waterfall Table (Base Case)
    ax_cf = fig.add_axes([0.04, 0.08, 0.44, 0.44])
    ax_cf.axis("off")
    ax_cf.set_title("Base Case 4-Year Cash Flow Schedule (₹ Lakh)", fontsize=10, weight="bold", color=NAVY, loc="left")

    cf_data = [
        ["Complaints Handled via AI", "0", "153,600", "326,400", "384,000", "864,000"],
        ["Frontline Hours Saved", "0", "15,076 hrs", "32,037 hrs", "37,691 hrs", "84,804 hrs"],
        ["Gross Labour Value (@ ₹400/hr)", "₹0.0", "₹60.3L", "₹128.1L", "₹150.8L", "₹339.2L"],
        ["Hard Benefit (50% Realised)", "₹0.0", "₹30.2L", "₹64.1L", "₹75.4L", "₹169.6L"],
        ["Soft Benefit (Escalations Cut)", "₹0.0", "₹34.6L", "₹73.4L", "₹86.4L", "₹194.4L"],
        ["Total Full Benefit", "₹0.0", "₹64.7L", "₹137.5L", "₹161.8L", "₹364.0L"],
        ["One-off Build Capital (Capex)", "(₹86.0L)", "₹0.0", "₹0.0", "₹0.0", "(₹86.0L)"],
        ["Annual Run Cost (Fixed Opex)", "₹0.0", "(₹40.0L)", "(₹40.0L)", "(₹40.0L)", "(₹120.0L)"],
        ["LLM Token Inference Cost", "₹0.0", "(₹3.3L)", "(₹6.9L)", "(₹8.1L)", "(₹18.3L)"],
        ["Total Cost (Capex + Opex)", "(₹86.0L)", "(₹43.3L)", "(₹46.9L)", "(₹48.1L)", "(₹224.3L)"],
        ["Net Cash Flow (Full View)", "(₹86.0L)", "+₹21.5L", "+₹90.6L", "+₹113.6L", "+₹139.7L"],
        ["Cumulative Cash (Full View)", "(₹86.0L)", "(₹64.5L)", "+₹26.1L", "+₹139.7L", "+₹139.7L"]
    ]
    t_cf = ax_cf.table(cellText=cf_data, colLabels=["Line Item", "Y0 (Build)", "Y1 (40%)", "Y2 (85%)", "Y3 (100%)", "Total"],
                       loc="center", cellLoc="center", colWidths=[0.36, 0.13, 0.13, 0.13, 0.13, 0.14])
    t_cf.auto_set_font_size(False)
    t_cf.set_fontsize(7.0)
    t_cf.scale(1, 1.35)
    for (row, col), cell in t_cf.get_celld().items():
        cell.set_edgecolor(BORDER_GREY)
        if row == 0:
            cell.set_facecolor("#f1f5f9")
            cell.set_text_props(weight="bold", color=NAVY)
        elif row in [6, 11, 12]:
            cell.set_text_props(weight="bold")
            if row == 12 and col in [3, 4, 5]:
                cell.set_facecolor(LIGHT_GREEN)

    # 4. Right Column: Top - Tornado Sensitivity Chart
    ax_tor = fig.add_axes([0.52, 0.44, 0.44, 0.44])
    drivers = [
        "Adoption Target (50% - 95%)",
        "Escalation Cost (₹2.5k - ₹8.0k)",
        "Labour Realisation (30% - 70%)",
        "Minutes Saved (0.6x - 1.3x)",
        "Agent Cost (₹300 - ₹500/hr)",
        "Annual Run Cost (0.75x - 1.5x)",
        "Acceptance Rate (65% - 95%)",
        "Token Price (0.5x - 3.0x)"
    ]
    low_diff = [-116.1, -75.4, -69.2, -69.2, -43.2, 24.0, -40.7, 7.1]
    high_diff = [58.0, 90.5, 69.2, 51.9, 43.2, -48.0, 20.3, -28.5]
    y_pos = np.arange(len(drivers))[::-1]

    ax_tor.barh(y_pos, low_diff, align='center', color='#ef4444', height=0.55, label='Low Case vs Base')
    ax_tor.barh(y_pos, high_diff, align='center', color='#22c55e', height=0.55, label='High Case vs Base')
    ax_tor.axvline(0, color=NAVY, lw=1.2, ls='--')
    ax_tor.set_yticks(y_pos)
    ax_tor.set_yticklabels(drivers, fontsize=7.5, color=NAVY)
    ax_tor.set_xlabel("Change in 3-Year Full NPV vs Base Case (₹ Lakh)", fontsize=8, color=GREY)
    ax_tor.set_title("Tornado Sensitivity: Adoption is the #1 Financial Lever (₹174.1L Swing)", fontsize=10, weight="bold", color=NAVY, loc="left")
    ax_tor.spines["top"].set_visible(False)
    ax_tor.spines["right"].set_visible(False)
    ax_tor.tick_params(axis="both", labelsize=7.5)
    ax_tor.legend(loc="lower right", fontsize=7.5, frameon=True)
    ax_tor.set_xlim(-135, 115)

    for i, (l, h) in enumerate(zip(low_diff, high_diff)):
        yp = y_pos[i]
        if l < 0:
            ax_tor.text(l - 2, yp, f"{l:+.1f}L", va='center', ha='right', fontsize=6.8, color='#991b1b', weight='bold')
        else:
            ax_tor.text(l + 2, yp, f"{l:+.1f}L", va='center', ha='left', fontsize=6.8, color='#166534', weight='bold')
        if h > 0:
            ax_tor.text(h + 2, yp, f"{h:+.1f}L", va='center', ha='left', fontsize=6.8, color='#166534', weight='bold')
        else:
            ax_tor.text(h - 2, yp, f"{h:+.1f}L", va='center', ha='right', fontsize=6.8, color='#991b1b', weight='bold')

    # 5. Right Column: Bottom - Strategic Executive Takeaways
    ax_msg = fig.add_axes([0.52, 0.08, 0.44, 0.31])
    ax_msg.axis("off")
    ax_msg.set_title("Four Core Strategic Takeaways for Bank Leadership", fontsize=10, weight="bold", color=NAVY, loc="left")

    messages = [
        ["1. Full vs Hard Distinction", "Full business case delivers ₹127.5L NPV and 18-month payback. Hard-only labor yields -₹23.4L. Escalation avoidance must be defended to win approval."],
        ["2. Tokens Are Marginal (8.2%)", "Token inference is only ₹2.12/complaint (₹18.3L over 3 years). 91.8% of spend is fixed team, MLOps, and change management. Model shopping saves pennies."],
        ["3. Adoption Overwhelms Tech", "Adoption swing is ₹174.1L—twice as large as agent wage swings. If adoption halves (80% -> 40%), NPV turns negative. Operations change management is king."],
        ["4. Unit Economics Protected", "Haiku routing for triage (USD 0.0001/call) and prompt caching (90% hit rate, USD 0.01702/call for Policy Q&A) lock scalable gross margins as volume grows."]
    ]
    t_msg = ax_msg.table(cellText=messages, colLabels=["Strategic Dimension", "Executive Recommendation & Financial Grounding"],
                         loc="center", cellLoc="left", colWidths=[0.32, 0.68])
    t_msg.auto_set_font_size(False)
    t_msg.set_fontsize(7.2)
    t_msg.scale(1, 1.45)
    for (row, col), cell in t_msg.get_celld().items():
        cell.set_edgecolor(BORDER_GREY)
        if row == 0:
            cell.set_facecolor(LIGHT_BLUE)
            cell.set_text_props(weight="bold", color=BLUE)

    # 6. Footer Note
    fig.text(0.04, 0.03, "Financial Assumptions Note: Anthropic token pricing (Nov 2026: Sonnet $2/$10, Haiku $0.10/$0.50). FX ₹88/USD. Discount rate 12%. 50% labor realization factor. Kestrel Bank is a fictional mid-size private bank.",
             fontsize=7.2, color=GREY, style="italic")

    with PdfPages(PDF_PATH) as pdf:
        pdf.savefig(fig, bbox_inches="tight")
    plt.savefig(PNG_PATH, bbox_inches="tight")
    plt.close()
    print(f"A2 One-Pager saved to:\n - {PDF_PATH}\n - {PNG_PATH}")

if __name__ == "__main__":
    build_a2_onepager()
