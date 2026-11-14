import os
import re
import urllib.request
import zipfile
import pandas as pd

RAW_DIR = os.path.join(os.path.dirname(__file__), "data", "raw")
ZIPS_DIR = os.path.join(RAW_DIR, "narrative_zips")
os.makedirs(ZIPS_DIR, exist_ok=True)

ARCHIVE_PAGE = "https://www.consumerfinance.gov/foia-requests/foia-electronic-reading-room/cfpb-consumer-complaint-database-narratives-archive/"

def get_archive_urls():
    req = urllib.request.Request(ARCHIVE_PAGE, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode("utf-8")
    
    links = re.findall(r'href=["\'](https://files\.consumerfinance\.gov/f/documents/CCDB_Export_[^"\']+\.zip)["\']', html)
    # The archives covering August 2024 to August 2026 are Export 7 to Export 21
    target_links = []
    for link in links:
        match = re.search(r'CCDB_Export_(\d+)_', link)
        if match:
            num = int(match.group(1))
            if 7 <= num <= 21:
                target_links.append(link)
    return target_links

def download_and_extract_narratives(target_complaint_ids):
    target_links = get_archive_urls()
    print(f"Found {len(target_links)} narrative archive files covering Sept 2024 - Aug 2026.")
    
    narratives_map = {}
    
    for url in target_links:
        filename = os.path.basename(url)
        zip_path = os.path.join(ZIPS_DIR, filename)
        
        # Check if already downloaded in RAW_DIR (like Export 21)
        existing_in_raw = os.path.join(RAW_DIR, filename)
        if os.path.exists(existing_in_raw) and not os.path.exists(zip_path):
            import shutil
            shutil.copy2(existing_in_raw, zip_path)
            
        if not os.path.exists(zip_path):
            print(f"Downloading {filename}...")
            urllib.request.urlretrieve(url, zip_path)
        else:
            print(f"Using cached {filename}...")
            
        # Read narratives from zip directly without extracting entire CSV to disk
        with zipfile.ZipFile(zip_path) as z:
            for csv_name in z.namelist():
                if csv_name.endswith(".csv"):
                    with z.open(csv_name) as f:
                        for chunk in pd.read_csv(f, usecols=["Complaint ID", "Consumer complaint narrative"], dtype=str, chunksize=50000):
                            chunk = chunk[chunk["Consumer complaint narrative"].fillna("").str.strip().ne("")]
                            matched = chunk[chunk["Complaint ID"].isin(target_complaint_ids)]
                            for _, row in matched.iterrows():
                                narratives_map[row["Complaint ID"]] = row["Consumer complaint narrative"]
        print(f"Total narratives collected so far: {len(narratives_map)}")
        
    return narratives_map

if __name__ == "__main__":
    bank_complaints_path = os.path.join(os.path.dirname(__file__), "bank_complaints_24m.csv")
    if not os.path.exists(bank_complaints_path):
        print(f"Waiting for {bank_complaints_path}...")
    else:
        df_bank = pd.read_csv(bank_complaints_path, dtype=str)
        target_ids = set(df_bank["Complaint ID"].dropna())
        print(f"Target bank complaints: {len(target_ids)}")
        narr_map = download_and_extract_narratives(target_ids)
        df_bank["Consumer complaint narrative"] = df_bank["Complaint ID"].map(narr_map).fillna("")
        df_bank.to_csv(bank_complaints_path, index=False)
        print("Updated bank_complaints_24m.csv with Consumer complaint narrative column!")
        print(f"Complaints with narrative: {df_bank['Consumer complaint narrative'].ne('').sum()}")
