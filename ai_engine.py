import streamlit as st
import google.generativeai as genai

# Configure the API key using Streamlit secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

def get_ai_message(prompt):
    # Select the Gemini model you want to use
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Make the API call to generate content
    response = model.generate_content(prompt)
    
    # Return the text from the response
    return response.text
