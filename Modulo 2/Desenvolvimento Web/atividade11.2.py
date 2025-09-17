import streamlit as st 

st.sidebar.image("theking.jpg")
st.sidebar.title("Calculo IMC")

peso = st.text_input('informe seu peso')
altura = st.text_input("informe sua altura")
IMC = peso / (altura*altura)

botao=st.button('calcular')
colunas =st.columns(2)
with colunas[0]:
    st.title('coluna 1')
    st.button('clique 1')
with colunas[1]:
    st.title('coluna 2')
    st.button('clique 2')

if botao == True:
    peso = float(peso)
    altura = float(altura)

    IMC = peso/(altura*altura)
    if IMC <=18.5:
        st.write("Magreza")
    elif IMC <24:
        st.write("Peso Ideal")


    





