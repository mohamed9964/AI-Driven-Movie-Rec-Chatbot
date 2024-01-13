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
