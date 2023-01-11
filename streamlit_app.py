```python
import streamlit as st
import openai

# API key de OpenAI
openai.api_key = "YOUR_API_KEY"

# Crear una página de bienvenida
st.title("Bienvenido a tu App de Streamlit con OpenAI GPT-3 Text-Davinci-003")
st.markdown("Esta aplicación te ayudará a crear outlines de artículos usando OpenAI GPT-3 Text-Davinci-003.")

# Obtener el texto de entrada del usuario
input_text = st.text_input("Introduzca el texto de entrada")

# Usar OpenAI GPT-3 Text-Davinci-003 para generar el outline
outline = openai.Completion.create(engine="davinci-003", prompt=input_text, max_tokens=100)

# Mostrar el outline generado
st.markdown("El outline generado es el siguiente:")
st.write(outline["choices"][0]["text"])
