import streamlit as st
import google.generativeai as genai

# Configuração da Página
st.set_page_config(page_title="Mestre da Shopee", page_icon="🚀")

st.markdown("""
    <style>
    .stButton>button { background-color: #EE4D2D; color: white; border-radius: 10px; width: 100%; }
    .main { background-color: #f5f5f5; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Shopee Mastermind AI")

# USANDO O SECRETS PARA SEGURANÇA
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Erro na Chave: Configure o Secrets no Streamlit.")

produto = st.text_input("Produto Minerado:", placeholder="Ex: Garrafa Térmica")

if st.button("GERAR ROTEIRO DE ELITE"):
    if produto:
        with st.spinner('Aplicando Neuromarketing...'):
            try:
                prompt = f"Especialista Shopee. Produto: {produto}. Gere narração de 30s e legenda de até 150 caracteres."
                response = model.generate_content(prompt)
                st.success("Material Gerado!")
                st.text_area("Resultado:", response.text, height=300)
            except Exception as e:
                st.error(f"Erro na IA: {e}")
