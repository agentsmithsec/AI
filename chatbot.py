import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.2,
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        bot_response = chat(user_input)
        print("Bot:", bot_response)
