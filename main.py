import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

movies_data = pd.read_csv('data/movies.csv')
m =  movies_data.shape[0]
st.write("shape: ", m, movies_data.shape[1])
st.write(movies_data.head())
print(movies_data.duplicated())
st.write(movies_data.count())
st.write(movies_data.columns)