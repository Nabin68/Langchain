# 📘 LangChain Learning Series

A comprehensive hands-on guide to mastering LangChain fundamentals and building production-ready AI applications.

## 🎯 What's Covered

This repository provides practical examples and implementations of core LangChain concepts:

- **Language Models** - Cohere and HuggingFace integration
- **Embeddings** - Text vectorization with Cohere and HuggingFace models
- **Prompts & Templates** - Dynamic prompt engineering with messages
- **Structured Outputs** - JSON, Pydantic models, and output parsers
- **Chains** - Simple, sequential, parallel, and conditional workflows
- **Runnables (LCEL)** - Advanced pipelines with branching logic
- **Document Loaders** - PDF, CSV, text, and web content ingestion
- **Text Splitters** - Intelligent chunking strategies
- **Vector Stores** - ChromaDB and FAISS implementations
- **Retrievers** - Semantic search with MMR and multi-query
- **RAG Pipelines** - Complete retrieval-augmented generation systems

## 🚀 Key Features

- Real-world examples with Cohere and HuggingFace
- Open-source and accessible model implementations
- Step-by-step implementations from basic to advanced
- Production-ready code patterns
- Complete RAG application workflows

## 🛠️ Tech Stack

- **LangChain Core** - Framework foundation
- **LLM Providers** - Cohere, HuggingFace
- **Vector Databases** - Chroma, FAISS
- **Python Libraries** - Pydantic, sentence-transformers

## 📦 Quick Start

```python
# Example: Simple RAG Pipeline
from langchain_cohere import ChatCohere, CohereEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

# Initialize components
llm = ChatCohere(model="command-r")
embeddings = CohereEmbeddings(model="embed-english-v3.0")
vector_store = Chroma(embedding_function=embeddings)

# Create retriever and chain
retriever = vector_store.as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
```

## 📚 Learning Path

1. **Models** - Understanding language and embedding models
2. **Prompts** - Crafting effective templates and messages
3. **Outputs** - Structuring LLM responses
4. **Chains & Runnables** - Building AI workflows
5. **Documents** - Loading and splitting content
6. **Vectors & Retrieval** - Semantic search implementation
7. **Integration** - Complete RAG applications

## 🎓 Who This Is For

- Developers learning LangChain from scratch
- Engineers building LLM-powered applications
- Anyone interested in RAG and semantic search
- Teams implementing AI solutions


## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

⭐ **Star this repo** if you find it helpful for your LangChain journey!
