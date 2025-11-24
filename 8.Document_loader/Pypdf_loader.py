from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("PDFfile.pdf")

docs=loader.load()

print(docs[0].page_content)
