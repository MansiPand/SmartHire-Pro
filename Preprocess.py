# preprocess.py
import pandas as pd
import numpy as np
import re
from sentence_transformers import SentenceTransformer

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

resume_df = pd.read_csv("C:\\Users\\\pande\\Downloads\\archive (20)\\Resume\\Resume.csv")
jd_df = pd.read_csv("C:\\Users\\pande\\Downloads\\archive (21)\\jb_df.csv")

print(resume_df.head())
print(jd_df.head())

resume_df['cleaned_resume'] = resume_df['Resume_str'].apply(clean_text)
jd_df['cleaned_jd'] = jd_df['Job Description'].apply(clean_text)

model = SentenceTransformer('all-MiniLM-L6-v2')

resume_embeddings = model.encode(resume_df['cleaned_resume'].tolist(), show_progress_bar=True)
jd_embeddings = model.encode(jd_df['cleaned_jd'].tolist(), show_progress_bar=True)

resume_df.to_csv("resume_cleaned.csv", index=False)
jd_df.to_csv("jd_cleaned.csv", index=False)
np.save("resume_embeddings.npy", resume_embeddings)
np.save("jd_embeddings.npy", jd_embeddings)

print("✅ All files saved.")
