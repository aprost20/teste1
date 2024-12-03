import pandas as pd
import streamlit as st
import io
import requests as rq

# Título do dashboard
st.title('Demandas TCU recebidas pelo MPO em 2024')

def get_data_from_excel():
 df = pd.read_excel( io = '/content/Demandas2024.xlsx', engine = 'openpyxl', sheet_name = 'None', usecols = 'A:Z', nrows = 262)

fig1, fig2 = st.columns(2)

with fig1:
  quantidades = df['estado_SISCOD'].value_counts()
  st.bar_chart(quantidades, x = ""Quantidade de itens demandados")
  




 

   
