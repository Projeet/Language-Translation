import streamlit as st

st.title("Language Translation App")

language_first=st.selectbox('Choose your language',
    ('Hindi', 'English', 'Freanch'))

your_text=st.text_area("Text to translate")