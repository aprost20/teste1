import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Demandas TCU 2024", layout="wide")

# Carregamento do arquivo Excel
df = pd.read_excel('Demandas2024.xlsx', sheet_name=0)

st.title("Demandas TCU recebidas pelo MPO em 2024")

streamlit run teste.py

