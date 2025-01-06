

```markdown
# GitaIlluminate - AI-Powered Recommendation System

**GitaIlluminate** is an AI-powered application that generates personalized recommendations from the Bhagavad Gita and Hindu mythology based on a user's life situation or query. Powered by **FastAPI** for the backend and **Streamlit** for the frontend, this application is designed to help individuals find answers or guidance from the sacred texts.

## Features
- **Personalized Recommendations:** Users can input their life situations or queries, and the system provides relevant recommendations from the Bhagavad Gita.
- **AI-Powered Insights:** Uses advanced NLP and Sentence Transformers for embedding-based recommendations.
- **Beautiful UI:** The frontend is designed using Streamlit, presenting the responses in a clear and readable format.
- **Jaccard & Cosine Similarity:** Both methods are used to evaluate similarity between user input and text in the dataset.

## Technology Stack
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **NLP:** SentenceTransformers (Embedding Model)
- **Similarity Measures:** Cosine Similarity, Jaccard Similarity
- **Data Storage:** Pickle (for storing processed embeddings)
- **Dependencies:** Pandas, scikit-learn, SentenceTransformers, requests, etc.

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/GitaIlluminate.git
cd GitaIlluminate
```

### 2. Install Dependencies
Create a virtual environment and install the required Python packages.

```bash
pip install -r requirements.txt
```

### 3. Run the Backend (FastAPI)

The backend server (FastAPI) is responsible for generating recommendations. Start the server by running the following command:

```bash
python api/api.py
```

This will start the FastAPI server on `http://127.0.0.1:8000`.

### 4. Run the Frontend (Streamlit)
To start the Streamlit frontend, run the following:

```bash
streamlit run streamlit_app.py
```

The application will start running locally, and you can access it at `http://localhost:8501` in your browser.

## Usage

1. **User Input:** 
   Once you open the Streamlit UI in your browser, you'll see a text area where you can input a description of your life situation or query. For example, you can write:
   - "I am struggling with work-life balance. What can I do to manage stress better?"

2. **Recommendations:**
   Once you input your situation, click the "Get Recommendations" button. The application will contact the FastAPI backend to generate recommendations, including related verses, meanings, and suggested solutions from the Bhagavad Gita.

3. **Viewing Results:**
   After processing, the system will display:
   - **Shloka in Sanskrit**
   - **Shloka in English Translation**
   - **Suggested Solution**

## Sample Input
Here's an example life situation you can input:

**Input:**  
"I feel overwhelmed by my professional responsibilities and am unsure how to manage them effectively. How can I bring balance and peace in my life?"

## Contributing

Feel free to fork the project and contribute by submitting pull requests for improvements or bug fixes.

### Steps to Contribute:
1. Fork this repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **Hindu Philosophy & Bhagavad Gita** for the inspirational texts
- **Streamlit, FastAPI** for making this project easier to deploy and scale
- **SentenceTransformers** for the embedding generation

---

**Note:** Please ensure you have the required dataset and processed data (Embeddings) for the application to function properly. You can generate the embeddings from the dataset using the provided `main.py`.

```
