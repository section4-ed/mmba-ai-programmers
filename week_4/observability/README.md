# Observability

## Overview
In this homework, you'll implement observability using LangSmith into the RAG system you worked on earlier. 

## Task
Your task is to complete the `search_documents` function in the starter code. The function should:
- Connect to your Pinecone index
- Query the vector database for relevant documents
- Return the search results for use in generating answers
- All operations will be automatically traced by LangSmith

**Estimated Time:** 5 minutes

## Requirements
- LangSmith API key (set as environment variable `LANGCHAIN_API_KEY`)
- Pinecone index with the same name as specified in the code (default is "test")

## Getting Started
1. Sign up for required services:
   - [LangSmith](https://smith.langchain.com/) - for observability
3. Get your API keys:
   - LangSmith API key from Settings > API Keys
4. Install required packages:
   ```bash
   pip install openai pinecone-client langsmith
   ```
5. Set up your environment variables:
   ```bash
   # For Mac/Linux
   export LANGCHAIN_API_KEY=your_langsmith_api_key_here
   export LANGCHAIN_PROJECT=rag-observability

   # For Windows (Command Prompt)
   set LANGCHAIN_API_KEY=your_langsmith_api_key_here
   set LANGCHAIN_PROJECT=rag-observability

   # For Windows (PowerShell)
   $env:LANGCHAIN_API_KEY="your_langsmith_api_key_here"
   $env:LANGCHAIN_PROJECT="rag-observability"
   ```

## Testing
1. Navigate to the `start` directory
2. Update the Pinecone index name to match your own.
3. Find the TODO and add a traceable decorator to trace your LLM and RAG calls in LangSmith.
4. Run the script to verify your implementation:
   ```bash
   python main.py
   ```
5. View your traces in LangSmith:
   - Log in to your LangSmith account
   - Navigate to your project
   - Review the detailed traces of your RAG pipeline execution

## Documentation
- LangSmith documentation: https://docs.smith.langchain.com

## Solution
A complete solution is provided in the `solution` directory. Try to implement the function yourself before checking the solution! 