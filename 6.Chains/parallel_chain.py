from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel

load_dotenv()

model=ChatCohere(
    model="command-a-03-2025"
)

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Generate a short and simple notes from the following text \n {text}",
    input_variables=['text']  
)

prompt2=PromptTemplate(
    template="Generate 5 short question answer from the following text \n {text}",
    input_variables=['text']
)

prompt3=PromptTemplate(
    template="Merge the provided notes and quiz into single document,Notes->{notes},quiz->{quiz}",
    input_variables=['notes','quiz']
)

parallel_chain=RunnableParallel({
    'notes':prompt1 | model | parser,
    'quiz':prompt2 | model |parser
})

merge_chain=prompt3 | model | parser

chain=parallel_chain | merge_chain

text=""""
Extra debugging checklist

HF token: make sure HUGGINGFACEHUB_API_TOKEN is set in .env. Without it the inference client may fail silently or select different provider logic.

huggingface_hub version: older versions had different client signatures. pip install -U huggingface_hub helps.

Model capability: confirm if model is chat-capable. If not, use text-generation API.

LangChain class match: ChatHuggingFace => chat endpoint. For text-generation models you should use the non-chat wrapper (or call InferenceClient.text_generation yourself).

Inspect resp: when calling HF client directly, print the raw response to know the exact shape (resp[0]["generated_text"] or resp.generated_text).
"""

result=chain.invoke({'text':text})

print(result)
chain.get_graph().print_ascii()