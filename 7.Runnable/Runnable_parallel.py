from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel,RunnableSequence

load_dotenv()

model=ChatCohere(
    model="command-a-03-2025",
)
parser=StrOutputParser()

tweet_prompt=PromptTemplate(
    template="Generate a  twitter post about the topic :{topic}",
    input_variables=["topic"]
)
linkedin_prompt=PromptTemplate(
    template="Generate a linkedin post about the topic :{topic}",
    input_variables=["topic"]
)

parallel_chain=RunnableParallel({
    "tweet": RunnableSequence(tweet_prompt,model,parser),
    "linkedin":RunnableSequence(linkedin_prompt,model,parser)
})



result=parallel_chain.invoke({"topic":"AI"})

print(result) #print whole output of both
print(result["tweet"])  #print only the result for tweet