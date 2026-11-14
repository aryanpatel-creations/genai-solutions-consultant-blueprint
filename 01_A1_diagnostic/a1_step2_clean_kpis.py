import pandas as pd

df = pd.read_csv("bank_complaints_24m.csv", dtype=str)

# 1. Types
for col in ["Date received", "Date sent to company"]:
    df[col] = pd.to_datetime(df[col], format="mixed", errors="coerce")

# 2. Duplicates: one row per Complaint ID
before = len(df)
df = df.drop_duplicates(subset="Complaint ID", keep="last")
print("Duplicates removed:", before - len(df))

# 3. Derived fields (flags, never silent fixes)
df["month"] = df["Date received"].dt.to_period("M").astype(str)
df["routing_lag_days"] = (df["Date sent to company"] - df["Date received"]).dt.days
df["flag_bad_dates"] = df["routing_lag_days"].isna() | (df["routing_lag_days"] < 0)
df["timely"] = df["Timely response?"].eq("Yes")
df["relief"] = df["Company response to consumer"].isin(
    ["Closed with monetary relief", "Closed with non-monetary relief"])
df["has_narrative"] = df["Consumer complaint narrative"].fillna("").str.strip().ne("")

# 4. Baseline KPI table
months = df["month"].nunique()
kpis = {
    "Complaints in window": len(df),
    "Average complaints per month": round(len(df) / months),
    "Timely response rate (%)": round(100 * df["timely"].mean(), 1),
    "Median routing lag (days)": df.loc[~df["flag_bad_dates"], "routing_lag_days"].median(),
    "Share closed with relief (%)": round(100 * df["relief"].mean(), 1),
    "Share submitted via web (%)": round(100 * df["Submitted via"].eq("Web").mean(), 1),
    "Share with a narrative (%)": round(100 * df["has_narrative"].mean(), 1),
    "Rows with bad dates (flagged)": int(df["flag_bad_dates"].sum()),
}
baseline = pd.Series(kpis, name="Baseline")
print(baseline)
baseline.to_csv("baseline_kpis.csv")
df.to_csv("complaints_clean.csv", index=False)

# 5. Outcome mix and relief rate by issue (where the bank was most often at fault)
print(df["Company response to consumer"].value_counts(normalize=True).round(3))
relief_by_issue = (df.groupby("Issue")
                     .agg(complaints=("Complaint ID", "count"), relief_rate=("relief", "mean"))
                     .sort_values("complaints", ascending=False))
relief_by_issue["relief_rate"] = (100 * relief_by_issue["relief_rate"]).round(1)
print(relief_by_issue.head(10))
relief_by_issue.to_csv("relief_by_issue.csv")
