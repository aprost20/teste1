import pandas as pd
import streamlit as st
import io
import requests as rq

# Título do dashboard
st.title('Demandas TCU recebidas pelo MPO em 2024')

df = pd.read_excel('https://github.com/aprost20/teste1/blob/main/Demandas2024.xlsx')
st.write(df)






 

   
