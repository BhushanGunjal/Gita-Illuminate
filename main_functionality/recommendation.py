import numpy as np
from .similarity import cosine_similarity_single, jaccard_similarity
from embeddings.preprocess import preprocess_text

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
    input_embedding = embedding_model.encode(user_input)
    

    # Calculate cosine similarity
    cosine_scores = cosine_similarity_single(input_embedding, embeddings_matrix)
    
    
    input_processed = preprocess_text(user_input)
    # Calculate Jaccard similarity based on 'Themes' and 'Tags'
    user_input_tokens = set(input_processed.split())
    data['Jaccard'] = data['Themes'].fillna('').apply(
        lambda x: jaccard_similarity(user_input_tokens, set(x.split()))
    )
    

    # Combine scores with a weighted average (you can adjust weights as needed)
    data['Similarity'] = 0.8 * cosine_scores + 0.2 * data['Jaccard']
    

    # Sort and get top recommendations
    recommendations = data.sort_values(by='Similarity', ascending=False)

    # for index, row in recommendations.iterrows():
    #     print(f"{index}, {row['Similarity']}, {row['Jaccard']}")

    
    final_recommendations = recommendations.head(1)

    return final_recommendations[['Title', 'Verse', 'Sanskrit Anuvad', 'English Translation', 'Suggested Solution']]



