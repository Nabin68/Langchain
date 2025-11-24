from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatCohere(
    model="command-a-03-2025",
)

prompt = PromptTemplate(
    template="Generate 5 important facts about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic': 'Football'})

print(result)







# from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# load_dotenv()

# llm=HuggingFaceEndpoint(
#     repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
#     task="text-generation"
# )
# model=ChatHuggingFace(llm=llm)

# prompt=PromptTemplate(
#     template="Generate 5 important facts about {topic}",
#     input_variables=['topic']  
# )

# parser=StrOutputParser()

# chain= prompt | model | parser

# result=chain.invoke({'topic':'Football'})

# print(result)