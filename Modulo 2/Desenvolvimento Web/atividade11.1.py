import streamlit as st 

st.button()
st.checkbox ()

st.title("Lista de contatos")
st.write("meus contatinhos")
contatos=[
        {"nome":"roberto","email":"roberto@email.com","telefone":"11987654321"},
        {"nome":"roberto","email":"roberto@email.com","telefone":"11987654321"},
        {"nome":"roberto","email":"roberto@email.com","telefone":"11987654321"},
        {"nome":"roberto","email":"roberto@email.com","telefone":"11987654321"},
        {"nome":"roberto","email":"roberto@email.com","telefone":"11987654321"},
]

st.table(contatos)
