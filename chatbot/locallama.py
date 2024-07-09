
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_community.llms import Ollama

import os
import streamlit as st
from dotenv import  load_dotenv

load_dotenv()

LANGCHAIN_TRACING_V2="true"
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_PROJECT="Ollama"


print(os.getenv("LANGCHAIN_API_KEY"))

os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']=LANGCHAIN_TRACING_V2
os.environ['LANGCHAIN_ENDPOINT']=LANGCHAIN_ENDPOINT
os.environ['LANGCHAIN_PROJECT']=LANGCHAIN_PROJECT

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user quieries"),
        ("user","Question:{question}")
    ]
)
 
## Streamlit framework

st.title('Lang chain Demo with Ollama')
input_text=st.text_input("Search the topic you want")


##ollama Llama2

llm=Ollama(model="llama3")

output_parser=StrOutputParser()

chain=prompt|llm|output_parser
 
if input_text:
    st.write(chain.invoke({'question':input_text}))
    