import openai
import streamlit as st
import os

# Configurar la clave de la API de OpenAI
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

if not api_key:
    st.warning("Please enter a valid API key to continue.")
else:
    openai.api_key = api_key
    # Continuar con el resto del código que utiliza la clave de API

# Set page title
st.title('GPT-3 Essay Outliner')

# Get essay title from user
title = st.text_input('Enter the title of your essay:')

# Generate essay outline using OpenAI GPT-3
prompt = f"TOC: {title}"
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=500,
    top_p=0.9
)

# Show essay outline
st.write(response['choices'][0]['text'])
