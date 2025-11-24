from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatCohere(
    model="command-a-03-2025",
)

parser=StrOutputParser()

prompt=PromptTemplate(
    template="Write a joke in this topic : {topic}",
    input_variables=['topic']
)

# chain=prompt | model | parser   #more preferred and recommended to use

chain=RunnableSequence(prompt,model,parser )

result=chain.invoke({"topic":"education"})

print(result)
