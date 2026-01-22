import streamlit as st
import google.generativeai as genai

# Título
st.title("🚀 Shopee Mastermind AI")

# 1. Verificação da Chave
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
else:
    st.error("Configure o Secret: GEMINI_API_KEY")
    st.stop()

# 2. Inicialização do Modelo (Método Atualizado 2026)
try:
    # Testamos o modelo flash que é o padrão atual
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Erro ao carregar modelo: {e}")

# 3. Interface
produto = st.text_input("Produto:", placeholder="Ex: Garrafa Térmica")

if st.button("GERAR ROTEIRO"):
    if produto:
        with st.spinner('Gerando...'):
            try:
                # Usamos o método mais simples de geração
                response = model.generate_content(produto)
                st.markdown("### ✨ Resultado:")
                st.write(response.text)
            except Exception as e:
                # Se o 404 aparecer aqui, o problema é Geoblocking (Região)
                st.error(f"Erro de Conexão (404): {e}")
                st.info("Dica: Se o erro persistir, o servidor do Streamlit pode estar em uma região bloqueada.")
    else:
        st.warning("Preencha o campo produto.")
