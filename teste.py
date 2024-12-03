import pandas as pd
import streamlit as st
import io
import requests as rq

st.title('Demandas TCU recebidas pelo MPO em 2024')

# Get the raw file content from GitHub using the 'raw' subdomain
url = 'https://raw.githubusercontent.com/aprost20/teste1/main/Demandas2024.xlsx'
response = requests.get(url)
response.raise_for_status()  # Raise an exception for bad responses

# Read the Excel file from the response content using io.BytesIO
df = pd.read_excel(io.BytesIO(response.content), engine='openpyxl') 

st.write("Demandas TCU 2024")
