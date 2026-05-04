import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
load_dotenv()

#langsmith tracking

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING"]= "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "default_project")

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

##Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that answers questions asked."),
    ("human", "{question}")
])

##streamlit fraemwork

st.title("langchain demo with llama 2")
input_text = st.text_input("ask any question u have in mind :) ")


##ollama llama 2 model


llm = Ollama(model="gemma:2b")

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)  


