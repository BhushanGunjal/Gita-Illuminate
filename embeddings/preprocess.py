import nltk
import os

# Specify the path to store NLTK data
nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')

# Ensure NLTK data directory is added to the NLTK data path list
nltk.data.path.append(nltk_data_path)

# Download the necessary resources if not found
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', download_dir=nltk_data_path)

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet', download_dir=nltk_data_path)

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', download_dir=nltk_data_path)











# import nltk

# Download necessary NLTK resources (should be downloaded once)
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('stopwords')


from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords



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


