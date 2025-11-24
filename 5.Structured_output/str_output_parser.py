"""using String output parser"""
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="text-generation"
)

Model=ChatHuggingFace(llm=llm)

template1=PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

template2=PromptTemplate(
    template="Write a 5 line summary on the following text\n {text}",
    input_variables=["text"]
)
parser=StrOutputParser()

chain=template1 | Model | parser | template2 | Model | parser

"""get the input as template1 |send it to model | parse it in good form of O/P | send the op to template 2 | and again send the template to Model | and again parse the output from that model """

result=chain.invoke({'topic':"Black Hole"})

print(result)








"""normally we do this"""
# from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate

# load_dotenv()

# llm=HuggingFaceEndpoint(
#     repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
#     task="text-generation"
# )

# model=ChatHuggingFace(llm=llm)


# template1=PromptTemplate(
#     template="Write a detailed report on {topic}",
#     input_variables=["topic"]
# )

# prompt1=template1.invoke({"topic":"black hole"})
# result=model.invoke(prompt1)

# template2=PromptTemplate(
#     template="Write a 5 line summary on the following text\n {text}",
#     input_variables=["text"]
# )

# prompt2=template2.invoke({"text":result.content})
# result1=model.invoke(prompt2)

# print(result1.content)
