import os

required_files = [
    "resume_cleaned.csv",
    "jd_cleaned.csv",
    "resume_embeddings.npy",
    "jd_embeddings.npy"
]

# app.py
import streamlit as st
import os
import pandas as pd
import numpy as np

st.set_page_config(page_title="SmartHire Pro", layout="wide")

# Sidebar Navigation
st.sidebar.title("📂 SmartHire Pro")
st.sidebar.markdown("Navigate between modules:")

# Title
st.title("💼 SmartHire Pro: AI-Powered Resume & JD Matcher")
st.markdown("Welcome to your project dashboard. Use the sidebar to explore each module.")

# Check if preprocessed files exist
required_files = [
    "resume_cleaned.csv",
    "jd_cleaned.csv",
    "resume_embeddings.npy",
    "jd_embeddings.npy"
]

missing = [f for f in required_files if not os.path.exists(f)]

if missing:
    st.warning(f"⚠️ Missing files: {', '.join(missing)}.\nPlease run `preprocess.py` to generate required data.")
    st.stop()

# Load Data
try:
    resume_df = pd.read_csv("resume_cleaned.csv")
    jd_df = pd.read_csv("jd_cleaned.csv")
    resume_embeddings = np.load("resume_embeddings.npy")
    jd_embeddings = np.load("jd_embeddings.npy")
except Exception as e:
    st.error(f"🚨 Error loading data: {e}")
    st.stop()

# Show data sample preview
with st.expander("🔍 Preview Processed Data"):
    st.write("**Resumes:**", resume_df.head(3))
    st.write("**Job Descriptions:**", jd_df.head(3))

st.success("✅ All required data files loaded successfully!")
st.info("Use the sidebar to open the modules: \n\n- 🧠 Matcher\n- 📊 Analytics\n- 🤖 AI Feedback")


