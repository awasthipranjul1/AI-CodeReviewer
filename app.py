import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyD93jv-nUCK30PGZNJgShG0xI0kYocz_AU")

sys_prompt = """You are a helpful AI Tutor for Data Science.
Students will ask you doubts related to various topics in data science.
You are expected to reply in as much detail as possible.
Make sure to take examples while explaining a concept.
In case if a student ask any question outside the data science scope,
politely decline and tell them to ask the question from data science domain only."""

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash",
                           system_instruction=sys_prompt)

st.title("GenAI App - AI Code Reviewer")

user_prompt = st.text_input("Enter your query:", placeholder="Type your query here...")

btn_click = st.button("Generate Answer")

if btn_click:
    # generate response: we need gemini or gpt model, configure (set the api key), call the model to generate the response
    response = model.generate_content(user_prompt)
    st.write(response.text)