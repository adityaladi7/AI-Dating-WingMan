# Import necessary libraries
import streamlit as st
import google.generativeai as genai
import os

# --- Configuration ---
# Configure the Gemini API key.
# It is highly recommended to use Streamlit secrets for security.
# To use this, create a file named `.streamlit/secrets.toml` in your repository
# and add your key like this:
#   [keys]
#   google_api_key = "YOUR_API_KEY_HERE"
#
# Then, uncomment the line below and comment out the hardcoded key line.
# genai.configure(api_key=st.secrets["keys"]["google_api_key"])

# For this example, we will use the hardcoded key from your notebook.
# This is NOT recommended for production apps.
genai.configure(api_key="AIzaSyAOu3n3durJJpZf3MHYavCIgWG1fSsHp5s")

# --- Function to Generate the Opening Line ---
def generate_opening_line(match_bio, tone):
    """
    Generates a witty opening line for a dating app using the Gemini API.

    Args:
        match_bio (str): The text from the match's profile bio.
        tone (str): The desired tone for the message (e.g., "funny", "sweet").

    Returns:
        str: The generated opening message or an error message.
    """
    # Create the prompt for the generative model
    prompt = (
        f"Based on this dating profile: \"{match_bio}\", "
        f"write a concise and engaging opening message with a {tone.lower()} tone "
        f"to start a conversation on a dating app. The response should be a "
        f"single, complete message."
    )
    
    try:
        # Initialize the model and generate content
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        
        # Check if the response contains text and return it
        if response and response.text:
            return response.text
        else:
            return "The model did not return a valid response."
            
    except Exception as e:
        # Catch and display any errors from the API call
        return f"An error occurred: {e}"

# --- Streamlit User Interface ---
st.title("Dating App Opening Line Generator �")
st.write("Enter your match's profile bio and select a tone to get a creative opening line!")

# Input fields for the user
match_bio_input = st.text_area("Paste your match's profile bio here:")
tone_input = st.selectbox(
    "Select the tone of the message:", 
    ["Funny", "Sweet", "Clever", "Romantic", "Casual"]
)

# Button to trigger the generation
if st.button("Generate Opening Line"):
    if match_bio_input:
        # Show a loading spinner while the API call is in progress
        with st.spinner("Generating your perfect opening line..."):
            opening_line = generate_opening_line(match_bio_input, tone_input)
            
        # Display the result
        st.success("Generated Opening Line:")
        st.info(opening_line)
    else:
        # Display a warning if the user hasn't entered a bio
        st.warning("Please enter your match's profile bio before generating a line.")

�
