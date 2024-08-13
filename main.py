import os
import streamlit as st
from dotenv import load_dotenv
from simpleaitranslator.translator import set_openai_api_key, get_text_language, translate

load_dotenv()
set_openai_api_key(os.getenv("OPENAI_API_KEY"))


# Inject custom CSS to style all headers
st.markdown(
    """
    <style>
    h1, h2, h3, h4, h5, h6 {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)


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

st.markdown("<h1 style='text-align: center;'>Simple AI Translator</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Define custom CSS to style the div
custom_css = f"""
    <style>
        .non-editable-textarea {{
            height: 500px;
            overflow-y: auto;
            white-space: pre-wrap;
            border: 1px solid #ccc;
            padding: 10px;
            background-color: #f0f2f6;
            border-radius: 5px;
            margin: -15px 0 0 0 ;
        }}
    </style>
"""




with col1:
    st.header("Text to translate")
    text_input_placeholder = st.empty()


    # Text area for user input
    txt = st.text_area(label="", label_visibility="collapsed", height=500)

    text_input_placeholder.text_input(
        "",
        disabled=True,
        placeholder="Detected language for translation" if txt is "" else get_text_language(txt),
        label_visibility="collapsed",
    )

with col2:
    st.header("Translated text")
    option = st.selectbox(
        "",
        ("Email", "Home phone", "Mobile phone"),
        index=None,
        placeholder="Select contact method...",
        label_visibility="collapsed"
    )

    if txt:
        language = get_text_language(txt)
        translated_txt = translate(txt)

    else:
        translated_txt = "Translation"

   # moj = st.text_area(label="asd",  height=500)

    # Render the CSS in Streamlit
    # Render the CSS in Streamlit
    st.markdown(custom_css, unsafe_allow_html=True)

    # Display the text area with the text
    st.markdown(f'<div class="non-editable-textarea">{translated_txt}</div>', unsafe_allow_html=True)

