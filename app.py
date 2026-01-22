import streamlit as st
import google.generativeai as genai

st.title("🚀 Shopee Mastermind AI")

# Configuração de segurança
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # Adicionamos 'models/' para garantir que a API encontre o modelo
    model = genai.GenerativeModel('models/gemini-1.5-flash')
else:
    st.error("Chave API não configurada nos Secrets!")
    st.stop()

produto = st.text_input("Qual o produto?", placeholder="Ex: Mini Processador")

if st.button("GERAR ROTEIRO"):
    if produto:
        with st.spinner('Criando estratégia de vendas...'):
            try:
                prompt = f"Crie um roteiro de vídeo curto e persuasivo para vender {produto} na Shopee."
                response = model.generate_content(prompt)
                st.markdown("### 📝 Roteiro Sugerido:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Erro na conexão com a IA: {e}")
