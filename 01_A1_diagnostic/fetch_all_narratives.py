import subprocess
import os
import zipfile
import pandas as pd

RAW_DIR = r"C:\Users\aryan\Desktop\project 1 strategy\01_A1_diagnostic\data\raw"
ZIPS_DIR = os.path.join(RAW_DIR, "narrative_zips")
os.makedirs(ZIPS_DIR, exist_ok=True)

# List of all export URLs covering August 2024 to August 2026
EXPORTS = [
    "CCDB_Export_7_August_2024_through_October_2024.zip",
    "CCDB_Export_8_November_2024_through_December_2024.zip",
    "CCDB_Export_9_January_2025_through_February_2025.zip",
    "CCDB_Export_10_March_2025_through_April_2025.zip",
    "CCDB_Export_11_May_2025_through_June_2025.zip",
    "CCDB_Export_12_July_2025_through_August_2025.zip",
    "CCDB_Export_13_September_2025_through_October_2025.zip",
    "CCDB_Export_14_November_2025_through_December_2025.zip",
    "CCDB_Export_15_January_2026_through_February_2026.zip",
    "CCDB_Export_16_March_2026.zip",
    "CCDB_Export_17_April_2026.zip",
    "CCDB_Export_18_May_2026.zip",
    "CCDB_Export_19_June_2026.zip",
    "CCDB_Export_20_July_2026.zip",
    "CCDB_Export_21_August_2026.zip",
]

BASE_URL = "https://files.consumerfinance.gov/f/documents/"

def main():
    bank_path = r"C:\Users\aryan\Desktop\project 1 strategy\01_A1_diagnostic\bank_complaints_24m.csv"
    print("Loading bank complaints...")
    df_bank = pd.read_csv(bank_path, dtype=str)
    target_ids = set(df_bank["Complaint ID"].dropna())
    print(f"Total target Complaint IDs: {len(target_ids)}")

    narr_map = {}

    for exp in EXPORTS:
        dest = os.path.join(ZIPS_DIR, exp)
        # Check if already in RAW_DIR
        alt = os.path.join(RAW_DIR, exp)
        if os.path.exists(alt) and not os.path.exists(dest):
            dest = alt
            
        if not os.path.exists(dest):
            url = BASE_URL + exp
            print(f"Downloading {exp}...")
            cmd = ["curl.exe", "-s", "-L", "-o", dest, url]
            res = subprocess.run(cmd)
            if res.returncode != 0:
                print(f"Failed to download {exp}")
                continue
        
        print(f"Extracting narratives from {exp}...")
        try:
            with zipfile.ZipFile(dest) as z:
                for name in z.namelist():
                    if name.endswith(".csv"):
                        with z.open(name) as f:
                            for chunk in pd.read_csv(f, usecols=["Complaint ID", "Consumer complaint narrative"], dtype=str, chunksize=100000):
                                chunk = chunk[chunk["Consumer complaint narrative"].fillna("").str.strip().ne("")]
                                matched = chunk[chunk["Complaint ID"].isin(target_ids)]
                                for _, row in matched.iterrows():
                                    narr_map[row["Complaint ID"]] = row["Consumer complaint narrative"]
            print(f"  Narratives found so far: {len(narr_map)}")
        except Exception as e:
            print(f"Error reading {exp}: {e}")

    print(f"Total bank complaints with narratives matched: {len(narr_map)}")
    df_bank["Consumer complaint narrative"] = df_bank["Complaint ID"].map(narr_map).fillna("")
    df_bank.to_csv(bank_path, index=False)
    print("Saved bank_complaints_24m.csv with Consumer complaint narrative column!")

if __name__ == "__main__":
    main()
