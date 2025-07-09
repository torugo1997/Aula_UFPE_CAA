"""
Victor Hugo Resende Lima
vhugoreslim@gmail.com

Esse código necessita dos seguintes pacotes nas respectivas versões:
Pillow==9.0.1
scipy==1.7.3
streamlit==1.5.0
click==8
"""
import streamlit as st
import numpy as np
import sys
from streamlit import cli as stcli
from scipy.integrate import quad #Single integral
from scipy.integrate import dblquad
from PIL import Image

def main():
    col1, col2, col3= st.columns(3)
    foto = Image.open('ufpe.png')
    col1.image(foto, width=130)
    foto = Image.open('caa.jpg')
    col3.image(foto, use_column_width=True)
    
    st.markdown("<h2 style='text-align: center; color: #306754;'>Avaliação Didática: Espaços vetoriais-Definição e propriedades</h2>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style="background-color: #F3F3F3; padding: 10px; text-align: center;">
          <p style="font-size: 20px; font-weight: bold;">Aplicação web para Teste de Dependência Linear e Mudança de Base</p>
          <p style="font-size: 15px;">By: Victor H. R. Lima</p>
        </div>
        """, unsafe_allow_html=True)

    aba = st.sidebar.radio("Escolha o módulo", ["Teste de Dependência Linear", "Mudança de Base"])
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
    


if st._is_running_with_streamlit:
    main()
else:
    sys.argv = ["streamlit", "run", sys.argv[0]]
    sys.exit(stcli.main())
