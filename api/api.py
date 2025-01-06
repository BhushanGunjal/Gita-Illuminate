from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sentence_transformers import SentenceTransformer
from main_functionality.recommendation import generate_recommendations
import numpy as np

# Initialize FastAPI
app = FastAPI()

# Load preprocessed data
DATA_PATH = "data/processed_data.pkl"
MODEL_NAME = "all-MiniLM-L6-v2"

data = pd.read_pickle(DATA_PATH)
embeddings_matrix = np.array(data['Embeddings'].tolist())
embedding_model = SentenceTransformer(MODEL_NAME)

class RecommendationRequest(BaseModel):
    input_text: str

@app.post("/recommendations/")
def get_recommendations(request: RecommendationRequest):
    """
    Endpoint to generate recommendations based on user input.
    """
    recommendations = generate_recommendations(
        request.input_text, data, embeddings_matrix, embedding_model
    )
    return recommendations.to_dict(orient="records")
