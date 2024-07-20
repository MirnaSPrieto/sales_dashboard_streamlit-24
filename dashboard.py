import streamlit as st
import pandas as pd

st.title('Dashboard de Ventas :shopping_trolley:') 

#Enlacenlace publico a B Ventas: https://github.com/MirnaSPrieto/sales_dashboard_streamlit-24/blob/main/base_ventas.csv
df_ventas = pd.read_csv('base_ventas.csv')
# Mostrar los datos en un dataframe de Streamlit
st.dataframe(df_ventas)