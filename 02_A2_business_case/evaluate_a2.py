import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Kestrel Bank Financial Model Engine for Project A2
# Follows the exact formulas in A2_GenAI_Cost_ROI.xlsx

PRICES = {
    "Claude Sonnet 5.5": {"input": 2.00, "cached": 0.10, "output": 10.00},
    "Claude Haiku 5.5": {"input": 0.10, "cached": 0.01, "output": 0.50}
}

USE_CASES = [
    {
        "name": "Triage and routing",
        "model": "Claude Haiku 5.5",
        "coverage": 1.0,
        "calls_per_complaint": 1.0,
        "input_tokens": 1200,
        "cacheable_tokens": 800,
        "output_tokens": 60,
        "min_saved_per_covered": 2.5
    },
    {
        "name": "Draft reply",
        "model": "Claude Sonnet 5.5",
        "coverage": 0.7,
        "calls_per_complaint": 1.5,
        "input_tokens": 6000,
        "cacheable_tokens": 2000,
        "output_tokens": 450,
        "min_saved_per_covered": 6.0
    },
    {
        "name": "Policy knowledge Q&A",
        "model": "Claude Sonnet 5.5",
        "coverage": 0.6,
        "calls_per_complaint": 1.0,
        "input_tokens": 8500,
        "cacheable_tokens": 3000,
        "output_tokens": 500,
        "min_saved_per_covered": 4.0
    }
]

BUILD_COSTS = [1800000, 4000000, 1500000, 700000, 600000] # Total: 86,00,000 INR
RUN_COSTS_EXCL_TOKENS = [900000, 400000, 2200000, 500000] # Total: 40,00,000 INR / year

SCENARIOS = {
    "Worst": {
        "Complaints_m": 40000,
        "AHT": 25,
        "Cost_hr": 400,
        "Adoption": 0.55,
        "Acceptance": 0.70,
        "Realisation": 0.35,
        "Esc_rate": 0.03,
        "Esc_cut": 0.08,
        "Esc_cost": 5000,
        "FX": 88,
        "Disc": 0.12,
        "Cache_hit": 0.90,
        "Cache_write": 1.25,
        "Ramp_Y1": 0.40,
        "Ramp_Y2": 0.85,
        "Ramp_Y3": 1.00
    },
    "Base": {
        "Complaints_m": 40000,
        "AHT": 25,
        "Cost_hr": 400,
        "Adoption": 0.80,
        "Acceptance": 0.85,
        "Realisation": 0.50,
        "Esc_rate": 0.03,
        "Esc_cut": 0.15,
        "Esc_cost": 5000,
        "FX": 88,
        "Disc": 0.12,
        "Cache_hit": 0.90,
        "Cache_write": 1.25,
        "Ramp_Y1": 0.40,
        "Ramp_Y2": 0.85,
        "Ramp_Y3": 1.00
    },
    "Best": {
        "Complaints_m": 40000,
        "AHT": 25,
        "Cost_hr": 400,
        "Adoption": 0.90,
        "Acceptance": 0.92,
        "Realisation": 0.65,
        "Esc_rate": 0.03,
        "Esc_cut": 0.22,
        "Esc_cost": 5000,
        "FX": 88,
        "Disc": 0.12,
        "Cache_hit": 0.90,
        "Cache_write": 1.25,
        "Ramp_Y1": 0.40,
        "Ramp_Y2": 0.85,
        "Ramp_Y3": 1.00
    }
}

def calc_unit_costs(p):
    rows = []
    tot_cost_per_complaint = 0.0
    tot_min_saved = 0.0
    
    for uc in USE_CASES:
        pr = PRICES[uc["model"]]
        uncached = uc["input_tokens"] - uc["cacheable_tokens"]
        c_hit = uc["cacheable_tokens"] * p["Cache_hit"]
        c_miss = uc["cacheable_tokens"] * (1 - p["Cache_hit"])
        
        # Micro-dollar calculation per 1M tokens
        call_cost_usd = (
            uncached * pr["input"] +
            c_hit * pr["cached"] +
            c_miss * pr["input"] * p["Cache_write"] +
            uc["output_tokens"] * pr["output"]
        ) / 1000000.0
        
        cost_per_complaint_usd = call_cost_usd * uc["calls_per_complaint"] * uc["coverage"]
        min_saved = uc["min_saved_per_covered"] * uc["coverage"]
        
        tot_cost_per_complaint += cost_per_complaint_usd
        tot_min_saved += min_saved
        
        rows.append({
            "use_case": uc["name"],
            "model": uc["model"],
            "call_cost_usd": call_cost_usd,
            "cost_per_complaint_usd": cost_per_complaint_usd,
            "min_saved": min_saved
        })
        
    return rows, tot_cost_per_complaint, tot_min_saved

