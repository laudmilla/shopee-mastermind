import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="Shopee Mastermind", page_icon="🚀")
st.title("🚀 Shopee Mastermind AI")

# 1. Configuração de Conexão Estável
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
else:
    st.error("ERRO: Configure a GEMINI_API_KEY nos Secrets do Streamlit.")
    st.stop()

# 2. Inicialização do Modelo (Caminho absoluto para evitar 404)
try:
    # Forçamos o modelo sem o prefixo 'models/' se o anterior falhou
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Erro ao carregar modelo: {e}")

# 3. Interface de Usuário
produto = st.text_input("Produto:", placeholder="Ex: Garrafa Térmica")

if st.button("GERAR ROTEIRO"):
    if produto:
        with st.spinner('A IA está pensando...'):
            try:
                # O segredo aqui é não passar configurações extras que o v1beta pedia
                response = model.generate_content(f"Gere um roteiro de vendas para Shopee do produto: {produto}")
                st.success("Concluído!")
                st.write(response.text)
            except Exception as e:
                # Se der erro 404, vamos mostrar o erro detalhado para diagnóstico
                st.error(f"Erro na API (404): O modelo não foi encontrado. Detalhes: {e}")
    else:
        st.warning("Digite o nome do produto.")
