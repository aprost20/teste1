import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title = "Demandas TCU 2024", layout = "wide")
df = pd.read_excel('/content/Demandas2024.xlsx', sheet_name = 0)
st.title("Demandas TCU recebidas pelo MPO em 2024")
