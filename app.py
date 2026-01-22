import streamlit as st
import google.generativeai as genai

st.title("🚀 Shopee Mastermind AI")

# Configuração de Conexão Estável
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    # ESTA LINHA É A CHAVE: Força o uso da API v1 estável
    genai.configure(api_key=api_key, transport='rest') 
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Configure sua GEMINI_API_KEY nos Secrets!")
    st.stop()

produto = st.text_input("Qual o produto?")

if st.button("GERAR ROTEIRO"):
    if produto:
        with st.spinner('Gerando...'):
            try:
                # Chamada direta
                response = model.generate_content(f"Roteiro Shopee para: {produto}")
                st.write(response.text)
            except Exception as e:
                # Se o erro 404 aparecer, o código vai nos dizer o motivo exato
                st.error(f"Erro: {e}")
