# this worked but after update TypedDict cannot be used with langchain
from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional

load_dotenv()

# Create base model
Model = ChatCohere(model="command-a-03-2025")

# Define structured output type
class Review(TypedDict):
    summary: str
    sentiment: str
    pros:Annotated[Optional[list[str]],"Write all the prons"]
    #optional make sure that it is optional if not present it wont return and if there is then will return list
    # annotated is used to give LLM extra context/knowledge of the subject matter

structured_model = Model.with_structured_output(schema=Review)

# Run inference
result = structured_model.invoke(
    "The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this."
)
print(result)
print(result["summary"])
print(result["sentiment"])
