from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

def analyze_sentiment(review):
    """
    Analyze the sentiment of a movie review using structured output.
    Returns a dictionary with 'thought' and 'sentiment' keys.
    """
    prompt = f"""
    I want you to tell me if the following movie review is positive or negative.

    Review: {review}

    The final response should be in the following format:
    thought: analyze the review to determine if it's positive or negative
    sentiment: "positive" or "negative"
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    # Parse the response
    content = response.choices[0].message.content
    lines = content.strip().split('sentiment:')
    
    result = {
        "thought": lines[0].replace("thought:", "").strip(),
        "sentiment": lines[1]
    }
    
    return result

def main():
    # Test cases
    reviews = [
        "This film shouldn't work at all. It doesn't have much of a story and the whole dial up internet thing is incredibly dated. However Hanks and Ryan sell it beautifully.",
        "The movie was terrible. The acting was wooden, the plot made no sense, and I want my two hours back.",
        "An absolute masterpiece! The cinematography was stunning, the acting was superb, and the story kept me engaged from start to finish."
    ]

    # Test each review
    for i, review in enumerate(reviews, 1):
        result = analyze_sentiment(review)
        print(f"\nReview {i}:")
        print(f"Thought: {result['thought']}")
        print(f"Sentiment: {result['sentiment']}")

if __name__ == "__main__":
    main() 