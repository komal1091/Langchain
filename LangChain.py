
from huggingface_hub import hf_hub_download
import os
from getpass import getpass
from langchain import HuggingFaceHub, PromptTemplate, LLMChain
import streamlit as st

HUGGINGFACE_API_TOKEN = getpass()
os.environ["HUGGINGFACE_API_TOKEN"] = HUGGINGFACE_API_TOKEN

template = '''

    question : {questions}
    Answer: lets think step by step
'''

template

prompt = PromptTemplate(template = template ,input_variables= {"question"})

prompt


llm = HuggingFaceHub(repo_id= "mistralai/Mixtral-8x7B-Instruct-v0.1",
                     huggingfacehub_api_token='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',
                     model_kwargs = {"temprature" : 0.6, "max_length" : 100})

llm


question = "who is prime minister of india"

print(llm.invoke(question))





