import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Set page title
st.title('GPT-3 Essay Outliner')

# Get essay title from user
title = st.text_input('Enter the title of your essay:')

# Generate essay outline using OpenAI GPT-3
prompt = f"Contents: {title}"
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=500,
    top_p=0.9
)

# Show essay outline
st.write(response['choices'][0]['text'])
