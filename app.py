import streamlit as st
import google.generativeai as genai

st.title("🚀 Shopee Mastermind AI")

# 1. Configuração de Conexão
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    # FORÇAR VERSÃO V1 PARA EVITAR O ERRO 404 V1BETA
    genai.configure(api_key=api_key, transport='rest') 
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Configure sua GEMINI_API_KEY nos Secrets!")
    st.stop()

# 2. Interface
produto = st.text_input("Qual o produto?")

if st.button("GERAR ROTEIRO"):
    if produto:
        with st.spinner('Gerando...'):
            try:
                # Chamada direta e simples
                response = model.generate_content(f"Roteiro de vendas Shopee: {produto}")
                st.write(response.text)
            except Exception as e:
                st.error(f"Erro: {e}")
