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
    fig1 = px.bar(quantidades, text_auto=True, orientation='h')
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



