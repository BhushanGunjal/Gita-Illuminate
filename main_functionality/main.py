import pandas as pd
from sentence_transformers import SentenceTransformer
from embeddings.generate_embeddings import preprocess_dataset
from utils.io import load_raw_data, save_processed_data

DATA_PATH = "data/main.xlsx"
PROCESSED_DATA_PATH = "data/processed_data.pkl"
OUTPUT_FILE = "data/processed_data.pkl"
MODEL_NAME = "all-MiniLM-L6-v2"

def main():
    """
    Entry point to prepare dataset embeddings, preprocess data, 
    and save for recommendation use.
    """
    print("Loading raw data...")
    raw_data = load_raw_data(DATA_PATH)
    print(f"Loaded {len(raw_data)} rows of data.")
    
    print("Preprocessing dataset...")
    processed_data = preprocess_dataset(raw_data, PROCESSED_DATA_PATH)

    print("Loading embedding model...")
    embedding_model = SentenceTransformer(MODEL_NAME)
    
    # print("Generating embeddings for the dataset...")
    # processed_data['Embeddings'] = processed_data['Preprocessed_Text'].apply(
    #     lambda text: embedding_model.encode(text)
    # )

    # print("Saving processed data...")
    # save_processed_data(processed_data, PROCESSED_DATA_PATH)

    print("Dataset preparation complete.")

if __name__ == "__main__":
    main()
