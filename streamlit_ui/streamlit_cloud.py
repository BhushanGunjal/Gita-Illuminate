import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from main_functionality.recommendation import generate_recommendations
import numpy as np

# Load preprocessed data
DATA_PATH = "data/data/processed_data.pkl"
MODEL_NAME = "all-MiniLM-L6-v2"

data = pd.read_pickle(DATA_PATH)
embeddings_matrix = np.array(data['Embeddings'].tolist())
embedding_model = SentenceTransformer(MODEL_NAME)

# Set page configuration with a title
st.set_page_config(page_title="गीता-Illuminate  कृष्णं सदा सहायते", page_icon="🔍", layout="wide")

# Title of the app
st.markdown('<h1 class="title">🔍 गीता-Illuminate 🔍</h1>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Background and style
st.markdown(
    """
    <style>
        body {
            background-color: #f9f5ec;
            font-family: 'Mukta', sans-serif;
        }
        .main {
            background-color: #f9f5ec;
        }
        .stButton>button {
            background-color: #FF8C00;
            color: black;
            font-size: 18px;
            padding: 10px 25px;
            border-radius: 10px;
            border: 2px solid #DAA520;
        }
        .stTextArea>div>div>textarea {
            font-size: 18px;
            font-family: 'Mukta', sans-serif;
            padding: 12px;
            border-radius: 10px;
        }
        .title {
            font-size: 50px;
            color: #8B0000;
            font-family: 'Mukta', sans-serif;
            text-align: center;
        }
        .shloka {
            font-size: 20px;
            color: #2E8B57;
            text-align: center;
            font-family: 'Mukta', serif;
            line-height: 1.8;
        }
        .translation {
            font-size: 18px;
            color: #FFFFFF;
            text-align: center;
            margin-top: -15px;
            font-family: 'Mukta', serif;
        }
        .recommendation {
            background-color: #000000;
            border: 1px solid #ffebcd;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
        }
        .image-container {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Divine Krishna Shloka
st.markdown(
    """
    <div class="shloka">
        <p><b>सर्वधर्मान्परित्यज्य मामेकं शरणं व्रज।<br>
        अहं त्वा सर्वपापेभ्यो मोक्षयिष्यामि मा शुचः ॥॥</b></p>
        <p class="translation"><i>"Abandon all varieties of religion and just surrender unto Me. I shall deliver you from all sinful reactions. Do not fear."</i><br>
        <strong>- Bhagavad Gita 18.66</strong></p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Add Krishna's image
st.markdown('<div class="image-container">', unsafe_allow_html=True)
st.image("krishna_bg.jpg", caption="Lord Krishna", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Input form for life situation or query
user_input = st.text_area("🔍 Describe your life situation or query:")

# Recommendation Button
if st.button("🌟 Get Divine Guidance"):
    if user_input.strip():
        st.write("✨ Seeking wisdom from the Bhagavad Gita... Please wait.")
        recommendations = generate_recommendations(user_input, data, embeddings_matrix, embedding_model)
        if not recommendations.empty:
            st.subheader("🌸 Your Divine Recommendations 🌸")
            for _, row in recommendations.iterrows():
                st.markdown(
                    f"""
                    <div class="recommendation">
                        <h3>{row['Title']}</h3>
                        <p><b>Sanskrit Shloka:</b> {row['Sanskrit Anuvad']}</p>
                        <p><b>English Translation:</b> {row['English Translation']}</p>
                        <p><b>Suggested Solution:</b> {row['Suggested Solution']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.error("No recommendations found. Please try a different query.")
    else:
        st.error("Please enter a valid query or life situation.")
