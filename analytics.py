import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import plotly.express as px

st.title("📊 SmartHire Analytics")

try:
    resume_df = pd.read_csv("resume_cleaned.csv")
    jd_df = pd.read_csv("jd_cleaned.csv")
except Exception as e:
    st.error(f"🚨 Failed to load data: {e}")
    st.stop()

# WordCloud
st.subheader("🧠 Resume Word Cloud")
text = " ".join(resume_df['cleaned_resume'].fillna("").astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)

# JD Role Distribution
if 'Role' in jd_df.columns:
    st.subheader("📈 JD Role Distribution")
    role_counts = jd_df['Role'].value_counts().reset_index()
    role_counts.columns = ['Role', 'Count']
    fig = px.bar(role_counts, x='Role', y='Count', title="JD Roles by Frequency")
    st.plotly_chart(fig, use_container_width=True)
