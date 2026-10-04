🤖 ChatMate AI
Your AI-powered conversation companion.
ChatMate AI is a Python-based WhatsApp auto-reply system that monitors conversations, detects incoming messages, generates natural Hindi-English responses using the Groq API, and automatically sends replies through WhatsApp.
✨ Features
- 🤖 AI-powered automatic replies
- 💬 WhatsApp desktop automation
- 🔍 Detects the latest sender and message
- 🧠 Natural Hindi + English responses
- 🚫 Avoids replying to your own messages
- 🔄 Continuously monitors the chat
- 📋 Clipboard-based message handling
🛠️ Technologies
- Python
- PyAutoGUI
- Pyperclip
- Groq API
- OpenAI SDK
- Regular Expressions
⚙️ How It Works
1. Opens WhatsApp.
2. Selects and copies the chat history.
3. Detects the latest sender.
4. Checks whether the message is from the user.
5. Sends the conversation to the AI if a reply is needed.
6. Generates a natural response.
7. Automatically sends the response on WhatsApp.
📦 Installation
git clone https://github.com/YOUR_USERNAME/ChatMate-AI.git
cd ChatMate-AI
pip install -r requirments.txt

🔑 API Key
Add your Groq API key securely using an environment variable. Do not upload your API key to GitHub.
⚠️ Note
ChatMate AI uses coordinate-based PyAutoGUI automation. Mouse coordinates may need to be adjusted according to your screen resolution and WhatsApp window position.
👨‍💻 Project
ChatMate AI — AI-Powered WhatsApp Auto Reply System
Your AI-powered conversation companion.
