import streamlit as st 
st.title("CALCULADORA")
st.image("calcular123.png")
if 'produtos' not in st.session_state:
    st.session_state = 'home'
st.button('Calcular')



numero1=st.text_input("Digite o número: ")
numero2=st.text_input("Digite o número2: ")

colunas =st.columns(4)
with colunas[0]:
    botao1 = st.button('Somar')
    if botao1 == True:
        soma = int(numero1) + int(numero2) 
        st.write(soma)


with colunas[1]:
    botao2 = st.button('Subtratir')
    if botao2 == True:
        subtração = int(numero1) - int(numero2)
        st.write(subtração)


with colunas[2]:
     botao3 = st.button('Multiplicar')

     if botao3 == True:
         multiplicação = int(numero1) * int(numero2)
         st.write(multiplicação)


with colunas[3]:
    botao4 = st.button('Dividir')

    if botao4 == True:
        divisão = int(numero1) / int(numero2)
        st.write(divisão)


