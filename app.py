import streamlit as st

# 1. Configuração da página e Título principal com ícone amigável
st.set_page_config(
    page_title="Calculadora Vibe Coding",
    page_icon="🎈",
    layout="centered"
)

st.title("🎈 Calculadora Interativa - Vibe Coding")
st.markdown("Insira os valores abaixo, escolha a operação e clique em calcular para ver a mágica acontecer!")

# Criando um layout em colunas para organizar melhor a interface
col1, col2 = st.columns(2)

with col1:
    # 2. Primeiro campo de entrada numérica
    num1 = st.number_input("Digite o primeiro número:", value=0.0, format="%.2f")

with col2:
    # Segundo campo de entrada numérica
    num2 = st.number_input("Digite o segundo número:", value=0.0, format="%.2f")

# 3. Componente de seleção para escolher a operação
operacao = st.selectbox(
    "Escolha a operação desejada:",
    ("Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)")
)

st.markdown("---")

# 4. Botão de ação "Calcular"
if st.button("Calcular", type="primary", use_container_width=True):
    # Lógica de cálculo com base na operação escolhida
    resultado = None
    erro = None

    if operacao == "Soma (+)":
        resultado = num1 + num2
    elif operacao == "Subtração (-)":
        resultado = num1 - num2
    elif operacao == "Multiplicação (*)":
        resultado = num1 * num2
    elif operacao == "Divisão (/)":
        # 5. Tratamento de divisão por zero
        if num2 == 0:
            erro = "⚠️ Erro: Não é possível realizar divisão por zero!"
        else:
            resultado = num1 / num2

    # 5. Exibição de erros ou resultados
    if erro:
        st.error(erro)
    elif resultado is not None:
        # Mostrando o resultado em grande destaque usando st.metric
        st.metric(label="Resultado da Operação", value=f"{resultado:.2f}")
        st.success("Cálculo realizado com sucesso! ✨")
        
        # Comando para disparar os balões na tela com sucesso
        st.balloons()

# Rodapé simples com estilo amigável
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Criado com 💜, balões e Python utilizando Streamlit</div>", 
    unsafe_allow_html=True
)

