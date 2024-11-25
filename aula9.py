import streamlit as st
import pandas as pd
df = pd.DataFrame({'nomeServidor': ['ana', 'aline', 'adriana'], 'idade': [40, 41, 43]})

st.write('Criando uma tabela')
st.write(df)

opcao = st.selectbox('Qual servidor vc gostaria de selecionar?', df['nomeServidor'])
st.write(opcao)
dadosfiltrados = df[df['nomeServidor'] == opcao]
st.write(dadosfiltrados)
