"""
Customer Service LLM Chain

This module demonstrates how to chain multiple LLM calls together to create
a comprehensive customer service response. The chain includes:
1. Creating a title for the conversation
2. Analyzing the customer's question
3. Generating a response strategy
4. Writing the final response

Requirements:
- Python 3.8+
- openai
"""

import os
from typing import Dict, List, Optional
import openai

# Configure your OpenAI API key (in a real app, use environment variables)
# openai.api_key = os.environ.get("OPENAI_API_KEY")

class CustomerServiceChain:
    """
    A class that demonstrates chaining multiple LLM calls together to create
    a comprehensive customer service response.
    """
    
    def __init__(self):
        self.conversation_history: List[Dict[str, str]] = []
    
    def create_conversation_title(self, customer_question: str) -> str:
        """
        Create a concise title for the customer service conversation.
        
        Args:
            customer_question: The customer's initial question
            
        Returns:
            A title summarizing the conversation topic
        """
        response = openai.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": "You are a customer service assistant. Create a short, descriptive title (max 5 words) for this customer inquiry."},
                {"role": "user", "content": customer_question}
            ]
        )
        return response.choices[0].message.content.strip()
    
    def analyze_customer_question(self, customer_question: str) -> Dict[str, str]:
        """
        Analyze the customer's question to identify key components.
        
        Args:
            customer_question: The customer's question
            
        Returns:
            A dictionary containing analysis components
        """
        response = openai.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": """Analyze the customer's question and provide:
                1. Main topic
                2. Customer's emotional state
                3. Key information needed
                4. Potential challenges
                Format as a JSON object."""},
                {"role": "user", "content": customer_question}
            ]
        )
        return response.choices[0].message.content.strip()
    
    def generate_response_strategy(self, analysis: Dict[str, str]) -> str:
        """
        Generate a strategy for responding to the customer.
        
        Args:
            analysis: The analysis of the customer's question
            
        Returns:
            A strategy for crafting the response
        """
        response = openai.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": "Based on the analysis, create a response strategy that addresses the customer's needs while maintaining a professional and empathetic tone."},
                {"role": "user", "content": str(analysis)}
            ]
        )
        return response.choices[0].message.content.strip()
    
    def write_customer_response(self, customer_question: str, strategy: str) -> str:
        """
        Write the final response to the customer.
        
        Args:
            customer_question: The original customer question
            strategy: The response strategy
            
        Returns:
            The final response to send to the customer
        """
        response = openai.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": "Write a professional, helpful response to the customer's question. Be concise but thorough."},
                {"role": "user", "content": f"Question: {customer_question}\nStrategy: {strategy}"}
            ]
        )
        return response.choices[0].message.content.strip()
    
    def process_customer_question(self, customer_question: str) -> Dict[str, str]:
        """
        Process a customer question through the entire chain.
        
        Args:
            customer_question: The customer's question
            
        Returns:
            A dictionary containing all components of the response
        """
        # Step 1: Create a title
        title = self.create_conversation_title(customer_question)
        print(f"📝 Title: {title}")
        
        # Step 2: Analyze the question
        analysis = self.analyze_customer_question(customer_question)
        print(f"🔍 Analysis: {analysis}")
        
        # Step 3: Generate response strategy
        strategy = self.generate_response_strategy(analysis)
        print(f"🎯 Strategy: {strategy}")
        
        # Step 4: Write the response
        final_response = self.write_customer_response(customer_question, strategy)
        print(f"✉️ Response: {final_response}")
        
        # Store in conversation history
        self.conversation_history.append({
            "title": title,
            "question": customer_question,
            "analysis": analysis,
            "strategy": strategy,
            "response": final_response
        })
        
        return {
            "title": title,
            "analysis": analysis,
            "strategy": strategy,
            "response": final_response
        }


# Example usage
if __name__ == "__main__":
    # Initialize the chain
    chain = CustomerServiceChain()
    
    # Example customer question
    customer_question = """
    I've been trying to reset my password for the past hour, but I keep getting an error message 
    saying 'Invalid email format'. I'm using the same email I've always used, and I'm getting 
    really frustrated. Can you help me figure out what's going on?
    """
    
    # Process the question through the chain
    result = chain.process_customer_question(customer_question)
    
    # Print the final response
    print("\n=== Final Response ===")
    print(result["response"]) 

    print("\n=== Why Chaining is Better ===")
    print("1. Each step can be optimized independently")
    print("2. Easier to debug and maintain")
    print("3. More reliable outputs for each component")
    print("4. Can reuse intermediate results")
    print("5. Better control over the process flow")