from .preprocess import preprocess_text

def preprocess_user_input(input_text):
    """
    Preprocesses a single user input string.
    :param input_text: Raw user input string.
    :return: Preprocessed text.
    """
    return preprocess_text(input_text)
