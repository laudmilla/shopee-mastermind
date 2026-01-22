import streamlit as st
import google.generativeai as genai

st.title("🚀 Shopee Mastermind AI")

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Erro de Chave: {e}")

produto = st.text_input("Produto:")

if st.button("GERAR"):
    if produto:
        response = model.generate_content(f"Script Shopee: {produto}")
        st.write(response.text)
