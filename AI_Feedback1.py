import streamlit as st
import pandas as pd
import openai

st.title("🤖 GPT-Powered Match Feedback")

openai.api_key = st.text_input("🔑 OpenAI API Key", type="password")

try:
    resume_df = pd.read_csv("resume_cleaned.csv")
    jd_df = pd.read_csv("jd_cleaned.csv")
except Exception as e:
    st.error(f"🚨 Failed to load data: {e}")
    st.stop()

res_idx = st.number_input("Select Resume Index", 0, len(resume_df)-1, 0)
jd_idx = st.number_input("Select JD Index", 0, len(jd_df)-1, 0)

if st.button("💬 Generate Match Feedback"):
    if not openai.api_key:
        st.warning("Please enter your OpenAI API key to use this feature.")
    else:
        prompt = f"""
Compare this resume to the job description and explain why it is a good or bad match.

Resume:
{resume_df['Resume_str'].iloc[res_idx]}

Job Description:
{jd_df['Job Description'].iloc[jd_idx]}
"""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            feedback = response.choices[0].message["content"]
            st.success("✅ Feedback Generated:")
            st.write(feedback)
        except Exception as e:
            st.error(f"🚨 GPT error: {e}")
