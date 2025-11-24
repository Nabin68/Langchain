from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding= CohereEmbeddings(
    model="embed-english-v3.0"
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership qualities. He has led India to several memorable victories across formats.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor, sharp cricketing mind, and unmatched finishing skills in limited-overs cricket.",
    "Sachin Tendulkar, often called the 'God of Cricket', is regarded as one of the greatest batsmen in the history of the sport with 100 international centuries.",
    "Rohit Sharma, nicknamed the 'Hitman', is known for his elegant batting style and record-breaking double centuries in ODIs.",
    "Jasprit Bumrah is a world-class Indian fast bowler known for his deadly yorkers, unorthodox action, and match-winning spells.",
    "Yuvraj Singh was India's match-winner in the 2011 World Cup, remembered for hitting six sixes in an over and his inspirational comeback after battling cancer.",
    "Ravichandran Ashwin is India's premier off-spinner, known for his sharp variations, cricketing intelligence, and key role in Test victories at home and abroad.",
    "Hardik Pandya is an Indian all-rounder known for his explosive batting, quick bowling, and exceptional fielding in limited-overs cricket.",
    "Sourav Ganguly, known as 'Dada', transformed Indian cricket with his fearless leadership and strong belief in young talent during the early 2000s.",
    "Rahul Dravid, famously called 'The Wall', is celebrated for his patience, technique, and consistent performances in Test cricket.",
    "Kapil Dev led India to its first World Cup victory in 1983 and was one of the greatest all-rounders in world cricket history.",
    "Shikhar Dhawan is known for his stylish left-handed batting and consistent performances in ICC tournaments.",
    "KL Rahul is a technically gifted batsman who can play multiple roles as an opener, middle-order player, and wicket-keeper.",
    "Rishabh Pant is an attacking wicket-keeper batsman known for his fearless stroke play and match-winning innings in Test cricket.",
    "Mohammed Shami is one of India's leading fast bowlers, recognized for his seam movement, consistency, and ability to take wickets in all conditions."
]

query="Tell me about virat kohli"

doc_embedding=embedding.embed_documents(documents) #converting doc into vector
query_embedding=embedding.embed_query(query) #converting query into vector

similarity=cosine_similarity([query_embedding],doc_embedding)[0] #geetting the similarity
index,score=sorted(list(enumerate(similarity)),key=lambda x:x[1])[-1] #fetching the index to which the query is similar to and the similarity score

print(documents[index])
print("Similarity Score is:",score)

# so in this way we just did the sematic search where we converted the query,docs into vector
# and calculated the similarity between the vector and the one with maximum similarity will be given most score