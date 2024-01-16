"""
import requests
from requests import get
from pprint import PrettyPrinter

url="https://data.nba.net"
ALL_JSON="/prod/v1/today.json"

response = get(url=ALL_JSON).json()
print(response)

for i in range(1,10):
    print(f"om{i+2}")
    for j in range(0,4):
        print(f"*{j+3+4}")

class a():
    def __init__(self,q,w,e):
         self.q=q
         self.w=w
         self.e=e
         while(e>10):

"""
import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarty[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    for i in movie_list:
        #fetch movie id from movies from api


        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies



movies_list = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)

similarty = pickle.load(open('similarity.pkl','rb'))


st.title("Movies recomendation")


option = st.selectbox('How wouds you like to be contacted ?', movies['title'].values)

if st.button('Recommend'):
    recmendations = recommend(option)
    for i in recmendations:
        st.write(i)