"""
Customer Service LLM Chainless Example

This module demonstrates how NOT to handle customer service responses by trying to do everything
in a single LLM call. This is meant to be compared with the chained approach to show why
breaking down complex tasks into smaller steps is better.

Requirements:
- Python 3.8+
- openai
"""

import os
from typing import Dict, List, Optional
import openai

# Configure your OpenAI API key (in a real app, use environment variables)
# openai.api_key = os.environ.get("OPENAI_API_KEY")

class CustomerServiceChainless:
    """
    A class that demonstrates how NOT to handle customer service responses by trying to do
    everything in a single LLM call. This is meant to be compared with the chained approach.
    """
    
    def __init__(self):
        self.conversation_history: List[Dict[str, str]] = []
    
    def process_customer_question(self, customer_question: str) -> Dict[str, str]:
        """
        Process a customer question in a single LLM call (not recommended).
        
        Args:
            customer_question: The customer's question
            
        Returns:
            A dictionary containing all components of the response
        """
        # Try to do everything in one prompt (this is not the best approach!)
        response = openai.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": """You are a customer service assistant. For the given customer question:
                1. Create a short title (max 5 words)
                2. Analyze the question for:
                   - Main topic
                   - Customer's emotional state
                   - Key information needed
                   - Potential challenges
                3. Create a response strategy
                4. Write a final response
                
                Format your response as a JSON object with these keys:
                - title
                - analysis (as a nested object with the 4 components above)
                - strategy
                - response
                
                Be professional, empathetic, and thorough."""},
                {"role": "user", "content": customer_question}
            ]
        )
        
        # Parse the response
        result = response.choices[0].message.content.strip()
        
        return result

if __name__ == "__main__":
    # Initialize the chainless processor
    processor = CustomerServiceChainless()
    
    # Example customer question
    customer_question = """
    I've been trying to reset my password for the past hour, but I keep getting an error message 
    saying 'Invalid email format'. I'm using the same email I've always used, and I'm getting 
    really frustrated. Can you help me figure out what's going on?
    """
    
    # Process the question (all at once!)
    result = processor.process_customer_question(customer_question)
    
    # Print the final response
    print("\n=== Final Response ===")
    print(result)
