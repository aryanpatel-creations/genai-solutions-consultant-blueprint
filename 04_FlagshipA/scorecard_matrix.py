"""Draw the value-vs-feasibility matrix from the Scorecard sheet of Flagship_A_templates.xlsx.

Run:  python scorecard_matrix.py      ->  matrix.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("Flagship_A_templates.xlsx", sheet_name="Scorecard", header=2).dropna(subset=["Use case"])
scores = ["Financial value", "Customer / regulatory", "Data readiness", "Technical", "Risk (5 = low)", "Adoption"]
df[scores] = df[scores].astype(float)
df["value"] = df[scores[:2]].mean(axis=1)                 # same formulas as the sheet
df["feasibility"] = df[scores[2:]].mean(axis=1)
df["total"] = df[scores].sum(axis=1)
df["result"] = ["Reject" if m == 1 else ("Pass" if t >= 20 else "Not yet")
                for t, m in zip(df["total"], df[scores].min(axis=1))]
colour = {"Pass": "#1a9a6c", "Not yet": "#e07b00", "Reject": "#52514e"}

fig, ax = plt.subplots(figsize=(10, 6))
ax.axvline(3.5, color="#d9d8d3"); ax.axhline(3.5, color="#d9d8d3")
ax.text(4.95, 4.95, "DO FIRST", ha="right", va="top", weight="bold", color="#1a9a6c")
ax.text(1.05, 4.95, "PLAN CAREFULLY", va="top", weight="bold", color="#e07b00")
ax.text(4.95, 1.05, "QUICK WINS", ha="right", weight="bold", color="#2a78d6")
ax.text(1.05, 1.05, "DON'T DO (NOW)", weight="bold", color="#52514e")
for _, r in df.iterrows():
    ax.scatter(r["feasibility"], r["value"], s=260, color=colour[r["result"]], edgecolor="white", zorder=3)
    ax.text(r["feasibility"], r["value"], str(int(r["#"])), ha="center", va="center", color="white",
            fontsize=9, weight="bold", zorder=4)
ax.set_xlim(1, 5); ax.set_ylim(1, 5)
ax.set_xlabel("Feasibility (average of data, technical, risk, adoption)")
ax.set_ylabel("Value (average of financial and customer/regulatory)")
legend = "\n".join(f'{int(r["#"])}  {r["Use case"]}  ({r["result"]})' for _, r in df.iterrows())
fig.text(0.70, 0.5, legend, va="center", fontsize=9)
plt.subplots_adjust(right=0.66)
plt.savefig("matrix.png", dpi=200)
print(df[["Use case", "total", "value", "feasibility", "result"]].to_string(index=False))
