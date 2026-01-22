import streamlit as st
import google.generativeai as genai

# Configuração visual
st.set_page_config(page_title="Shopee Mastermind", page_icon="🚀")

# Estilo laranja Shopee
st.markdown("<style>.stButton>button { background-color: #EE4D2D; color: white; }</style>", unsafe_allow_html=True)

st.title("🚀 Shopee Mastermind AI")

# Configuração Segura
try:
    # Busca a chave que você salvou no Secrets do Streamlit
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Usa o modelo mais estável disponível
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Erro de Configuração: {e}")

produto = st.text_input("Produto Minerado:", placeholder="Ex: garrafa termica")

if st.button("GERAR ROTEIRO DE ELITE"):
    if produto:
        with st.spinner('Gerando roteiro de vendas...'):
            try:
                prompt = f"Crie um roteiro de 30 segundos para vídeo de Shopee sobre: {produto}. Foque em benefícios e termine com uma chamada para ação."
                # O comando abaixo agora usará a versão correta da API automaticamente
                response = model.generate_content(prompt)
                st.success("Roteiro Criado!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Erro na IA: {e}")
