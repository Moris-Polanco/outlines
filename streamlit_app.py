import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")

st.title("GPT-3 Essay Outline Generator")

st.header("Enter Your Essay Title Here")

title = st.text_input("")

st.write("Generating Essay Outline...")

response = completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
)

st.write(response['choices'][0]['text'])
