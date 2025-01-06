import pandas as pd
from .preprocess import preprocess_text
from .compute_embeddings import compute_embeddings

def preprocess_dataset(file_path, output_path):
    """
    Load dataset, preprocess text, and save embeddings.
    :param file_path: Path to the input Excel file.
    :param output_path: Path to save the output with embeddings.
    """
    # Load dataset
    data = file_path
    
    # Combine relevant fields into one column
    data['CombinedText'] = data.apply(
        lambda row: f"{row['Themes']} {row['Tags']} {row['Life Situation']}", axis=1
    )
    
    # Preprocess the CombinedText
    data['Processed_CombinedText'] = data['CombinedText'].fillna('').apply(preprocess_text)
    
    # Compute embeddings
    data['Processed_Embeddings'] = compute_embeddings(data['Processed_CombinedText'].tolist())
    
    # Compute embeddings
    data['Embeddings'] = compute_embeddings(data['CombinedText'].tolist())

    return data
    

if __name__ == "__main__":
    INPUT_FILE = "data/main.xlsx"
    OUTPUT_FILE = "data/processed_data.pkl"
    preprocess_dataset(INPUT_FILE, OUTPUT_FILE)
