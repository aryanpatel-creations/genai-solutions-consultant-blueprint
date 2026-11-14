import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Narratives come from the CFPB archive files, filtered the same way as Step 1
df = pd.read_csv("complaints_clean.csv", dtype=str)
text = df["Consumer complaint narrative"].fillna("").str.strip()
narr = df[text.ne("")].copy()

# A. 100 complaints to read and tag by hand (the most valuable part)
sample = narr.sample(n=min(100, len(narr)), random_state=42)
sample[["Complaint ID", "Product", "Issue", "Consumer complaint narrative"]].assign(
    root_cause="", ai_could_help="").to_csv("narrative_sample_to_tag.csv", index=False)

# B. Optional: find themes automatically (reuses your K-Means skills from project #2)
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
stops = list(ENGLISH_STOP_WORDS | {"xxxx", "xx"})   # CFPB masks private details as XXXX
vec = TfidfVectorizer(stop_words=stops, max_features=5000, min_df=5,
                      token_pattern=r"(?u)\b[a-zA-Z]{3,}\b")   # words of 3+ letters only
X = vec.fit_transform(narr["Consumer complaint narrative"])
k = 6
km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X)
narr["theme"] = km.labels_
terms = vec.get_feature_names_out()
for i, centre in enumerate(km.cluster_centers_):
    top_words = [terms[j] for j in centre.argsort()[-8:][::-1]]
    print(f"Theme {i} ({(narr['theme'] == i).sum()} complaints):", ", ".join(top_words))
