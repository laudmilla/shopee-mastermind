import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Shopee Mastermind", page_icon="🚀")
st.title("🚀 Shopee Mastermind AI")

# Configuração da API via Secrets
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Erro: Configure a GEMINI_API_KEY nos Secrets do Streamlit.")
    st.stop()

produto = st.text_input("Produto Minerado:", placeholder="Ex: Garrafa Térmica")

if st.button("GERAR ROTEIRO DE ELITE"):
    if produto:
        with st.spinner('Gerando roteiro...'):
            try:
                # O comando correto em inglês é 'generate_content'
                response = model.generate_content(f"Roteiro de 30s para Shopee: {produto}")
                st.success("Roteiro gerado!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Erro na IA: {e}")
