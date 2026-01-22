import streamlit as st
import google.generativeai as genai

st.title("🚀 Shopee Mastermind AI")

# Configuração simples e direta
if "GEMINI_API_KEY" in st.secrets:
    # Apenas configura a chave, sem comandos extras de transporte ou versão
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Chamamos o modelo diretamente pelo nome simples
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Configure sua GEMINI_API_KEY nos Secrets!")
    st.stop()

produto = st.text_input("Qual o produto?")

if st.button("GERAR ROTEIRO"):
    if produto:
        with st.spinner('Gerando roteiro...'):
            try:
                # O comando mais básico de todos
                response = model.generate_content(f"Crie um roteiro para vender {produto} na Shopee")
                st.markdown("---")
                st.write(response.text)
            except Exception as e:
                # Isso vai nos mostrar o erro real se ainda houver falha
                st.error(f"Erro na geração: {e}")
    else:
        st.warning("Por favor, digite o nome de um produto.")
