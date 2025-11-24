from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage

load_dotenv()

Model=ChatCohere(
    model="command-a-03-2025"
)

chathistory=[
    SystemMessage(content="You are a very helpful assitant")
]
while True:
    user_input=input("You: ")
    chathistory.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result=Model.invoke(chathistory)
    chathistory.append(AIMessage(content=result.content))
    print("AI: ",result.content)
print(chathistory)