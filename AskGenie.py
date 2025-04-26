import streamlit as st
import google.generativeai as genai

# Configure your API key
genai.configure(api_key="GOOGLE_API_KEY")  # Replace with your API key

# Set up the model
model = genai.GenerativeModel('gemini-1.5-pro')  # Corrected model name

# Streamlit app title
st.title("Ask Genie Chatbot")

# User input
user_prompt = st.text_input("Enter your prompt:")

# Button to submit the prompt
if st.button("Generate Response"):
    if user_prompt.strip() != "":
        with st.spinner("Generating response..."):
            # Generate content
            response = model.generate_content(user_prompt)
            # Show the response
            st.success("Response generated!")
            st.write(response.text)
    else:
        st.warning("Please enter a prompt before generating a response.")
