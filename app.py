import streamlit as st
import google.generativeai as genai

# Configuração da Página
st.set_page_config(page_title="Shopee Mastermind", page_icon="🚀")

st.title("🚀 Shopee Mastermind AI")

# Configuração da API
try:
    # IMPORTANTE: Use exatamente GEMINI_API_KEY nos Secrets
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Erro de Chave: {e}")

produto = st.text_input("Produto Minerado:", placeholder="Ex: Garrafa Térmica")

if st.button("GERAR ROTEIRO DE ELITE"):
    if produto:
        with st.spinner('Gerando...'):
            try:
                # Usando o método padrão que evita o erro v1beta
                response = model.generate_content(f"Roteiro de 30s para Shopee: {produto}")
                st.success("Gerado com sucesso!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Erro na IA: {e}")
