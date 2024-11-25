import streamlit as st
import pandas as pd
df = pd.DataFrame({'nomeServidor': ['ana', 'aline', 'adriana'], 'idade': [40, 41, 43]})

st.write('Criando uma tabela')
st.write(df)
