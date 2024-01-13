# AI-Driven Movie Recommender System

## Project Overview
This repository hosts an AI-driven chatbot designed to revolutionize the movie selection process by providing personalized recommendations. Harnessing the power of content-based filtering and cosine similarity, this system offers precise cinematic suggestions tailored to individual user preferences.

## Key Features
- **Data-Driven Insights:** Utilizes the TMDB movie dataset with 5000 entries for comprehensive analysis.
- **Personalized Recommendations:** Employs content-based filtering to suggest movies based on user preferences.
- **Cosine Similarity Algorithm:** Measures the likeness between user profiles and movie attributes for accurate predictions.
- **Chatbot Integration:** Provides real-time recommendations through a user-friendly chatbot interface.
- **Performance Evaluation:** Manual evaluation of model effectiveness based on similarity with user preferences.

## Technologies Used
- Python
- TensorFlow
- Scikit-learn
- Pandas, NumPy
- Flask for API integration
- Dialogflow for chatbot creation

## Data Preparation
- **Data Cleaning:** Standardized datasets for coherence.
- **Feature Engineering:** Extracted crucial movie attributes like genre, cast, and director.
- **Vectorization:** Transformed text attributes into numerical representations.

## Model Training
- **Algorithm Selection:** Trained with SVM, Random Forest, Decision Tree, and Logistic Regression.
- **Evaluation:** Used confusion matrices and accuracy metrics to select the best-performing model.

## Chatbot Implementation
- Designed conversation flows and intents using Dialogflow.
- Integrated the recommendation system with a Flask backend.
- Deployed using ngrok for real-time interaction.

## File Structure and Usage

### Files Submitted:
- **`recommendation_system(G12).ipynb`:** The main recommendation system script for data preprocessing and exporting the "movies_df(G12).csv" for use in recommendations.
- **`Clust_class(G12).ipynb`:** Contains the classification and clustering models.
- **`flask(G12).py`:** The Flask script that must be run 24/7 on a dedicated terminal to enable chatbot connectivity. It utilizes "ngrok" for connectivity and contains the necessary recommendation functions.
- **`movies_df.csv`:** The data preprocessed by the recommendation script and used by the Flask script for recommendations.

### Steps for Using the Chatbot:
1. Ensure you have access to Dialogflow.
2. Run ngrok and enter the command `ngrok.exe http 5000`.
3. Take the IP provided by ngrok and enter it into the fulfillment section in Dialogflow, appending `/webhook` at the end to reflect our webhook in the Flask script.
4. Run the Flask script.
5. Open Dialogflow to start using the chatbot.
