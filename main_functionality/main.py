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
    print("Loading embedding model...")
    processed_data = preprocess_dataset(raw_data)


    # Save processed dataset
    save_processed_data(processed_data,PROCESSED_DATA_PATH)  # Save as a pickle for embeddings compatibility
    print("Dataset preparation complete.")



if __name__ == "__main__":
    main()
