
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="text-generation"
)

Model=ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str=Field(description="Name of the person")
    age:int = Field(gt=18,description="Age of the person")
    city:str = Field(description="Name of the city the person belong to ")
    
    
parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template="Generate the name,age and city of a fictional {place} person\n {format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

# prompt=template.invoke({"place":"Nepali"})

# print(prompt)

# result=Model.invoke(prompt)

# final_result=parser.parse(result.content)

chain=template | Model | parser

final_result=chain.invoke({"place":"Nepali"})

print(final_result)