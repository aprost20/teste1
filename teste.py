import pandas as pd
import streamlit as st
import io
import requests

st.title('Demandas TCU recebidas pelo MPO em 2024')

url = 'https://raw.githubusercontent.com/aprost20/teste1/main/Demandas2024.xlsx'
response = requests.get(url)
response.raise_for_status() 

df = pd.read_excel(io.BytesIO(response.content), engine='openpyxl') 

st.write("Demandas TCU 2024")
