import streamlit as st
import pandas as pd
import random

st.title("🤖 Smart Feedback Generator (Keyless GPT Mode)")
st.caption("🔐 No API key required – ready for viva, offline demo, and mock presentations!")

# Load cleaned data
try:
    resume_df = pd.read_csv("resume_cleaned.csv")
    jd_df = pd.read_csv("jd_cleaned.csv")
except Exception as e:
    st.error(f"🚨 Couldn’t load data: {e}")
    st.stop()

# Select a resume & JD
res_idx = st.number_input("Select Resume Index", 0, len(resume_df) - 1, 0)
jd_idx = st.number_input("Select JD Index", 0, len(jd_df) - 1, 0)

resume_text = resume_df['Resume_str'].iloc[res_idx][:1000]
jd_text = jd_df['Job Description'].iloc[jd_idx][:1000]

# Define mock GPT-style templates
summaries = [
    "- Skilled in Python, SQL, and data wrangling.\n- Strong analytical and visualization skills.\n- Built end-to-end ML pipelines.",
    "- Proficient in NLP, deep learning, and model deployment.\n- Familiar with TensorFlow, Flask, and REST APIs.\n- Worked on chatbot systems.",
    "- Experienced in project-based learning with Kaggle competitions.\n- Solid understanding of statistics and predictive models.\n- Great communicator and team player."
]

feedbacks = [
    """✅ **Strong Match**: This candidate fits well due to overlapping technical skills like Python and ML.\n
⚠️ **Gaps**: Could enhance cloud tool exposure (AWS, GCP).\n
📌 **Suggestion**: Add measurable impact like 'reduced churn by 10%'.""",

    """✅ **Relevant Skills Found**: Resume includes data visualization and project experience.\n
⚠️ **Missing Elements**: No mention of teamwork or agile workflow.\n
📌 **Tip**: Include soft skills and leadership qualities for full-stack roles.""",

    """✅ **Alignment Noted**: Keywords such as NLP and transformers match JD.\n
⚠️ **Enhancement Needed**: Resume could benefit from certifications or recent training.\n
📌 **Recommendation**: Highlight academic achievements and hands-on projects."""
]

# On Button Press → Generate Simulated Feedback
if st.button("💬 Generate Simulated Feedback"):
    summary = random.choice(summaries)
    feedback = random.choice(feedbacks)

    st.subheader("📄 Resume Summary (Simulated)")
    st.markdown(summary)

    st.subheader("🎯 Match Feedback (Simulated GPT Style)")
    st.markdown(feedback)

    full_feedback = f"""Resume Summary:\n{summary}\n\nFeedback:\n{feedback}"""

    # Copyable & Downloadable
    st.download_button("📄 Download Feedback as TXT",
                       data=full_feedback,
                       file_name="Smarthire_feedback.txt")

    st.code(full_feedback, language="markdown")
