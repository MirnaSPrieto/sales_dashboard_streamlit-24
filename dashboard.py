pip install streamlit 
import streamlit as st
import pandas as pd

st.title('Dashboard de Ventas :shopping_trolley:') 

df_ventas = pd.read_cvs ('base_ventas.csv')

st.dataframe(df_ventas)