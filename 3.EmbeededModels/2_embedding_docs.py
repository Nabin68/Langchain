from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding= CohereEmbeddings(
    model="embed-english-v3.0"
)

documents=[
    "hello there",
    "how are you guys",
    "how you guys are doing well"
]

result=embedding.embed_documents(documents)

print(str(result))
print(f"Embedding length: {len(result)}")

#so this code willl generate embedding for the entire docs and return it in the form of vector