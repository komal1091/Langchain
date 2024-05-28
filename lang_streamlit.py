from huggingface_hub import hf_hub_download
import os
from getpass import getpass
from langchain import HuggingFaceHub, PromptTemplate, LLMChain
import streamlit as st

# Get Hugging Face API token
os.environ["HUGGINGFACE_API_TOKEN"] = "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"
# Prompt template
template = '''
Question: {question}
Answer: 
'''

prompt = PromptTemplate(template=template, input_variables=["question"])

# HuggingFaceHub LLM initialization
llm = HuggingFaceHub(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    huggingfacehub_api_token="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",
    model_kwargs={"temperature": 0.7, "max_length": 6000}
)

# Streamlit application
st.title("Question and Answer with Hugging Face Hub")

question = st.text_input("Enter your question:")

if st.button("Get Answer"):

    if question:
        chain = LLMChain(llm=llm, prompt=prompt)
        answer = chain.invoke({"question": question})
        st.write("### Answer:")
        st.write(answer['text'].strip())  
    else:
        st.write("Please enter a question.")



# from huggingface_hub import hf_hub_download
# import os
# from langchain import HuggingFaceHub, PromptTemplate, LLMChain
# import streamlit as st
# import time

# # Get Hugging Face API token
# os.environ["HUGGINGFACE_API_TOKEN"] = "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"

# # Prompt template
# template = '''
# Question: {question}
# Answer: 
# '''

# prompt = PromptTemplate(template=template, input_variables=["question"])

# # HuggingFaceHub LLM initialization with a smaller model
# llm = HuggingFaceHub(
#     repo_id="mistralai/Mixtral-2x1B-Instruct-v0.1",  # Assuming a smaller model is available
#     huggingfacehub_api_token="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",
#     model_kwargs={"temperature": 0.7, "max_length": 100}  # Adjust max_length for faster response
# )

# # Streamlit application
# st.title("Question and Answer with Hugging Face Hub")

# question = st.text_input("Enter your question:")

# if st.button("Get Answer"):
#     if question:
#         start_time = time.time()
#         chain = LLMChain(llm=llm, prompt=prompt)
#         try:
#             answer = chain.invoke({"question": question})
#             response_time = time.time() - start_time
#             if response_time < 3:
#                 st.write("### Answer:")
#                 st.write(answer['text'].strip())
#             else:
#                 st.write("Response took too long, please try again.")
#         except Exception as e:
#             st.write("An error occurred:", str(e))
#     else:
#         st.write("Please enter a question.")

# # Function to check accuracy using a test dataset
# def check_accuracy(test_data):
#     correct_answers = 0
#     total_questions = len(test_data)
    
#     for q, expected_answer in test_data:
#         answer = chain.invoke({"question": q})
#         if answer['text'].strip() == expected_answer:
#             correct_answers += 1
    
#     accuracy = correct_answers / total_questions
#     return accuracy

# # Example test dataset (replace with your actual dataset)
# test_data = [
#     ("What is the capital of France?", "Paris"),
#     ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee"),
#     # Add more questions and expected answers here
# ]

# # Check accuracy
# accuracy = check_accuracy(test_data)
# st.write(f"Model Accuracy: {accuracy * 100:.2f}%")



