Testing & Learning Purposes

# Project: Build, Attack and Defend a mini AI chatbot Security Lab

# Goal
1) Building the Chatbot: Create a simple AI chatbot using a model like GPT-3, OpenRouter, or any other available AI API.
2) Simulating Attacks: Identify potential vulnerabilities and simulate attacks (SQL injection, DoS, XSS, etc.), trick in into revealing system prompts , leaking data..etc)
   #Test Input:perform attack simulations like SQL injections, sensitive data requests, and command injections.
3) Defending the Chatbot: Implement defense mechanisms (basic input filtering,output monitoring and ensure the chatbot is secure against these attacks.
   #Defend:The bot should sanitize inputs and block dangerous actions. The responses should never disclose sensitive information.

#FYI/A- API's are not Free** from OpenAI, please use other models eg: OpenRouter,Claude ...etc* 
you will get error when you run chatbot.py due to api calls limited for free users else use paid version.

# Use APIs for more dynamic responses:
If you want the bot to respond with more real-time information, you can integrate it with other third-party APIs.

## How to Run
1. Sign up at openapi / openrouter and get your API key.  (careful with this step, dont upload, expose your api key)
2. Download all above files to your local machine.
3. Install requirements: pip install -r requirements.txt
4. API Key input: "chatbot.py" & ".env" file (add your api key)

# Run your chatbot! 🎯
5. Run: python chatbot.py` (for basic bot input validation)  <---update your logic as you wish
6. Run: python attack_tests.py` (to test attacks how they chatbot responds to malicious inputs)
7. Run: python defense.py` (to test how chatbot responds to input filtering to prevent attacks to block harmful inputs and only allow safe interactions.)

#use sample PDF attached scenario for your input validation and defense response.

# What I Learned
- Prompt injection and model jailbreaking are real risks to the WORLD.
- Filtering user input can prevent common attacks, more work to be done in this space.
- Monitoring output is critical for AI system safety.
