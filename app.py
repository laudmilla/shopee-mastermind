import streamlit as st
import google.generativeai as genai

st.title("🚀 Shopee Mastermind AI")

# Configuração robusta
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # Usando o nome completo do modelo para evitar o erro 404
    model = genai.GenerativeModel('models/gemini-1.5-flash')
else:
    st.error("Configure sua chave GEMINI_API_KEY nos Secrets!")
    st.stop()

produto = st.text_input("Produto:", placeholder="Ex: Garrafa Térmica")

if st.button("GERAR"):
    if produto:
        with st.spinner('Aguarde...'):
            try:
                # Gerando o conteúdo
                response = model.generate_content(f"Crie um roteiro de vendas para: {produto}")
                st.write(response.text)
            except Exception as e:
                st.error(f"Erro na IA: {e}")
