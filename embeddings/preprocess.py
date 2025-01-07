import nltk

# Download necessary NLTK resources (should be downloaded once)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


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


