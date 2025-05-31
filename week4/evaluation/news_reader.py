from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import json

model_id='gpt-4o-mini'
prompt_name='extract_news_data'

# Load the model and prompt
llm = ChatOpenAI(model=model_id, temperature=0)
prompt_template = ChatPromptTemplate([
  ("system", "Extract information from the news into a dictionary. The dictionary keys are company_name, date_of_transaction, amount, product_service, location. Make sure the output is in proper JSON with double quotes around the keys and values."),
  ("user", "{news}")
])

# Load stories
with open('class_3/class_code/stories.json', 'r') as f:
    stories = json.load(f)['stories']

# Process each story
for story in stories:
    formated_prompt = prompt_template.invoke({"news": story})
    response = llm.invoke(formated_prompt)
    print(f"\nInput: {story['news']}\nOutput: {response.content}")