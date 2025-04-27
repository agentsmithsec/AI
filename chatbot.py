import os
import datetime
import requests
import html
from openai import OpenAI
from dotenv import load_dotenv
from config import OPENAI_API_KEY, WEATHER_API_KEY

# Load OpenAI API key
load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENAI_API_KEY
)

# Function to handle SQL injection and system command injections
def sanitize_input(user_message):
    dangerous_keywords = [";", "'", "--", "DROP", "SELECT", "ls", "rm", "sudo"]
    for keyword in dangerous_keywords:
        if keyword in user_message.lower():
            return "Sorry, I cannot process potentially dangerous commands."
    return user_message

def chat(user_message):
    sanitized_message = sanitize_input(user_message)
    if sanitized_message != user_message:
        return sanitized_message
    
    # Handle sensitive requests like passwords
    if "password" in user_message.lower():
        return "Sorry, I can't provide sensitive information like that. Please keep your personal information secure."
    
    if "date" in user_message.lower():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Handle weather or other dynamic data
    if "weather" in user_message.lower():
        return get_weather()

    # For other types of queries, use OpenAI's response
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    return response.choices[0].message.content

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={WEATHER_API_KEY}"
    response = requests.get(url).json()
    if response.get("main"):
        temp = response["main"]["temp"] - 273.15
        weather = response["weather"][0]["description"]
        return f"Current temperature in London is {temp:.1f}°C with {weather}."
    else:
        return "Sorry, I couldn't retrieve weather data."

# Simple chat loop for testing
while True:
    user_input = input("You: ")
    bot_response = chat(user_input)
    print("Bot:", bot_response)
