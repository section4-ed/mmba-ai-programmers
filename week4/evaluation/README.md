# Homework Assignment: LLM Evaluation with LangSmith

In this homework, you will implement a solution for evaluating a news extraction model using OpenAI's API and LangSmith. The goal is to understand how to effectively evaluate LLM performance on structured information extraction tasks.

## Task Overview

You will use LangSmith to run and track your evaluations for a news information extraction task. The model needs to extract structured data (company name, transaction date, amount, product/service, and location) from news articles.

## Getting Started

1. Navigate to the `start` directory to begin
2. Review the `evaluation.py` file which contains partially implemented functions:
   - `make_call_to_llm` - Already implemented to call OpenAI's API
   - `perform_eval` - Already implemented to evaluate extraction accuracy
   - You need to implement the final `evaluate` function to run the evaluation

## Prerequisites

Before starting, make sure you have:
- An OpenAI API key
- A LangSmith account with API key
- The required Python packages:
  ```
  pip install openai langsmith
  ```

## Environment Setup

Set the following environment variables:
```bash
export OPENAI_API_KEY="your-openai-api-key"
export LANGCHAIN_API_KEY="your-langsmith-api-key"
export LANGCHAIN_PROJECT="news_extraction_homework"
```

## Instructions

1. Complete the evaluation implementation:
   - Implement the missing `evaluate` function at the end of the file
   - Use LangSmith's `evaluate` function to run the evaluation
   - The dataset is already uploaded to LangSmith with the name "news_dataset_class"
   - Create an experiment with the prefix "news_extraction_homework"
   - Run the evaluation on the provided dataset
   - Review the evaluation results in LangSmith's interface

2. Check that your implementation correctly:
   - Uses the `make_call_to_llm` function as the prediction function
   - Uses the `perform_eval` function as the evaluator
   - Connects to the "news_dataset_class" dataset in LangSmith

## Testing

Run your solution with:
```bash
python evaluation.py
```

## Solution

After completing your implementation, you can check the `solution` directory to compare your approach with a reference solution.

## Submission

Submit your completed `evaluation.py` file along with a brief explanation of your implementation choices and any observations about the evaluation results.

## Learning Objectives

By completing this homework, you'll demonstrate your ability to:
- Work directly with the OpenAI API for structured information extraction
- Design effective evaluation metrics for LLM outputs
- Use LangSmith to track and analyze model performance 