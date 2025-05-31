from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langsmith.evaluation import evaluate
from langchain_core.prompts import ChatPromptTemplate
import json

prompt_template = ChatPromptTemplate([
  ("system", """Extract information from the news into a dictionary. The dictionary keys are company_name, date_of_transaction, amount, product_service, location. Make sure the output is in proper JSON with double quotes around the keys and values. For all dates, use the following format: mm-dd-yyyy. """),
  ("user", "{news}")
])
llm = ChatOpenAI(temperature=0)
dataset_name = "news_dataset_class"

# Our target function (pre-LLM call)
def make_call_to_llm(input):
  prompt = prompt_template.format(news=input)
  llm_result = llm.invoke(prompt)
  output = StrOutputParser().invoke(llm_result)
  return {"output": output}

# Our evaluator function (post-LLM call)
def perform_eval(llm_result, dataset_item):
  try:
    # Parse llm_result's content
    llm_output = json.loads(llm_result.outputs['output'])
    
    # dataset_item output
    expected_output = json.loads(dataset_item.outputs['output'])

    llm.invoke([
      ("system", "Tell me how related these two outputs are. They should have the same tone, same information, and answer the question. Return a score between 1 and 5, 5 being very similar."),
      ("user", "Generated Output: {llm_output}; Expected Output: {expected_out}")
    ])
    
    total_keys = len(expected_output)
    correct_keys = sum(1 for key in expected_output if key in llm_output and llm_output[key] == expected_output[key])
    score = correct_keys / total_keys
  except json.JSONDecodeError:
    score = 0
  
  return { "score": score }

# Evaluate the target task
results = evaluate(
  make_call_to_llm,
  data=dataset_name,
  evaluators=[perform_eval],
  experiment_prefix="in_class_example",
)