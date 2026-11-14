import sys
import pandas as pd

# The full CFPB download (large), read in chunks. Try it first on the synthetic sample:
#   python a1_step1_load.py data/SYNTHETIC_sample_complaints.csv
RAW = sys.argv[1] if len(sys.argv) > 1 else "data/complaints.csv"
PRODUCTS = r"Checking or savings account|Credit card"   # bank products only
START, END = "2024-09-01", "2026-08-31"                   # a 24-month window

keep = []
for chunk in pd.read_csv(RAW, chunksize=200_000, dtype=str):
    chunk["Date received"] = pd.to_datetime(chunk["Date received"],
                                            format="mixed", errors="coerce")
    mask = (chunk["Product"].str.contains(PRODUCTS, case=False, na=False)
            & chunk["Date received"].between(START, END))
    keep.append(chunk[mask])

df = pd.concat(keep, ignore_index=True)
df.to_csv("bank_complaints_24m.csv", index=False)
print(df.shape)
print(df["Product"].value_counts())
