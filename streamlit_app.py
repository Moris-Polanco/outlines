import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")

st.title("GPT-3 Essay Outline Generator")

st.header("Enter Your Essay Title Here")

title = st.text_input("")

st.write("Generating Essay Outline...")

response = api.Engine(engine="text-davinci-003").completion(
    prompt=title,
    max_tokens=1000,
    temperature=0.7,
    top_p=0.9,
    frequency_penalty=0.2
)

st.write(response['choices'][0]['text'])
