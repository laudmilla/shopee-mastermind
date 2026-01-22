import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(page_title="Shopee Mastermind", page_icon="🚀")

# Estilo laranja Shopee
st.markdown("""
    <style>
    .stButton>button { background-color: #EE4D2D; color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Shopee Mastermind AI")

# Configuração da IA usando o segredo salvo
try:
    # Esta linha lê a chave do seu Secrets do Streamlit
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # Definindo o modelo estável
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Erro na chave: {e}")

produto = st.text_input("Produto Minerado:", placeholder="Ex: Garrafa Térmica")

if st.button("GERAR ROTEIRO DE ELITE"):
    if produto:
        with st.spinner('Criando estratégia de vendas...'):
            try:
                prompt = f"Atue como especialista em Shopee. Produto: {produto}. Gere um roteiro de 30s e uma legenda de até 150 caracteres."
                response = model.generate_content(prompt)
                st.success("Pronto!")
                st.write(response.text)
            except Exception as e:
                # Se der erro 404 aqui, é sinal de que a biblioteca está desatualizada
                st.error(f"Erro na IA: {e}")
    else:
        st.warning("Digite o nome de um produto.")
