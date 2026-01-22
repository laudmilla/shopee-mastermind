import streamlit as st
import google.generativeai as genai
from google.generativeai.types import RequestOptions

st.title("🚀 Shopee Mastermind AI")

# Configuração da Chave
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    # Forçamos a biblioteca a usar a API v1 estável e ignorar o v1beta
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Configure sua GEMINI_API_KEY nos Secrets!")
    st.stop()

produto = st.text_input("Qual o produto?")

if st.button("GERAR ROTEIRO"):
    if produto:
        with st.spinner('Conectando ao servidor oficial...'):
            try:
                # O segredo: RequestOptions força a versão 'v1' na chamada
                response = model.generate_content(
                    f"Roteiro de vendas: {produto}",
                    request_options=RequestOptions(api_version='v1')
                )
                st.markdown("---")
                st.write(response.text)
            except Exception as e:
                st.error(f"Erro de Conexão: {e}")
