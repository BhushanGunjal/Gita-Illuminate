from sentence_transformers import SentenceTransformer

def compute_embeddings(texts, model_name='all-MiniLM-L6-v2'):
    """
    Computes embeddings for a list of text entries.
    :param texts: List of text strings.
    :param model_name: Pretrained SentenceTransformer model name.
    :return: List of embeddings.
    """
    model = SentenceTransformer(model_name)
    return [model.encode(text) for text in texts]
