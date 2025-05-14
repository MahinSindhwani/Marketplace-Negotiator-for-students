# import json
# from openai import OpenAI



# client = OpenAI()

# # Load listing description
# with open("listing.json", "r", encoding="utf-8") as f:
#     listing = json.load(f)

# # Prompt with negotiation
# prompt = f"""
# You are a university student looking to rent or buy something on a student budget. Here's the listing:

# \"{listing["description"]}\"

# Now write a message to the seller. Be polite and respectful, but try to negotiate the price. Mention you're a student, 
# that you're interested, and ask if they'd be willing to reduce the price or help in any way. Keep it under 100 words 
# and in a casual but professional tone.
# """

# # Send prompt to OpenAI API
# response = client.chat.completions.create(
#     model="gpt-4o",  # You can use "gpt-4o-mini" for cheaper/faster response
#     messages=[
#         {"role": "user", "content": prompt}
#     ]
# )

# # Print the AI-generated message
# print(response.choices[0].message.content)