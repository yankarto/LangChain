
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import  load_dotenv

import sys
# print(sys.path)


load_dotenv()

LANGCHAIN_TRACING_V2="true"
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_PROJECT="OpenaAI"

# LANGCHAIN_API_KEY=""
# OPENAI_API_KEY=""

# os.environ['LANGCHAIN_API_KEY']=LANGCHAIN_API_KEY
# os.environ['OPENAI_API_KEY']=OPENAI_API_KEY


##langsmith API KEY
# os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")

##OpenAI API KEY
# os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")



#langsmith project name
os.environ['LANGCHAIN_PROJECT']=LANGCHAIN_PROJECT

#langsmith tracking
os.environ['LANGCHAIN_TRACING_V2']=LANGCHAIN_TRACING_V2
os.environ['LANGCHAIN_ENDPOINT']=LANGCHAIN_ENDPOINT

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user quieries"),
        ("user","Question:{question}")
    ]
)

## Streamlit framework

st.title('Lang chain Demo with openAI')
input_text=st.text_input("Search the topic you want")

##OpenAI LLM

llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
    