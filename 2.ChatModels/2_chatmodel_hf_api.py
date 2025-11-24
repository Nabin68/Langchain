from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  # Different model
    #here we declare which opensource model you want to use as there are alots of open source model there in Hugging Face
       
    task="text-generation",
    #this is which task we wanna perfrom using this model
    max_new_tokens=512,
)

model = ChatHuggingFace(llm=llm)
response = model.invoke("What is Hugging Face?")
print(response)
