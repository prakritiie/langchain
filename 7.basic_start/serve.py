from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="llama-3.3-70b-versatile", api_key=groq_api_key)

#1 create the prompt template
system_template = "translate the following text into {language}:"
prompt = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("human", "{input_text}")
])

#2 create the output parser
parser = StrOutputParser()


#3 chain the components together
chain = prompt | model | parser


#4 create the app and add the route
app = FastAPI(title =" langchain server",
              version="0.1",
              description="a simple app to translate text using groq and langchain")

add_routes(app,chain,path="/chain")


#5 serve the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

    

