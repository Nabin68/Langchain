
from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from typing import Literal,Optional

load_dotenv()

Model = ChatCohere(model="command-a-03-2025")

class Review(BaseModel):
    summary: str
    sentiment: Literal["pos","Neg","Neu"]=Field(description="Return sentiments of the review either pos,neg,nue")
    pros:Optional[list[str]]=Field(default=None,description="Write all the pros")
    cons:Optional[list[str]]=Field(default=None,description="Write all the cons")
    name:Optional[str]=Field(default=None,description="Write the name of the reviewer")

# Create structured model
structured_model = Model.with_structured_output(schema=Review)

result = structured_model.invoke(
    "The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this."
)

print(result)
print(result.summary)
print(result.sentiment)
 