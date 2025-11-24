from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough,RunnableLambda

load_dotenv()

model = ChatCohere(
    model="command-a-03-2025",
)

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Write a joke in this topic : {topic}",
    input_variables=['topic']
)

joke_gen_chain=RunnableSequence(prompt1,model,parser)


def word_count(text):
    return len(text.split())


parallel_chain=RunnableParallel({
    "joke":RunnablePassthrough(),
    "count":RunnableLambda(word_count)
    #"count":RunnableLambda(lambda x: len(x.split()))     or we can use this instead, will give the same answer 
})

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)

result=final_chain.invoke({"topic":"Math"})

print(result)
