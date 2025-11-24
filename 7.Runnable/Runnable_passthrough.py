from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough

load_dotenv()

model = ChatCohere(
    model="command-a-03-2025",
)

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Write a joke in this topic : {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Explain this joke:{joke}",
    input_variables=["joke"]
)

joke_gen_chain=RunnableSequence(prompt1,model,parser)

parallel_chain=RunnableParallel({
    "joke":RunnablePassthrough(),
    "explanation":RunnableSequence(prompt2,model,parser)
})

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)

result=final_chain.invoke({"topic":"Math"})

print(result)
