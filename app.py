import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyDplai8TdzRpuYaY73_cRD0JiZajCyhqu4")  # Replace with your actual API key

# Streamlit UI
st.title("🤖 AI Code Reviewer")
st.write("Enter your Python code below and get a detailed review!")

user_code = st.text_area("Enter Python code here ...", height=250)

if st.button("Generate Review"):
    if user_code.strip():
        st.write("Analyzing your code... Please wait ⏳")

        # Creating the prompt for AI
        prompt = f"Review the following Python code. Identify potential bugs, inefficiencies, and suggest improvements:\n\n{user_code}"

        # Call Google Generative AI API
        try:
            model = genai.GenerativeModel("gemini-pro")  # Correct model
            response = model.generate_content(prompt)  # Generate AI response
            review_result = response.text  # Extract text

            st.subheader("🔍 Code Review Report")
            st.markdown(review_result)
        except Exception as e:
            st.error(f"Error while analyzing code: {e}")
    else:
        st.warning("⚠️ Please enter some Python code first.")
