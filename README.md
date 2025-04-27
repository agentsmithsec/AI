# Project: build, attack and defend a mini AI chatbot Security Lab

## Goal
- Build an AI chatbot using OpenAI API. **Purely for Testing & Learning Purposes only**
- Simulate attacks like prompt injection and jailbreaking.
- Defend against attacks with input/output filtering.

**FYI- API is not Free from OpenAI, please use other models eg: OpenRouter,Claude ...etc**
you will get error when you run chatbot.py due to api calls limit for free users else use paid version.

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Create `.env` file with your API Key.
3. Run: `python chatbot.py` (for basic bot)
4. Run: `python attack_tests.py` (to test attacks)
5. Run: `python defense.py` (secured chatbot)

**Step	What to do**
1	Sign up at openrouter.ai and get your API key.
2	Put the API key in .env file.
3	Update your chatbot.py to set base_url="https://openrouter.ai/api/v1".
4	Change model to "openai/gpt-3.5-turbo".
5	Run your chatbot! 🎯

## What I Learned
- Prompt injection and model jailbreaking are real risks.
- Filtering user input can prevent common attacks.
- Monitoring output is critical for AI system safety.
