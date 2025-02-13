import numpy as np
from sklearn.metrics.pairwise import cosine_similarity



def cosine_similarity_single(input_embedding, dataset_embeddings):
    """
    Compute cosine similarity between an input embedding and dataset embeddings.
    :param input_embedding: Embedding of user input.
    :param dataset_embeddings: Matrix of dataset embeddings.
    :return: Array of similarity scores.
    """


    cos_sim = cosine_similarity([input_embedding], dataset_embeddings)[0]


    return cos_sim








def jaccard_similarity(set1, set2):
    """
    Compute Jaccard similarity between two sets of words.
    :param set1: Set of words from the input.
    :param set2: Set of words from a dataset entry.
    :return: Jaccard similarity score.
    """


    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    jac_sim =  intersection / union if union != 0 else 0

    # print('set1 ip:', set1)
    # print('set2 emb:', set2)
    return jac_sim
