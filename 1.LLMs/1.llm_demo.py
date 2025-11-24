#this is how LLM model type used to work 
#this wont work because cohere removed this features 
#and upgraded to chatmodel
#which is in Langchain/@.ChatModels/chatmodel_demo.py

#this thing will work with gemini anthropic or openai

from dotenv import load_dotenv
from langchain_community.llms import Cohere

load_dotenv()

llm = Cohere(model="command-a-03-2025")

response = llm.invoke("What is the capital of Nepal?")

print(response)
