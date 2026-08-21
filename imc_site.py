import streamlit as st

#Título da página
st.title ("Calculadora de IMC")

# Texto explicativo
st.write("Minha primeira página")

# Input de dados
nome = st.text_input("digite seu nome:" )

# Botão
if st.button ("Enviar"):
    if nome:
        st.success(f"Olá {nome} Seja Bem-Vindo(a)!!!")
    else:
        st.warning("Gentileza, digitar um nome!")
