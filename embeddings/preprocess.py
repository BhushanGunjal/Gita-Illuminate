


import streamlit as st
import nltk

# Get the current NLTK data paths
nltk_data_paths = nltk.data.path

# Display it in Streamlit UI
st.write("Current NLTK Data Paths:", nltk_data_paths)

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Function to download NLTK resources (using st.cache_resource to avoid redundant downloads)
@st.cache_resource
def download_nltk_resources():
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('stopwords')

# Download the resources at app startup
download_nltk_resources()




def preprocess_text(text):
    """
    Preprocesses input text by tokenizing, lemmatizing, and removing stopwords.
    :param text: Input text (string) to preprocess.
    :return: Preprocessed text as a string.
    """


    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    processed_tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word.isalnum() and word not in stop_words
    ]


    tokenized_text = ' '.join(processed_tokens)


    return tokenized_text


