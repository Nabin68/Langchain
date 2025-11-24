from langchain_text_splitters import RecursiveCharacterTextSplitter

text="""Full runnable example — define, store, load and use chat history (two variants)
Below are two complete examples you can run as-is.
Pure-Python (no external libs) — shows how to store history (in memory + JSON file), load it, then build the final messages payload you would send to any chat LLM (OpenAI, Anthropic, etc.).
LangChain-style (if you have langchain / langchain_core) — shows the same flow but using MessagesPlaceholder + ChatPromptTemplate. (This section is optional — run it only if you have the library installed.)
What is a Message Placeholder?A message placeholder is a special marker (a variable) used inside a chat template to inject messages dynamically at runtime.
It does not contain actual text itself — instead, it holds a place where messages will later be inserted.
It is used when you're building a conversation for LLMs (like ChatGPT, OpenAI API, LangChain, etc.) and want to pass in:
user messages assistant messages system instructions history memory any conversation context
"""

splitter=RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0
)
chunks=splitter.split_text(text=text)

print(len(chunks))
print(chunks[0])