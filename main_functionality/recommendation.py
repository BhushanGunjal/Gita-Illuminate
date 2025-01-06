import numpy as np
from .similarity import cosine_similarity_single, jaccard_similarity
from embeddings.input_preprocess import preprocess_user_input

def generate_recommendations(user_input, data, embeddings_matrix, embedding_model):
    """
    Generate recommendations based on user input.
    :param user_input: Raw user input.
    :param data: Dataset as a pandas DataFrame.
    :param embeddings_matrix: Matrix of dataset embeddings.
    :param embedding_model: Pretrained SentenceTransformer model.
    :return: Top recommendations as a DataFrame.
    """
    # Preprocess user input and compute its embedding
    input_processed = preprocess_user_input(user_input)
    input_embedding = embedding_model.encode(input_processed)
    
    # Calculate cosine similarity
    cosine_scores = cosine_similarity_single(input_embedding, embeddings_matrix)
    
    # Calculate Jaccard similarity based on 'Themes' and 'Tags'
    user_input_tokens = set(input_processed.split())
    data['Jaccard'] = data['Themes'].fillna('').apply(
        lambda x: jaccard_similarity(user_input_tokens, set(x.split()))
    )
    
    # Combine scores with a weighted average (you can adjust weights as needed)
    data['Similarity'] = 0.8 * cosine_scores + 0.2 * data['Jaccard']
    
    # Sort and get top recommendations
    recommendations = data.sort_values(by='Similarity', ascending=False).head(1)
    return recommendations[['Title', 'Verse', 'Sanskrit Anuvad', 'English Translation', 'Suggested Solution']]
