from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List
from pprint import pprint
import os

# TODO: Add a new Ingredients model that can be used in the Recipe model with the following properties:
# - amount
# - unit
# - name

class Recipe(BaseModel):
    """
    Use this model when working with complete cooking recipes.
    """
    title: str = Field(description="Name of the recipe")
    ingredients: List[str] = Field(description="List of ingredients needed for the recipe")
    instructions: List[str] = Field(description="Step-by-step instructions to prepare the recipe")

def get_recipe_from_text(recipe_text: str) -> Recipe:
    """
    Convert recipe text into a structured Recipe object using OpenAI.
    """
    client = OpenAI()

    # Make the API call
    response = client.responses.parse(
        model="gpt-4o-mini-2024-07-18",
        input=[
            {"role": "user", "content": f"Convert this recipe into the specified format:\n\n{recipe_text}"}
        ],
        text_format=Recipe
    )
    
    return response.output_parsed

# Example usage
if __name__ == "__main__":
    # Read recipe text from file
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    recipe_path = os.path.join(script_dir, "mac_and_cheese_recipe.txt")
    with open(recipe_path, "r") as file:
        recipe_text = file.read()

    # Get structured recipe
    recipe = get_recipe_from_text(recipe_text)
    
    # Print results
    pprint(recipe.ingredients[0])
    # pprint(recipe) # to see the whole object