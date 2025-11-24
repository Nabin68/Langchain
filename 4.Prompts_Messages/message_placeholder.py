from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

#chat template
chat_template=ChatPromptTemplate([
    ("system","You are a helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user","{query}")
])

chat_history = []
with open("chat_history.txt") as f:
    for line in f:
        chat_history.append(line.strip())  # or build HumanMessage objects here

# print(chat_history)

#create prompt
prompt=chat_template.invoke({"chat_history":chat_history,"query":"When will i get my refund"})

print(prompt)
