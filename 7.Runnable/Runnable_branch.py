#get the user query and reply them according to the feedback
from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough,RunnableLambda,RunnableBranch

from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

model = ChatCohere(
    model="command-a-03-2025",
)
parser1=StrOutputParser()

class QueryType(BaseModel):
    query_type:Literal["Complaint","Refund","General query"]=Field(description="distinguish the type of query based on the users feedback")
        
parser2=PydanticOutputParser(pydantic_object=QueryType)

prompt1=PromptTemplate(
    template="Classify the type of query based on the users feedback into complaints,refund and General query\n {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={"format_instruction":parser2.get_format_instructions()}
)

classifier_chain=RunnableSequence(prompt1,model,parser2)

complaints_prompt=PromptTemplate(
    template="Write a message to the user for the complaint based on the following feedback \n{feedback}",
    input_variables=["feedback"]
)
general_query_prompt=PromptTemplate(
    template="Write a message to the user for the general query based on the following feedback \n{feedback}",
    input_variables=["feedback"]
)
refund_prompt=PromptTemplate(
    template="Write a message to the user for the refund request based on the following feedback \n{feedback}",
    input_variables=["feedback"]
)

branch_chain=RunnableBranch(
    (lambda x:x['classification'].query_type=="Complaint",RunnableSequence(complaints_prompt | model | parser1)),
    (lambda x:x['classification'].query_type=="General query",RunnableSequence(general_query_prompt | model | parser1)),
    (lambda x:x['classification'].query_type=="Refund",RunnableSequence(refund_prompt | model | parser1)),
    RunnableLambda(lambda x: "Sorry, I couldn't classify your query type.")
)
final_chain=RunnableSequence(
    RunnableParallel(
        classification=classifier_chain,
        feedback=RunnablePassthrough()),
    RunnableParallel(
        classification=lambda x:x["classification"],
        response=branch_chain
    )
)
result=final_chain.invoke({"feedback":"How can I fill out the bank account opening form?"})
print(result['classification'])
print(result['response'])
