import streamlit as st
import google.generativeai as genai

st.title("🚀 Shopee Mastermind AI")

# Configuração de conexão estável
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # A linha abaixo é o segredo: usar 'models/' evita o erro 404 v1beta
    model = genai.GenerativeModel('models/gemini-1.5-flash')
else:
    st.error("Chave API não encontrada nos Secrets!")
    st.stop()

produto = st.text_input("Qual o produto?", placeholder="Ex: Garrafa Térmica")

if st.button("GERAR ROTEIRO"):
    if produto:
        with st.spinner('Conectando ao cérebro da IA...'):
            try:
                # Prompt otimizado
                response = model.generate_content(f"Crie um roteiro de vendas para Shopee do produto: {produto}")
                st.markdown("---")
                st.write(response.text)
            except Exception as e:
                # Se o erro v1beta aparecer, este bloco vai nos avisar
                st.error(f"Erro de Conexão: {e}")
