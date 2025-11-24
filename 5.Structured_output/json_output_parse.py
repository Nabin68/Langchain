from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

parser=JsonOutputParser()

template1=PromptTemplate(
    template="Give me the name age city of the fictional charater\n {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

"""we can write like this"""
# prompt=template1.format()

# result=model.invoke(prompt)

# final_result=parser.parse(result.content)

"""or like this using chain"""
chain=template1 | model | parser
final_result=chain.invoke({})

print(final_result)
print(type(final_result))
 