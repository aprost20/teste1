import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title = "Demandas TCU 2024", layout = "wide")
st.title("Demandas TCU recebidas pelo MPO em 2024")

urldemandas = "https://github.com/aprost20/teste1/blob/main/Demandas2024.xlsx"
resposta = req.get(urldemandas)
dadosJSON = resposta.json()
