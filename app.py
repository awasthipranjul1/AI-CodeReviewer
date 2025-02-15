import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyD93jv-nUCK30PGZNJgShG0xI0kYocz_AU")

sys_prompt = """You are a AI python code reviewer"""

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash",
                           system_instruction=sys_prompt)

st.title("GenAI App - AI Python Code Reviewer")

user_prompt = st.text_input("Enter your query:", placeholder="Type your query here...")

btn_click = st.button("Generate Answer")

if btn_click:
    # generate response: we need gemini or gpt model, configure (set the api key), call the model to generate the response
    response = model.generate_content(user_prompt)
    st.write(response.text)
