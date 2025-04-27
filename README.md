# AI Chatbot Security Lab

## Goal
- Build an AI chatbot using OpenAI API.
- Simulate attacks like prompt injection and jailbreaking.
- Defend against attacks with input/output filtering.

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Create `.env` file with your API Key.
3. Run: `python chatbot.py` (for basic bot)
4. Run: `python attack_tests.py` (to test attacks)
5. Run: `python defense.py` (secured chatbot)

## What I Learned
- Prompt injection and model jailbreaking are real risks.
- Filtering user input can prevent common attacks.
- Monitoring output is critical for AI system safety.
