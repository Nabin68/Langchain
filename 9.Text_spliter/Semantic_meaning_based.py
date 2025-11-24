#not working idk why but we will look into it when working with it

from langchain_text_splitters import SemanticTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

splitter = SemanticTextSplitter(
    embedding=emb,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)
text="""
Artificial Intelligence is rapidly transforming industries, enabling machines to perform tasks that once required human intelligence. However, my laptop battery has started draining unusually fast, and I'm not sure whether it's due to the new software updates or a hardware issue. Meanwhile, climate change remains one of the biggest challenges of our generation, with rising temperatures and unpredictable weather patterns affecting daily life everywhere. Yesterday, I also tried a new pasta recipe that surprisingly turned out delicious despite using fewer spices than usual. In the financial world, cryptocurrency markets experienced significant volatility last week, causing many investors to reconsider their long-term strategies.
")
"""
chunks = splitter.split_text(text)
print(chunks)