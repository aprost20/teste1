import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Demandas TCU 2024", layout="wide")

# Carregar arquivo via upload
uploaded_file = st.file_uploader("Carregue o arquivo Demandas2024.xlsx", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file, sheet_name=0)
    st.title("Demandas TCU recebidas pelo MPO em 2024")
    # Continue com o restante do código...
else:
    st.warning("Por favor, carregue um arquivo para visualizar os dados.")

import pandas as pd

df = pd.read_excel("Demandas2024.xlsx", sheet_name=0)
print(df.head())

   
