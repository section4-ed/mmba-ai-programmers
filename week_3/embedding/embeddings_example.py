# Example documents about movies
texts = [
    "The Godfather is a classic mafia crime drama",
    "Inception explores dreams within dreams",
    "The Shawshank Redemption is a story about hope and friendship",
]

from openai import OpenAI

def get_embedding(text):
    client = OpenAI()
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding

# get_embedding(texts[0])

embeddings = []
for text in texts:
    embedding = get_embedding(text)
    embeddings.append(embedding)

import faiss

dimension = len(embeddings[0])
index = faiss.IndexFlatL2(dimension)

import numpy 
index.add(numpy.array(embeddings, dtype='float32'))

query = 'Tell me about a prison movie'

query_embedding = get_embedding(query)
distances, indicies = index.search(numpy.array([query_embedding], dtype='float32'), 3)

for i in range(3):
    # print(f"Match {i+1}, Distance: {distances[0][i]:.f4}")
    print(texts[indicies[0][i]])

