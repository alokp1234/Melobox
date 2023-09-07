import streamlit as st
import pickle
import pandas as pd


st.title('Song Recommender')


def recommend(song):
    index = songs[songs['title'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_song_names = []

    for i in distances[1:11]:

        recommended_song_names.append(songs.iloc[i[0]].title)

    return recommended_song_names


song_dict = pickle.load(open('song_dict (2).pkl', 'rb'))
songs = pd.DataFrame(song_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

song_list = songs['title'].values
selected_movie = st.selectbox(
    "Type or select a song from the dropdown",
    song_list
)

if st.button('Show Recommendation'):
    recommended_song_names = recommend(selected_movie)
    for i in recommended_song_names:
        st.write(i)