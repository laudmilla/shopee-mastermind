import streamlit as st
import google.generativeai as genai

st.title("🚀 Shopee Mastermind AI")

# Configuração simples
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Chave API não configurada nos Secrets!")
    st.stop()

produto = st.text_input("Qual o produto?")

if st.button("GERAR ROTEIRO"):
    if produto:
        with st.spinner('Gerando...'):
            try:
                response = model.generate_content(f"Crie um roteiro para: {produto}")
                st.write(response.text)
            except Exception as e:
                st.error(f"Erro: {e}")
