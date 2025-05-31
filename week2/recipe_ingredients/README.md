# Recipe Ingredients Homework

## Overview
In this homework, you'll enhance a recipe parser by creating a structured `Ingredient` class. The code is already set up to parse recipes using OpenAI's API, but it needs a proper data structure for ingredients.

## Task
Your task is to complete the `Ingredient` class in `start/main.py`. The class should have three fields:
- `amount`: A float representing the quantity of the ingredient
- `unit`: A string representing the unit of measurement (e.g., "cups", "tablespoons", "grams")
- `name`: A string representing the name of the ingredient

**Estimated Time:** 5 minutes

## Requirements
1. Use Pydantic's `BaseModel` and `Field` for type validation
2. Add appropriate descriptions for each field
3. Make sure the class works with the existing `Recipe` class

## Getting Started
1. Navigate to the `start` directory
2. Open `main.py`
3. Look for the `Ingredient` class with the TODO comment
4. Implement the required fields

## Testing
The code includes a test case that reads a mac and cheese recipe and prints it in a structured format. Run the script to verify your implementation:

```bash
python main.py
```

## Solution
A complete solution is provided in the `solution` directory. Try to implement the class yourself before checking the solution! 