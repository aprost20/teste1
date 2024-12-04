import pandas as pd
import streamlit as st

st.set_page_config(page_title="Demandas TCU 2024", layout="wide")

# Carregar arquivo via file_uploader
uploaded_file = st.file_uploader("Carregue o arquivo Demandas2024.xlsx", type="xlsx")

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file, sheet_name=0)
        st.write("Arquivo carregado com sucesso!")
        st.write(df.head())  # Mostrar as primeiras linhas para verificar o conteúdo
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
else:
    st.warning("Por favor, carregue um arquivo para visualizar os dados.")

   
