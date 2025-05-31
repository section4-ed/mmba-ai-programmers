# RAG Homework Assignment

## Overview
In this homework, you'll implement a Retrieval-Augmented Generation (RAG) system using Pinecone as a vector database. You'll learn how to store and search through documents using embeddings, and generate answers based on the retrieved content.

## Task
Your task is to complete the `search_documents` function in the starter code. The function should:
- Connect to your Pinecone index
- Query the vector database for relevant documents
- Return the search results for use in generating answers

**Estimated Time:** 15 minutes

## Requirements
- OpenAI API key (set as environment variable `OPENAI_API_KEY`)
- Pinecone API key (set as environment variable `PINECONE_API_KEY`)
- Python packages: `openai`, `pinecone-client`
- Pinecone index with the same name as specified in the code (default is "test")

## Getting Started
1. Sign up for a free account at [Pinecone](https://www.pinecone.io/)
2. Create a new index:
   - Choose a name for your index (e.g., "class_documents" or "test")
   - Under configuration, select the OpenAI "text-embedding-3-small" embedding model
3. Get your API key from the Pinecone dashboard
4. Install required packages:
   ```bash
   pip install openai pinecone-client
   ```
5. Set up your environment variables:
   ```bash
   # For Mac/Linux
   export OPENAI_API_KEY=your_api_key_here
   export PINECONE_API_KEY=your_api_key_here

   # For Windows (Command Prompt)
   set OPENAI_API_KEY=your_api_key_here
   set PINECONE_API_KEY=your_api_key_here

   # For Windows (PowerShell)
   $env:OPENAI_API_KEY="your_api_key_here"
   $env:PINECONE_API_KEY="your_api_key_here"
   ```

## Testing
1. Navigate to the `start` directory
2. **IMPORTANT: Near the bottom of the file in the main function, uncomment and run the document loading and embedding code (first-time setup). Once that runs successfully, comment it again.**
3. Then test with the provided query or create your own questions
4. Run the script to verify your implementation:
   ```bash
   python main.py
   ```

## Documentation
- Pinecone documentation: https://sdk.pinecone.io/python/pinecone/grpc.html#GRPCIndex.query

## Solution
A complete solution is provided in the `solution` directory. Try to implement the function yourself before checking the solution! 