def run_model(p):
    rows, cost_per_comp_usd, min_per_comp = calc_unit_costs(p)
    
    ramps = [0.0, p["Ramp_Y1"], p["Ramp_Y2"], p["Ramp_Y3"]]
    complaints_ai = [p["Complaints_m"] * 12 * p["Adoption"] * r for r in ramps]
    hours_saved = [c * min_per_comp * p["Acceptance"] / 60.0 for c in complaints_ai]
    labour_gross = [h * p["Cost_hr"] for h in hours_saved]
    hard_benefit = [lg * p["Realisation"] for lg in labour_gross]
    soft_benefit = [c * p["Esc_rate"] * p["Esc_cut"] * p["Esc_cost"] for c in complaints_ai]
    full_benefit = [h + s for h, s in zip(hard_benefit, soft_benefit)]
    
    build_cost = [sum(BUILD_COSTS), 0.0, 0.0, 0.0]
    run_excl_tokens = [0.0, sum(RUN_COSTS_EXCL_TOKENS), sum(RUN_COSTS_EXCL_TOKENS), sum(RUN_COSTS_EXCL_TOKENS)]
    token_cost = [c * cost_per_comp_usd * p["FX"] for c in complaints_ai]
    total_cost = [b + r + t for b, r, t in zip(build_cost, run_excl_tokens, token_cost)]
    
    net_hard = [h - tc for h, tc in zip(hard_benefit, total_cost)]
    net_full = [f - tc for f, tc in zip(full_benefit, total_cost)]
    
    cum_hard = np.cumsum(net_hard).tolist()
    cum_full = np.cumsum(net_full).tolist()
    
    # Payback calculation
    def get_payback(cum_list, net_list):
        for y in range(1, 4):
            if cum_list[y-1] < 0 and cum_list[y] >= 0:
                frac = -cum_list[y-1] / net_list[y]
                return (y - 1) + frac
        return None

    pb_hard = get_payback(cum_hard, net_hard)
    pb_full = get_payback(cum_full, net_full)
    
    # NPV calculation: Y0 + NPV(disc, Y1..Y3)
    # in numpy, npf.npv or manual
    disc = p["Disc"]
    npv_hard = net_hard[0] + sum(net_hard[y] / ((1 + disc) ** y) for y in [1, 2, 3])
    npv_full = net_full[0] + sum(net_full[y] / ((1 + disc) ** y) for y in [1, 2, 3])
    
    # 3-year ROI: (Total Benefit - Total Cost) / Total Cost
    tot_full_benefit = sum(full_benefit)
    tot_cost = sum(total_cost)
    roi_full = (tot_full_benefit - tot_cost) / tot_cost
    
    token_share = sum(token_cost) / tot_cost
    cost_per_complaint_inr = cost_per_comp_usd * p["FX"]
    
    return {
        "unit_rows": rows,
        "cost_per_complaint_usd": cost_per_comp_usd,
        "cost_per_complaint_inr": cost_per_complaint_inr,
        "min_per_complaint": min_per_comp,
        "net_hard": net_hard,
        "net_full": net_full,
        "cum_hard": cum_hard,
        "cum_full": cum_full,
        "npv_hard": npv_hard,
        "npv_full": npv_full,
        "pb_hard": pb_hard,
        "pb_full": pb_full,
        "roi_full": roi_full,
        "token_share": token_share,
        "tot_full_benefit": tot_full_benefit,
        "tot_cost": tot_cost
    }

