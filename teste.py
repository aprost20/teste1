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
  fig1 = px.bar(quantidades, text_auto = True, orientation = 'h')
  fig1.update_layout(title = 'Demandas TCU x Situação', xaxis_title = "Quantidade de itens demandados", yaxis_title = "Situação")
  st.plotly_chart(fig1, use_container_width = True)





 

   
