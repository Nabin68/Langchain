#here we tried running embedding model locally in our system via HuggingFace

from langchain_huggingface import HuggingFaceEmbeddings

embeddding=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text="hello there"

vector=embeddding.embed_query(text=text)

print(str(vector))
