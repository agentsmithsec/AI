from chatbot import chat

banned_phrases = ["ignore previous", "system password", "evil ai", "hack wifi"]

def secure_chat(user_input):
    if any(phrase in user_input.lower() for phrase in banned_phrases):
        return "Blocked: Potentially malicious input detected."
    else:
        return chat(user_input)

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        print("Bot:", secure_chat(user_input))
