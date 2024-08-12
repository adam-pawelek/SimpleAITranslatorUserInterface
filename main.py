import os

import streamlit as st
from dotenv import load_dotenv
from simpleaitranslator.translator import set_openai_api_key, get_text_language, translate

load_dotenv()
set_openai_api_key(os.getenv("OPENAI_API_KEY"))

print(get_text_language("Hello world"))  # Output: 'eng'

# Define CSS to adjust the width of the main content area
css = """
<style>
    .main .block-container {
        max-width: 80%;  /* Adjust this value to your desired width */
        padding-top: 1rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 1rem;
    }
</style>
"""
# Inject the CSS into the Streamlit app
st.markdown(css, unsafe_allow_html=True)




#set_openai_api_key(os.getenv("OPENAI_API_KEY"))

# Your Streamlit app code goes here
st.title("Simple AI Translator")
st.write("This is a simple example of how to change the width of your Streamlit app's page.")



col1, col2 = st.columns(2)

with col1:
    # Placeholder for the header
    header_placeholder = st.empty()

    # Text area for user input
    txt = st.text_area(label="", label_visibility="collapsed")

    # Update the header with the text area input
    header_placeholder.header(f"Detected language {get_text_language(txt)}" if txt else "Write here your text for translation")


with col2:
    st.header("A dog")
    if txt:
        language = get_text_language(txt)
        translated_txt = translate(txt)

    else:
        language = "Language not specified"
        translated_txt = ""
    col2.write(language)
    moj = col2.code(
        translated_txt
    )
    col2.write("Translated text:ashfkljsahfjklshakj;fhsa;jlhf;lsafl;ksal;kfsda;ldfsah;jhdsakjfshdakljdhskjhsdafkjhsda;kj")
    col2.write("asdfsad")
