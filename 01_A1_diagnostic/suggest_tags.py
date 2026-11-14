import re
import pandas as pd

def classify_narrative(text, issue):
    t = str(text).lower()
    iss = str(issue).lower()

    # Default
    cause = "Process"
    ai = "Knowledge"

    # Rules for root cause
    if any(k in t for k in ["fee", "interest", "apr", "annual fee", "overdraft fee", "late fee", "charged"]):
        if any(k in t for k in ["policy", "terms", "contract", "rate increased", "unfair"]):
            cause = "Policy"
            ai = "None"  # Fix the policy / refund
        elif any(k in t for k in ["explained", "disclose", "didn't know", "surprise"]):
            cause = "Information"
            ai = "Draft"
        else:
            cause = "Process"
            ai = "Knowledge"
    elif any(k in t for k in ["transferred", "hold", "called", "representative", "agent", "told me", "rude"]):
        if any(k in t for k in ["misinformed", "told me wrong", "rude", "unprofessional"]):
            cause = "People"
            ai = "Knowledge"
        else:
            cause = "Process"
            ai = "Triage"
    elif any(k in t for k in ["fraud", "unauthorized", "scam", "stolen", "hacked", "identity"]):
        cause = "System"
        ai = "Summary"
    elif any(k in t for k in ["app", "website", "online", "login", "error", "glitch", "crash", "locked"]):
        cause = "System"
        ai = "Triage"
    elif any(k in t for k in ["misunderstood", "confused", "thought", "didn't realize"]):
        cause = "Customer understanding"
        ai = "Draft"

    return cause, ai

def enrich_sample():
    csv_path = "narrative_sample_to_tag.csv"
    df = pd.read_csv(csv_path)
    
    suggested_causes = []
    suggested_ais = []
    
    for _, row in df.iterrows():
        c, a = classify_narrative(row["Consumer complaint narrative"], row["Issue"])
        suggested_causes.append(c)
        suggested_ais.append(a)
        
    df["suggested_root_cause"] = suggested_causes
    df["suggested_ai_could_help"] = suggested_ais
    
    # Save back with suggestion columns
    df.to_csv("narrative_sample_to_tag.csv", index=False)
    print(f"Enriched {len(df)} sample complaints with suggested tags.")
    print("Suggested root causes breakdown:")
    print(df["suggested_root_cause"].value_counts())
    print("\nSuggested AI-could-help breakdown:")
    print(df["suggested_ai_could_help"].value_counts())

if __name__ == "__main__":
    enrich_sample()
