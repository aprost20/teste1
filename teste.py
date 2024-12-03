

import pandas as pd
import streamlit as st
import io
import requests as rq

# Título do dashboard
st.title('Demandas TCU recebidas pelo MPO em 2024')

# URL do arquivo Excel no GitHub
url = 'https://raw.githubusercontent.com/aprost20/teste1/main/Demandas2024.xlsx'

# Carregar o arquivo do GitHub
try:
    response = rq.get(url)
    response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

    # Ler o conteúdo do Excel
    df = pd.read_excel(io.BytesIO(response.content))

    # Exibir uma tabela com os dados
    st.write("### Demandas TCU 2024")
    st.dataframe(df)

    # Adicionar gráficos simples (exemplo)
    if not df.empty:
        # Supondo que haja uma coluna 'Categoria' e 'Total' no dataset
        st.write("#### Gráfico por Categoria")
        if 'Categoria' in df.columns and 'Total' in df.columns:
            chart_data = df.groupby('Categoria')['Total'].sum().reset_index()
            st.bar_chart(chart_data.set_index('Categoria'))
        else:
            st.warning("As colunas 'Categoria' e 'Total' não foram encontradas no arquivo.")
except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
