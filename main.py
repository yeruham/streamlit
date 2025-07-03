import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

col1, col2, col3 = st.columns(3)

movies_data = pd.read_csv('data/movies.csv')


col1.write('**data columns:**')
col1.write(movies_data.columns)
col2.write('**data dtype:**')
col2.write(movies_data.dtypes)
col3.write('**data describe:**')
col3.write(movies_data.describe())

st.write('### five lines from movies data:')
st.write(movies_data.head())

st.write('### plots:')


fig = plt.figure(figsize = (19, 10))
plt.bar(movies_data.genre, movies_data.score)
plt.title('score movies by genre')
plt.xlabel('genre')
plt.ylabel('score')
st.pyplot(fig)

st.write(movies_data.genre.value_counts())

fig = plt.figure(figsize = (19, 10))
plt.plot(movies_data.genre.value_counts().sort_values())
plt.title('num movies by genre')
st.pyplot(fig)
