import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Intialize GPT-3 model 
tokenizer = openai.AutoTokenizer.from_pretrained('text-davinci-003') 
model = openai.AutoModelWithLMHead.from_pretrained('text-davinci-003') 

# Create the Streamlit app 
st.title("GPT-3 Outline Generator") 
prompt = st.text_input('Enter your essay topic:') 

# Generate the essay outline 
if st.button('Generate Outline'): 
    with st.spinner('Generating Outline...'): 
        generated_outline = tokenizer.generate(
            prompt,
            num_return_sequences=3,
            max_length=150,
            return_tensors='pt'
        ) 

# Display the essay outline 
for i in range(generated_outline.shape[0]): 
    outline = tokenizer.decode(generated_outline[i], skip_special_tokens=True) 
    st.markdown(f"#### Outline {i+1}") 
    st.success(outline)
