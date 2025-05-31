import os
import glob
import openai
from pinecone import Pinecone
from typing import List
from langsmith import Client, traceable

# Initialize OpenAI and Pinecone clients
openai.api_key = os.environ.get("OPENAI_API_KEY")
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

# LangSmith client setup
langsmith_api_key = os.environ.get("LANGCHAIN_API_KEY")
langsmith_project = "rag-observability"
langsmith_client = Client(api_key=langsmith_api_key)

# Constants
INDEX_NAME = "test"
EMBEDDING_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4o-mini-2024-07-18"

@traceable(name="load_documents")
def load_documents():
    """Load all text documents from the letters directory."""
    documents = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, "letters/*.txt")
    files = glob.glob(path)
    
    for file_path in files:
        with open(file_path, 'r') as file:
            content = file.read()
            documents.append({"content": content, "metadata": {"source": file_path}})
    
    print(f"Found {len(documents)} letters")
    return documents

@traceable(name="chunk_documents")
def chunk_documents(documents, chunk_size=1000, chunk_overlap=200):
    """Split documents into smaller chunks for better processing."""
    chunks = []
    
    for doc in documents:
        content = doc["content"]
        metadata = doc["metadata"]
        
        # Simple text splitting - you can implement more sophisticated chunking if needed
        for i in range(0, len(content), chunk_size - chunk_overlap):
            if i > 0:
                start = i - chunk_overlap
            else:
                start = 0
                
            chunk_content = content[start:start + chunk_size]
            if chunk_content:
                chunks.append({"content": chunk_content, "metadata": metadata})
    
    return chunks

@traceable(name="get_embeddings")
def get_embeddings(texts: List[str]):
    """Generate embeddings for a list of texts using OpenAI."""
    response = openai.embeddings.create(
        input=texts,
        model=EMBEDDING_MODEL
    )
    return [embedding.embedding for embedding in response.data]

@traceable(name="embed_documents")
def embed_documents(chunks, namespace):
    """Embed documents and store them in Pinecone."""
    # Get Pinecone index
    index = pc.Index(INDEX_NAME)
    
    # Prepare batches (Pinecone usually works well with batches of ~100)
    batch_size = 100
    for i in range(0, len(chunks), batch_size):
        chunk_batch = chunks[i:i+batch_size]
        
        # Get text from each chunk
        texts = [chunk["content"] for chunk in chunk_batch]
        
        # Get embeddings
        embeddings = get_embeddings(texts)
        
        # Prepare data for Pinecone
        vectors = []
        for j, embedding in enumerate(embeddings):
            vectors.append({
                "id": f"chunk_{i+j}",
                "values": embedding,
                "metadata": chunk_batch[j]["metadata"]
            })
        
        # Upsert to Pinecone
        index.upsert(vectors=vectors, namespace=namespace)

@traceable(name="search_documents")
def search_documents(query, namespace, top_k=5):
    """Search the vector store with the user query."""
    # Get query embedding
    query_embedding = get_embeddings([query])[0]
    
    # Search Pinecone
    index = pc.Index(INDEX_NAME)
    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        namespace=namespace,
        include_metadata=True,
        include_values=False
    )
    
    # Get matched documents
    docs_with_scores = []
    for match in results["matches"]:
        # Load the document content based on the source file
        with open(match["metadata"]["source"], 'r') as f:
            content = f.read()
        docs_with_scores.append((content, match["score"]))
    
    return docs_with_scores

@traceable(
        name="ask_openai",
        project_name=langsmith_project,
        run_type="llm"
        )
def ask_openai(query, documents):
    """Ask OpenAI a question with context from the documents."""
    # Join all documents into a single context string
    context = "\n\n".join([doc for doc, _ in documents])
    
    # Create messages for OpenAI
    messages = [
        {"role": "system", "content": "Provide an answer to the user's query about Berkshire Hathaway."
                              "Documents from the Berkshire Hathaway shareholder meetings will be provided."
                              "Use those documents to best answer the question."},
        {"role": "system", "content": f"Documents: {context}"},
        {"role": "user", "content": query}
    ]
    
    # Use LangSmith wrapper for OpenAI client
    response = openai.chat.completions.create(
        model=CHAT_MODEL,
        messages=messages
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    # Step 2: Write a query
    user_query = "When did Berkshire Hathaway purchase it's first coke stock?" # Year: 1988

    # Step 3: Check Pinecone for similar chunks
    docs_and_scores = search_documents(query=user_query, namespace="chunks")
    
    # Step 4: Put docs into prompt and send to OpenAI
    response = ask_openai(user_query, docs_and_scores)
        
    print(response) 