import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Demandas TCU 2024", layout="wide")

# Carregamento do arquivo Excel
df = pd.read_excel('Demandas2024_09_dez.xlsx', sheet_name=0)

st.title("Demandas TCU recebidas pelo MPO em 2024")

col1, col2 = st.columns(2)

with col1:
    quantidades_counts = df['estado_SISCOD'].value_counts().reset_index()
    quantidades_counts.columns = ['estado_SISCOD', 'quant_estado']
    fig1 = px.pie(quantidades_counts, values = 'quant_estado', names = 'estado_SISCOD', color_discrete_sequence=px.colors.qualitative.Set2)
    fig1.update_layout(title = 'Demandas TCU x Situação atual')
    st.plotly_chart(fig1, use_container_width = True)
 
with col2:
    tipo_demanda = df['tipo_processo'].value_counts()
    fig2 = px.bar(tipo_demanda, text_auto=True, color_discrete_sequence=['#2237FF'])
    fig2.update_layout(
        title='Demandas por tipo de Processo TCU',
        xaxis_title="Tipo de Processo",
        yaxis_title="Quantidade itens demandados"
    )
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
  qnt_dem_respons = df['responsavel'].value_counts()
  fig3 = px.bar(qnt_dem_respons, text_auto = True, color_discrete_sequence=['#2237FF'])
  fig3.update_layout(title = 'Demandas por unidade do MPO', xaxis_title = "Unidade demandada", yaxis_title = "Quantidade de itens")
  st.plotly_chart(fig3, use_container_width = True)

with col4:
  no_prazo_counts = df['no_prazo'].value_counts().reset_index()
  no_prazo_counts.columns = ['no_prazo', 'valor_no_prazo']
  fig4 = px.pie(no_prazo_counts, values = 'valor_no_prazo', names = 'no_prazo', color_discrete_sequence=px.colors.qualitative.Set2)
  fig4.update_layout(title = 'Atendimento às demandas quanto ao prazo')
  st.plotly_chart(fig4, use_container_width = True)


col5, col6 = st.columns(2)

with col5:
  del_acordao = df.query('Ato == "Ciência" or Ato == "Determinação" or Ato == "Recomendação" or Ato == "Alerta"')
  filtro_del = del_acordao['Ato'].value_counts()
  fig5 = px.bar(filtro_del, text_auto = True, color_discrete_sequence=['#2237FF'])
  fig5.update_layout(title = 'Deliberações de Acórdãos TCU', xaxis_title = "Quantidade de itens", yaxis_title = "Tipo de Deliberação")
  st.plotly_chart(fig5, use_container_width = True)
  
with col6:
  tratamento_det = df.query('Ato == "Determinação"')
  tratamento_det['Ato'].value_counts()
  filtro_tto_det = tratamento_det['tratamento'].value_counts()
  fig6 = px.bar(filtro_tto_det, text_auto = True, color_discrete_sequence=['#2237FF'])
  fig6.update_layout(title = 'Tratamento de Determinações', xaxis_title = "Providências", yaxis_title = "Quantidade de itens")
  st.plotly_chart(fig6, use_container_width = True)

col7, col8 = st.columns(2)

with col7:
  tratamento_rec = df.query('Ato == "Recomendação"')
  tratamento_rec['Ato'].value_counts()
  filtro_tto_rec = tratamento_rec['tratamento'].value_counts()
  fig7 = px.bar(filtro_tto_rec, text_auto = True, color_discrete_sequence=['#2237FF'])
  fig7.update_layout(title = 'Tratamento de Recomendações', xaxis_title = "Providências", yaxis_title = "Quantidade de itens")
  st.plotly_chart(fig7, use_container_width = True)




