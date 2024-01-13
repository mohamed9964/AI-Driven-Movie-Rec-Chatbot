from flask import Flask, request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval

app = Flask(__name__)

def access (dic):
    age = dic["age"]["amount"]
    favmovie = dic['favmovie']
    genre = dic['genre']
    
    return favmovie , genre , age

movies_df = pd.read_csv('C:/Users/Retshard/Downloads/recommend/movies_df.csv')
count_vectorizer = CountVectorizer(stop_words="english")
count_matrix = count_vectorizer.fit_transform(movies_df["soup"])
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
movies_df = movies_df.reset_index()
indices = pd.Series(movies_df.index, index=movies_df['original_title']).drop_duplicates()

def capitalize_first_letter(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    result = " ".join(capitalized_words)
    return result

def get_recommendations(title, cosine_sim=cosine_sim2):
    title = capitalize_first_letter(title)
    idx = indices[title]
    similarity_scores = list(enumerate(cosine_sim[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:11]

    movies_indices = [ind[0] for ind in similarity_scores]
    movies = movies_df["original_title"].iloc[movies_indices]

    recommendations = "\n".join(f"{i+1}. {movie}" for i, movie in enumerate(movies))

    return recommendations

@app.route('/webhook', methods=["POST", "GET"])
def webhook():
    req = request.get_json(force=True)
    

    myParam=req["queryResult"]["parameters"]
    print( access(myParam) )
    var1  = access(myParam)
 
    return {
        'fulfillmentText': f'{get_recommendations(var1[0], cosine_sim=cosine_sim2)}'
    }

if __name__ == '__main__':
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()



