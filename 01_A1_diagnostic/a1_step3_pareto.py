import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("complaints_clean.csv", dtype=str)
counts = df["Issue"].value_counts()
top = counts.head(12)
cum_pct = 100 * top.cumsum() / counts.sum()   # cumulative share of ALL complaints

fig, ax = plt.subplots(figsize=(11, 5))
sns.barplot(x=top.values, y=top.index, ax=ax, color="#2a78d6")
ax.set_xlabel("Number of complaints")
ax.set_ylabel("")
ax.set_title("Top complaint issues (Pareto)")
for i, (v, c) in enumerate(zip(top.values, cum_pct.values)):
    ax.text(v, i, f"  {c:.0f}% cumulative", va="center", fontsize=8)
plt.tight_layout()
plt.savefig("pareto_issues.png", dpi=200)

# How many issues make up 80% of complaints?
all_cum = 100 * counts.cumsum() / counts.sum()
n80 = int((all_cum < 80).sum()) + 1
print("Issues needed to reach 80% of complaints:", n80, "of", len(counts))
