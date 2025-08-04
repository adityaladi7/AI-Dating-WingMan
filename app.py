import streamlit as st
from prompts import build_opener_prompt
from ai_engine import get_ai_message

st.set_page_config(page_title="AI Dating Wingman 💘", page_icon="💬")
st.title("💘 Your AI Dating Wingman")

st.markdown("Get a clever opener for your next match. Just fill in your details below.")

name = st.text_input("Your Name", value="Aditya")
age = st.slider("Your Age", 18, 60, 24)
interests = st.text_input("Your Interests", value="coffee, anime, data, traveling")
match_interests = st.text_input("Matched Person's Interests", value="books, pets, humor")
tone = st.selectbox("Choose Message Tone", ["Funny", "Romantic", "Witty", "Classy"])

if st.button("Generate Opener 💬"):
    with st.spinner("Crafting the perfect message..."):
        prompt = build_opener_prompt(name, age, interests, match_interests, tone)
        response = get_ai_message(prompt)
        st.success("Here's your opening line:")
        st.markdown(f"💬 **{response}**")
