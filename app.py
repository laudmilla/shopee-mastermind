import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Shopee Mastermind", page_icon="🚀")

st.markdown("""
    <style>
    .stButton>button { background-color: #EE4D2D; color: white; border-radius: 10px; width: 100%; }
    .main { background-color: #f5f5f5; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Shopee Mastermind AI")
genai.configure(api_key="AIzaSyB1evYmvvwE1mR248p3BBNgFntyJtv0EmQ")
model = genai.GenerativeModel('gemini-3-flash-preview')

produto = st.text_input("Produto Minerado:", placeholder="Ex: Garrafa Térmica")

if st.button("GERAR ROTEIRO DE ELITE"):
    if produto:
        with st.spinner('Aplicando Neuromarketing...'):
            prompt = f"Expert Shopee. Produto: {produto}. Gere narração de 30s e legenda de até 150 caracteres."
            try:
                response = model.generate_content(prompt)
                st.success("Material Gerado!")
                st.text_area("Resultado para Copiar:", response.text, height=300)
            except Exception as e:
                st.error(f"Erro na IA: {e}")
