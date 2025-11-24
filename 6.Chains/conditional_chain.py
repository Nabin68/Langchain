from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnableBranch,RunnableLambda
from langchain_core.output_parsers import StrOutputParser

#the LLM can give any output,rather than just +ve and -ve.so we will be using PydanticOutputParser to control the output from the LLM
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

model=ChatCohere(
    model="command-a-03-2025"
)

parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment:Literal['Positive','Negative']=Field(description="Give the sentiment of the Feedback")
    
parser2=PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template="classify the sentiments of the following feedback into positive or negative,just answer positive or negative \n {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

feedback="This is a beautiful smartphone"

classifier_chain= prompt1 | model | parser2

positive_prompt=PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=['feedback']
)

negative_prompt=PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=['feedback']
)

branch_chain=RunnableBranch(
    (lambda x:x.sentiment == 'Positive',positive_prompt | model | parser),
    (lambda x:x.sentiment == 'Negative',negative_prompt | model | parser), 
    RunnableLambda(lambda x: "Could not find sentiment") #we used this to convert lambda function to lambda chain so that it can be compatible wtih runnablebranch
)

chain=classifier_chain | branch_chain

print(chain.invoke({'feedback':feedback}))












