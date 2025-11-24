from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding= CohereEmbeddings(
    model="embed-english-v3.0",
    # dimensions=100     #this is not being used in cohere
                        #other models like openai have this used to reduce the cost
)

result=embedding.embed_query("Kathmandu is the capital of Nepal")

print(str(result))
print(f"Embedding length: {len(result)}")

#so this code willl generate embedding for the text and return it in the form of vector