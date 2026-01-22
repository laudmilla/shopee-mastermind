import streamlit as st
import google.generativeai as genai

# Título da aplicação
st.title("🚀 Shopee Mastermind AI")

# Verificação e configuração da API
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # Usar 'models/gemini-1.5-flash' garante que a API localize o modelo corretamente
    model = genai.GenerativeModel('models/gemini-1.5-flash')
else:
    st.error("ERRO: A chave 'GEMINI_API_KEY' não foi encontrada nos Secrets do Streamlit.")
    st.stop()

# Entrada do usuário
produto = st.text_input("Qual produto você minerou?", placeholder="Ex: Mini Processador")

if st.button("GERAR ESTRATÉGIA DE VENDA"):
    if produto:
        with st.spinner('A IA está analisando o produto e criando o roteiro...'):
            try:
                # Prompt direto para conversão em vendas
                prompt = (
                    f"Atue como um especialista em vendas na Shopee. "
                    f"Crie um roteiro de vídeo de 30 segundos focado em benefícios para o produto: {produto}. "
                    f"Ao final, inclua uma legenda curta de até 150 caracteres com hashtags."
                )
                
                response = model.generate_content(prompt)
                
                # Exibição do resultado
                st.success("Roteiro pronto para uso!")
                st.markdown("---")
                st.markdown(response.text)
                
            except Exception as e:
                # Caso ocorra um erro, ele será detalhado aqui
                st.error(f"Ocorreu um erro técnico: {e}")
    else:
        st.warning("Por favor, digite o nome de um produto.")
