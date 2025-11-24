from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_cohere import ChatCohere
from dotenv import load_dotenv 

load_dotenv()

Model=ChatCohere(
    model="command-a-03-2025"
)
Messages=[
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about langchain")
]

result=Model.invoke(Messages)

Messages.append(AIMessage(content=result.content))

print(Messages)