if __name__ == "__main__":
    print("=== HAND-CHECK: Policy Q&A ===")
    p_base = SCENARIOS["Base"]
    res_base = run_model(p_base)
    policy_row = [r for r in res_base["unit_rows"] if r["use_case"] == "Policy knowledge Q&A"][0]
    print(f"Policy Q&A Call Cost USD: ${policy_row['call_cost_usd']:.5f} (Target: $0.01702)")
    assert abs(policy_row['call_cost_usd'] - 0.01702) < 1e-6, "Hand-check failed!"
    print("HAND-CHECK PASSED!\n")

    print("=== SCENARIO EVALUATION SUMMARY ===")
    summary_data = []
    for sc_name in ["Worst", "Base", "Best"]:
        res = run_model(SCENARIOS[sc_name])
        pb_f_str = f"{res['pb_full']:.2f} yrs ({res['pb_full']*12:.1f} mos)" if res['pb_full'] else "Not within 3 yrs"
        pb_h_str = f"{res['pb_hard']:.2f} yrs" if res['pb_hard'] else "Not within 3 yrs"
        summary_data.append({
            "Scenario": sc_name,
            "NPV Full (INR)": f"₹{res['npv_full']:,.0f}",
            "NPV Full (Lakh)": f"₹{res['npv_full']/100000:.1f} L",
            "NPV Hard (INR)": f"₹{res['npv_hard']:,.0f}",
            "NPV Hard (Lakh)": f"₹{res['npv_hard']/100000:.1f} L",
            "Payback Full": pb_f_str,
            "Payback Hard": pb_h_str,
            "3-Yr ROI (Full)": f"{res['roi_full']*100:.1f}%",
            "Token Share": f"{res['token_share']*100:.1f}%",
            "Cost/Complaint": f"₹{res['cost_per_complaint_inr']:.2f}"
        })
    df_sc = pd.DataFrame(summary_data)
    print(df_sc.to_string(index=False))

    # Generate Tornado Sensitivity Chart
    print("\n=== GENERATING TORNADO CHART ===")
    # Data from Tornado sheet
    drivers = [
        "Adoption (0.50 - 0.95)",
        "Escalation Cost (₹2.5k - ₹8k)",
        "Realisation (30% - 70%)",
        "Minutes Saved (0.6x - 1.3x)",
        "Agent Cost (₹300 - ₹500/hr)",
        "Run Cost (0.75x - 1.5x)",
        "Acceptance Rate (65% - 95%)",
        "Token Price (0.5x - 3.0x)"
    ]
    low_diff = [-116.1, -75.4, -69.2, -69.2, -43.2, 24.0, -40.7, 7.1]
    high_diff = [58.0, 90.5, 69.2, 51.9, 43.2, -48.0, 20.3, -28.5]
    
    fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
    y_pos = np.arange(len(drivers))[::-1]
    
    # Plot bars
    ax.barh(y_pos, low_diff, align='center', color='#ef4444', height=0.55, label='Low Case vs Base')
    ax.barh(y_pos, high_diff, align='center', color='#22c55e', height=0.55, label='High Case vs Base')
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(drivers, fontsize=9, fontweight='medium')
    ax.axvline(0, color='#0f172a', lw=1.2, ls='--')
    ax.set_xlabel('Change in 3-Year NPV vs Base Case (₹ Lakh)', fontsize=10, fontweight='bold')
    ax.set_title('Tornado Sensitivity Analysis: Kestrel Bank GenAI Business Case\nBase Case Full NPV: ₹127.5 Lakh', fontsize=12, fontweight='bold', pad=15)
    ax.legend(loc='lower right', frameon=True)
    ax.grid(axis='x', linestyle=':', alpha=0.6)
    
    # Add values text
    for i, (l, h) in enumerate(zip(low_diff, high_diff)):
        yp = y_pos[i]
        if l < 0:
            ax.text(l - 3, yp, f"{l:+.1f}L", va='center', ha='right', fontsize=8, color='#991b1b', weight='bold')
        else:
            ax.text(l + 3, yp, f"{l:+.1f}L", va='center', ha='left', fontsize=8, color='#166534', weight='bold')
            
        if h > 0:
            ax.text(h + 3, yp, f"{h:+.1f}L", va='center', ha='left', fontsize=8, color='#166534', weight='bold')
        else:
            ax.text(h - 3, yp, f"{h:+.1f}L", va='center', ha='right', fontsize=8, color='#991b1b', weight='bold')
            
    ax.set_xlim(-140, 120)
    plt.tight_layout()
    tornado_img_path = "02_A2_business_case/outputs/tornado.png"
    import os
    os.makedirs("02_A2_business_case/outputs", exist_ok=True)
    plt.savefig(tornado_img_path)
    plt.close()
    print(f"Saved tornado chart to {tornado_img_path}")
