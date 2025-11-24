from langchain_cohere import ChatCohere
from dotenv import load_dotenv

load_dotenv()

model = ChatCohere(
    model="command-a-03-2025",
    temperature=1.5,
    max_completion_tokens=4
)

response=model.invoke("write me a poem about sun")

print(response.content)

# so this is how all other models works
# in this same way we can use claude,openai,gemeni and all other AI models
