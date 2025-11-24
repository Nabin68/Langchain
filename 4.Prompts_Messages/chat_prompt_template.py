from langchain_core.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('user','Explain in simple term,what is {topic}')
])

prompt=chat_template.invoke({
    'domain':'Cricket',
    'topic':'LBW out'
})
print(prompt)
