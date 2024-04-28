import streamlit as st
from LLM import language_model as lm

st.title("Language Translation App")

your_text=st.text_area("Text to translate")


language=st.selectbox('Choose your language',
    ('Hindi', 'French', 'Italian', 'Korean', 'Hibrew', 'Arabic', 'Japanese', 'Russian'))

output_language=language
text=your_text
human_mesage=f"""
        Given the input sentence and output language below:
        Input Sentence : {text}
        Output Language : {output_language}
        
        Please translate the input sentence into {output_language} without giving any explanation.

        Translation: 
    """
if st.button("Translate"):
    response=lm.get_llm_response(human_mesage)
    st.write(f"Translated Text: {response}")
    