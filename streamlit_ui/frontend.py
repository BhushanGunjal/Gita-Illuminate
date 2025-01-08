import streamlit as st
import requests
import pandas as pd
import subprocess
import time





API_URL = "http://127.0.0.1:8000/recommendations/"  # Update with your API URL


fastapi_process = None

def start_fastapi():
    global fastapi_process
    try:
        # Check if API is already running
        requests.get(API_URL)
    except requests.ConnectionError:
        # If not running, start FastAPI server
        fastapi_process = subprocess.Popen(["uvicorn", "api.api:app", "--host", "127.0.0.1", "--port", "8000"])
        time.sleep(2)  # Give some time for the server to start

# Ensure FastAPI server starts
start_fastapi()


# Helper function to fetch recommendations
def fetch_recommendations(input_text):
    """
    Send user input to FastAPI and fetch recommendations.
    :param input_text: Raw user input string.
    :return: List of recommendations.
    """

    # Check for suicide-related keywords
    sensitive_keywords = ["suicide", "end my life", "kill myself", "hopeless", "no reason to live"]
    if any(keyword in input_text.lower() for keyword in sensitive_keywords):
        st.error("In the darkest moments, light emerges. We understand you might be going through a tough time. Please know that help is available. ")
        st.markdown("""
        **💬 Immediate Support Resources:**
        - Call a trusted friend or family member.
        - Contact a mental health professional.
        - Reach out to a suicide prevention helpline near you:
          - [India](https://www.aasra.info): 91-9820466726 / 91-22-27546669
        """, unsafe_allow_html=True)
        
    


    try:
        response = requests.post(API_URL, json={"input_text": input_text})
        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            st.error("Error: Unable to fetch recommendations.")
            return None

    except requests.ConnectionError:
        st.error("Error: Unable to connect to the API. Please try again later.")
        return None



# Set page configuration with a title
st.set_page_config(page_title="गीता-Illuminate  कृष्णं सदा सहायते", page_icon="🕉️", layout="wide")




# Title of the app
st.markdown('<h1 class="title">🕉️ गीता-Illuminate 🕉️</h1>', unsafe_allow_html=True)
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
        <p><b>सर्वधर्मान्परित्यज्य मामेकं शरणं व्रज ।<br>
        अहं त्वा सर्वपापेभ्यो मोक्षयिष्यामि मा शुचः ॥</b></p>
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
user_input = st.text_area("🕉️ Describe your life situation or query:")




# Recommendation Button
if st.button("🌟 Get Divine Guidance"):
    if user_input.strip():
        st.write("✨ Seeking wisdom from the Bhagavad Gita... Please wait.")
        recommendations = fetch_recommendations(user_input)
        if recommendations is not None:
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
            st.error("Unable to retrieve recommendations. Please try again later.")
    else:
        st.error("Please enter a valid query or life situation.")




# Disclaimer Section
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    """
    #### Disclaimer
    **गीता-Illuminate** is designed as a spiritual guide based on the teachings of the Bhagavad Gita. It provides general guidance and reflections, but it is **not a substitute for professional advice**, including medical, legal, financial, or mental health services. For any serious concerns, especially mental health issues, please consult a qualified professional or contact a helpline in your region.
    """, 
    unsafe_allow_html=True
)





# Footer Style
st.markdown(
    """
    <style>
        hr {
            border: 0;
            height: 1px;
            background: #DAA520;
        }
    </style>
    """,
    unsafe_allow_html=True
)