import streamlit as st
import pandas as pd

st.set_page_config(page_title="Minhas finanças", layout="wide")
st.title("Meu controle financeiro")
st.write("Registros dos gastos pessoais")

if "registros" not in st.session_state:
    st.session_state.registros = []

valor = st.text_input("Valor do gasto",value="R$")

tipo_gasto=st.selectbox(
    "Tipo de gasto",
    ["Gasto fixo", "Gasto variável", "alimentação", "transporte", "investimento"]

)

if st.button("Registrar valor"):
    st.session_state.registros.append({
        "Valor": valor,
        "Tipo": tipo_gasto

        })



st.subheader("Valores registrados")

if st.session_state.registros:
    tabela = pd.DataFrame(st.session_state.registros)
    st.table(tabela)

else:
    st.info("Nenhum valor registrado ainda.")
