from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

# os.environ["LANGCHAIN_TRACKING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# # api_key = os.getenv("LANGCHAIN_API_KEY")

# # # Check if the environment variable is set and has a non-empty value
# # if api_key is not None and api_key != "":
# #     # Set the environment variable only if it has a non-empty value
# #     os.environ["LANGCHAIN_API_KEY"] = api_key
# # else:
# #     # Handle the case where the environment variable is not set or empty
# #     print("The LANGCHAIN_API_KEY environment variable is not set or empty.")


# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system","you are helpful assistant"),
#         ("user","question:{question}")
#     ]
# )


# st.title("langchain demo for ollama")
# input_text = st.text_input("search your topic")


# llm = Ollama(model = "llama2")
# output_parser = StrOutputParser()
# chain = prompt|llm|output_parser


# if input_text:
#     st.write(chain.invoke({"question": input_text}))





os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)
## streamlit framework

st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("Search the topic u want")

# ollama LLAma2 LLm 
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))