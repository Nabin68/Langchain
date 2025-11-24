from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser,ResponseSchema

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

schema=[
    ResponseSchema(name="Fact_1",description="Fact 1 about the topic"),
    ResponseSchema(name="Fact_2",description="Fact 2 about the topic"),
    ResponseSchema(name="Fact_3",description="Fact 3 about the topic")
]

parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template="Give me 3 fact about {topic}\n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)



"""Either we can write this way"""
# prompt=template.invoke({"topic":"Blackhole"})

# result=model.invoke(prompt)

# final_result=parser.parse(result.content)


"""Or we can write it in chain format"""
chain= template | model | parser
final_result=chain.invoke({"topic":"Blackhole"})

print(final_result)