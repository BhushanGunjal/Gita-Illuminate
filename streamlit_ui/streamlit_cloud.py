import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import os
import sys
import nltk



# Get the absolute path of the current file (streamlit_cloud.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to sys.path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Now you can import from main_functionality
from main_functionality.recommendation import generate_recommendations


# Function to download NLTK resources (using st.cache_resource to avoid redundant downloads)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt_tab')

# Load preprocessed data
DATA_PATH = "data/processed_data.pkl"
MODEL_NAME = "all-MiniLM-L6-v2"

data = pd.read_pickle(DATA_PATH)
embeddings_matrix = np.array(data['Embeddings'].tolist())
embedding_model = SentenceTransformer(MODEL_NAME)

# Set page configuration with a title
st.set_page_config(page_title="गीता-Illuminate  कृष्णं सदा सहायते", page_icon="🔍", layout="wide")

# Title of the app
st.markdown('<h1 class="title">🔍 गीता-Illuminate 🔍</h1>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


# Suicide-related keywords check function
def check_suicide_keywords(input_text):
    sensitive_keywords = ["suicide", "end my life", "kill myself", "hopeless", "no reason to live"]
    return any(keyword in input_text.lower() for keyword in sensitive_keywords)



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

        if check_suicide_keywords(user_input):
            st.error("In the darkest moments, light emerges. We understand you might be going through a tough time. Please know that help is available.")
            st.markdown("""
            **💬 Immediate Support Resources:**
            - Call a trusted friend or family member.
            - Contact a mental health professional.
            - Reach out to a suicide prevention helpline near you:
              - [India](https://www.aasra.info): 91-9820466726 / 91-22-27546669
            """, unsafe_allow_html=True)



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
