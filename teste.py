import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title = "Demandas TCU 2024", layout = "wide")
st.title("Demandas TCU recebidas pelo MPO em 2024")

df = pd.read_excel('https://github.com/aprost20/teste1/blob/main/Demandas2024.xlsx', sheet_name = 0)
