import streamlit as st
st.write('Hello world')

st.title("Relatório Gerencial Demandas TCU")
st.header("Exercício 2024")
st.subheader("Atendimento a diligências e acórdãos")
st.markdown("Neste relatório serão apresentados graficamente a quantidade de demandas recebidas pelo MPO em 2024, assim como as providências tomadas em relação a elas, agregadas por tema e secretaria responsável")
st.caption("O quantitativo de diligências será mensurado pelo número de ofícios e o de acórdãos será pelo número de itens atendidos")
st.code("x=2024")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

resposta_num = st.slider('Selecione o seu grau de satisfação', 0,100)
resposta_dig = st.number_input('Selecione o seu grau de satisfação', 0,100)
st.write(resposta_num)
st.write(resposta_dig)
