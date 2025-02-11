!pip install streamlit

import streamlit as st
import google.generativeai as gena

# Set your OpenAI API Key
gena.api_key = "AIzaSyDplai8TdzRpuYaY73_cRD0JiZajCyhqu4"

st.title("💬 An AI Code Reviewer")
st.subheader("Enter your Python code below and get a review!")

# Text area for user input
user_code = st.text_area("Enter your Python code here ...", height=200)

if st.button("Generate"):
    if user_code.strip():
        with st.spinner("Analyzing code..."):
            prompt = f"Review the following Python code and provide a bug report and corrected version:\n\n{user_code}"
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "system", "content": "You are an AI code reviewer."},
                          {"role": "user", "content": prompt}]
            )
            result = response["choices"][0]["message"]["content"]

        st.subheader("Code Review")
        st.markdown(result)  # Display AI-generated output
    else:
        st.warning("Please enter some Python code.")

