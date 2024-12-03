import pandas as pd
import streamlit as st
import io
import requests as rq

# Título do dashboard
st.title('Demandas TCU recebidas pelo MPO em 2024')

# URL do arquivo Excel no GitHub
url = 'https://raw.githubusercontent.com/aprost20/teste1/main/Demandas2024.xlsx'

# Carregar o arquivo do GitHub
try:
    response = rq.get(url)
    response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

    # Ler o conteúdo do Excel
    df = pd.read_excel(io.BytesIO(response.content))

   
