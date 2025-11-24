from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatCohere(
    model="command-a-03-2025",
)

prompt1=PromptTemplate(
    template="Give detailed explanation on {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Give me the 5 most important word from the following text:\n{explanation}",
    input_variables=['explanation']
)

parser=StrOutputParser()

chain=prompt1 | model | prompt2 | model | parser

result=chain.invoke({'topic':'Unemployment'})

print(result) 

chain.get_graph().print_ascii()