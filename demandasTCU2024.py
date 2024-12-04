import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Demandas TCU 2024", layout="wide")

# Carregamento do arquivo Excel
df = pd.read_excel('Demandas2024.xlsx', sheet_name=0)

st.title("Demandas TCU recebidas pelo MPO em 2024")

col1, col2 = st.columns(2)

with col1:
    quantidades = df['estado_SISCOD'].value_counts()
    fig1 = px.bar(quantidades, text_auto=True, orientation='h', color_discrete_sequence=['#FF5733', '#33FF57'])
    fig1.update_layout(
        title='Demandas TCU x Situação',
        xaxis_title="Quantidade de itens demandados",
        yaxis_title="Situação"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    tipo_demanda = df['tipo_processo'].value_counts()
    fig2 = px.bar(tipo_demanda, text_auto=True)
    fig2.update_layout(
        title='Ofícios TCU 2024',
        xaxis_title="Tipo de Processo TCU",
        yaxis_title="Quantidade Ofícios recebidos"
    )
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
  qnt_dem_respons = df['responsavel'].value_counts()
  fig3 = px.bar(qnt_dem_respons, text_auto = True)
  fig3.update_layout(title = 'Demandas por unidade do MPO', xaxis_title = "Unidade demandada", yaxis_title = "Quantidade de itens")
  st.plotly_chart(fig3, use_container_width = True)

with col4:
  del_acordao = df.query('Ato == "Ciência" or Ato == "Determinação" or Ato == "Recomendação" or Ato == "Alerta"')
  filtro_del = del_acordao['Ato'].value_counts()
  fig4 = px.bar(filtro_del, text_auto = True)
  fig4.update_layout(title = 'Deliberações de Acórdãos TCU', xaxis_title = "Quantidade de itens", yaxis_title = "Tipo de Deliberação")
  st.plotly_chart(fig4, use_container_width = True)

col5, col6 = st.columns(2)

with col5:
  tratamento_det = df.query('Ato == "Determinação"')
  tratamento_det['Ato'].value_counts()
  filtro_tto_det = tratamento_det['tratamento'].value_counts()
  fig5 = px.bar(filtro_tto_det, text_auto = True)
  fig5.update_layout(title = 'Tratamento de Determinações', xaxis_title = "Providências", yaxis_title = "Quantidade de itens")
  st.plotly_chart(fig5, use_container_width = True)

with col6:
  tratamento_rec = df.query('Ato == "Recomendação"')
  tratamento_rec['Ato'].value_counts()
  filtro_tto_rec = tratamento_rec['tratamento'].value_counts()
  fig6 = px.bar(filtro_tto_rec, text_auto = True)
  fig6.update_layout(title = 'Tratamento de Recomendações', xaxis_title = "Providências", yaxis_title = "Quantidade de itens")
  st.plotly_chart(fig6, use_container_width = True)
