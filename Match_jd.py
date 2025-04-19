import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

st.title("🧠 Resume–JD Matching Engine")

try:
    resume_df = pd.read_csv("resume_cleaned.csv")
    jd_df = pd.read_csv("jd_cleaned.csv")
    resume_embeddings = np.load("resume_embeddings.npy")
    jd_embeddings = np.load("jd_embeddings.npy")
except Exception as e:
    st.error(f"🚨 Failed to load data: {e}")
    st.stop()

# Filters
search_keyword = st.text_input("🔍 Search resumes for keyword (e.g. Python, MBA):")
if search_keyword:
    mask = resume_df['Resume_str'].str.contains(search_keyword, case=False, na=False)
    resume_df = resume_df[mask].reset_index(drop=True)
    resume_embeddings = resume_embeddings[mask]

roles = jd_df['Role'].dropna().unique().tolist() if 'Role' in jd_df.columns else []
selected_roles = st.multiselect("🎯 Filter by JD Role", roles, default=roles)
if selected_roles:
    mask = jd_df['Role'].isin(selected_roles)
    jd_df = jd_df[mask].reset_index(drop=True)
    jd_embeddings = jd_embeddings[mask]

top_n = st.slider("📈 Top N Matches per Resume", 1, 10, 3)
threshold = st.slider("🎯 Score Threshold", 0.0, 1.0, 0.75)

# Matching Logic
if resume_embeddings.shape[0] == 0 or jd_embeddings.shape[0] == 0:
    st.warning("⚠️ No resumes or job descriptions found after filtering.")
    st.stop()

match_scores = cosine_similarity(resume_embeddings, jd_embeddings)
results = []

for i, row in enumerate(match_scores):
    top_idx = row.argsort()[::-1][:top_n]
    for j in top_idx:
        score = row[j]
        if score >= threshold:
            results.append({
                "Resume #": i+1,
                "JD #": j+1,
                "Resume": resume_df['Resume_str'].iloc[i][:300],
                "JD": jd_df['Job Description'].iloc[j][:300],
                "Score": round(score, 3)
            })

df = pd.DataFrame(results)
st.subheader("🎯 Matching Results")
st.dataframe(df, use_container_width=True)

if not df.empty:
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download as CSV", csv, "Smarthire_matches.csv", "text/csv")
