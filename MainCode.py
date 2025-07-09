import streamlit as st
import numpy as np

col1, col2 = st.columns(2)

with col1:
    st.image("ufpe.png", width=200)

with col2:
    st.image("caa.jpg", width=200)

st.title("Espaços Vetoriais: Dependência Linear e Mudança de Base")

# Rodapé com seu nome
st.markdown("<p style='text-align: center; font-size: 18px;'>Desenvolvido por: Victor H. R. Lima</p>", unsafe_allow_html=True)

aba = st.sidebar.radio("Escolha o módulo", ["Teste de Dependência Linear", "Mudança de Base"])

# =========================
# Aba 1: Dependência Linear
# =========================
if aba == "Teste de Dependência Linear":
    st.header("Teste de Dependência Linear")
    st.write("Digite os vetores como listas separadas por vírgulas.")

    num_vetores = st.number_input("Número de vetores", min_value=2, max_value=5, step=1, value=3)
    tamanho = st.number_input("Dimensão dos vetores", min_value=2, max_value=5, step=1, value=3)

    vetores = []
    for i in range(num_vetores):
        vetor = st.text_input(f"Vetor {i + 1}", "1,2,3")
        vetor = np.array([float(x) for x in vetor.split(",")])
        if len(vetor) != tamanho:
            st.error(f"O vetor {i+1} deve ter exatamente {tamanho} componentes.")
        else:
            vetores.append(vetor)
    
    if len(vetores) == num_vetores:
        matriz = np.column_stack(vetores)
        rank = np.linalg.matrix_rank(matriz)
        
        st.subheader("Resultado:")
        st.write("Matriz formada pelos vetores como colunas:")
        st.write(matriz)
        st.write(f"Posto da matriz (rank): {rank}")
        
        if rank < num_vetores:
            st.error("Os vetores são linearmente dependentes.")
        else:
            st.success("Os vetores são linearmente independentes.")

# =====================
# Aba 2: Mudança de Base
# =====================
elif aba == "Mudança de Base":
    st.header("Mudança de Base")
    st.write("Informe as duas bases (cada vetor separado por vírgulas).")

    tamanho = st.number_input("Dimensão dos vetores", min_value=2, max_value=5, step=1, value=2)

    st.subheader("Base Original (B1)")
    base1 = []
    for i in range(tamanho):
        vetor = st.text_input(f"Vetor {i+1} da Base B1", "1,0" if i == 0 else "0,1")
        vetor = np.array([float(x) for x in vetor.split(",")])
        if len(vetor) != tamanho:
            st.error(f"O vetor deve ter {tamanho} componentes.")
        else:
            base1.append(vetor)
    
    st.subheader("Nova Base (B2)")
    base2 = []
    for i in range(tamanho):
        vetor = st.text_input(f"Vetor {i+1} da Base B2", "1,0" if i == 0 else "0,1", key=f"b2_{i}")
        vetor = np.array([float(x) for x in vetor.split(",")])
        if len(vetor) != tamanho:
            st.error(f"O vetor deve ter {tamanho} componentes.")
        else:
            base2.append(vetor)
    
    if len(base1) == tamanho and len(base2) == tamanho:
        matriz_B1 = np.column_stack(base1)
        matriz_B2 = np.column_stack(base2)
        
        try:
            matriz_mudanca = np.linalg.inv(matriz_B2) @ matriz_B1
            st.subheader("Matriz de mudança de base (de B1 para B2):")
            st.write(matriz_mudanca)
        except np.linalg.LinAlgError:
            st.error("A matriz da nova base não é invertível. Bases inválidas.")

