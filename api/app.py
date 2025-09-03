import streamlit as st
import pickle
import pandas as pd
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def fetch_poster(movie_id):
    
    api_key = os.getenv('TMDB_API_KEY')
    if not api_key:
        st.error("API key not found. Please check your .env file")
        return None
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US', timeout=10)
    data = response.json()
    print(data)
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return None
    
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies = []
    
    recommended_movie_posters = []
    
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
        
    return recommended_movies,recommended_movie_posters


movies_dict = pickle.load(open('models/movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('models/similarity.pkl','rb'))


st.title('Movie Recommender System')

selected_movie = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]
    for i in range(5):
        with columns[i]:
            st.text(recommended_movie_names[i])
            if recommended_movie_posters[i] is not None:
                st.image(recommended_movie_posters[i])
            else:
                st.write("No poster available")


        