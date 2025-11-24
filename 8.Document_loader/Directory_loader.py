from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

loader=DirectoryLoader(
    path="PDFs",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs=loader.load()

print(len(docs))  #total no of pages in all 3 .pdf documents

print(docs[0].page_content)  #show page content of 1st page out of all the pages in total form all the PDFs

print(docs[0].metadata)