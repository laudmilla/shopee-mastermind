import streamlit as st
import google.generativeai as genai

# Configuração da Página
st.set_page_config(page_title="Shopee Mastermind", page_icon="🚀")

# Estilo
st.markdown("""
    <style>
    .stButton>button { background-color: #EE4D2D; color: white; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Shopee Mastermind AI")

# Configuração da API
try:
    # Pega a chave dos Secrets
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Modelo Correto
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Erro de Configuração: Verifique a Chave API nos Secrets.")

# Interface
produto = st.text_input("Produto Minerado:", placeholder="Ex: Garrafa Térmica")

if st.button("GERAR ROTEIRO DE ELITE"):
    if produto:
        with st.spinner('Analisando mercado e criando copy...'):
            try:
                # Prompt Otimizado
                prompt = f"Crie um roteiro de vídeo de 30s para vender {produto} na Shopee. Foco em dor e desejo. Inclua legenda curta com hashtags."
                
                response = model.generate_content(prompt)
                
                st.success("Estratégia Gerada!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Erro Técnico: {e}")
    else:
        st.warning("Digite o nome do produto.")
