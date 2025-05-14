import json
from openai import OpenAI

class Negotiator:
    def __init__(self, jsonPath="listing.json", model="gpt-4o"):
        self.jsonPath = jsonPath
        self.model = model
        self.client = OpenAI()
        self.listing = self.loadListing()
        self.response = None
    
    def loadListing(self):
        try:
            with open(self.jsonPath, "r", encoding="utf-8") as f:
                listing = json.load(f)
            return listing
        except Exception as e:
            print("Error loading listing JSON:", e)
            return {}
        
    def buildPrompt(self):
        description = self.listing.get("description", "No description available.")
        price = self.listing.get("price", "unknown")

        return f"""
        You are a university student looking to rent or buy something on a student budget.

        Here's the listing description:
        \"{description}\"

        The listed price is: {price}

        Now write a message to the seller. Be polite and respectful, but try to negotiate the price. Mention you're a student, 
        that you're interested, and ask if they'd be willing to reduce the price or help in any way. Keep it under 100 words 
        and in a casual but professional tone.
        """
    
    def generateMessage(self):
        prompt = self.buildPrompt()

        try:
            self.response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}]
            )
        except Exception as e:
            print("Error generating message:", e)
            self.response = None
    
    def message(self):
        if self.response:
            return self.response.choices[0].message.content
        else:
            print("No message generated.")