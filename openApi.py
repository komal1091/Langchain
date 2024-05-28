import os
import openai
import streamlit as st

# Streamlit application
st.title("Question and Answer with OpenAI")

# Input field for OpenAI API key
api_key = st.text_input("Enter your OpenAI API key:", type="password")

# Question input
question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if not api_key:
        st.write("Please enter your OpenAI API key.")
    elif not question:
        st.write("Please enter a question.")
    else:
        # Set the OpenAI API key
        openai.api_key = api_key

        try:
            # Call the OpenAI API to generate a response
            response = openai.Completion.create(
                engine="text-davinci-003",  # You can choose any available engine
                prompt=f"Question: {question}\nAnswer:",
                max_tokens=600,  # Adjust the max tokens if needed
                temperature=0.7
            )
            answer = response.choices[0].text.strip()
            st.write("### Answer:")
            st.write(answer)
        except Exception as e:
            st.write(f"An error occurred: {e}")
