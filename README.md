# 📱 WhatsApp Message Automation using Twilio

This Python project allows you to **schedule and send WhatsApp messages automatically** using the Twilio API.  
It securely loads your Twilio credentials from an `.env` file and lets you schedule a message at any date and time.

---

## 🚀 Features
- Schedule WhatsApp messages for future times  
- Securely stores Twilio credentials using environment variables  
- User-friendly prompts and error handling  
- Works with the official Twilio Sandbox  

---

## 🧠 Requirements

Install the dependencies before running:
```bash
pip install twilio python-dotenv
Create a .env File

Inside your project folder, create a file named .env and add your Twilio credentials:

TWILIO_ACCOUNT_SID=your_twilio_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here


⚠️ Never share or push this file — it’s listed in .gitignore.

4️⃣ Run the Script
python3 main.py
Example Run
Enter the recipient's WhatsApp number with country code (e.g., +919876543210): +919876543210
Enter the recipient's name: John
Enter the message to send via WhatsApp to John: Hello John! This is a scheduled message.
Enter the date to send the message (YYYY-MM-DD): 2025-11-09
Enter the time to send the message (HH:MM in 24-hour format): 15:30
⏰ Message scheduled to be sent to John at 2025-11-09 15:30:00.
✅ Message sent successfully! MESSAGE SID: SMxxxxxxxxxxxxxxxxxxxx
Project Structure
Whatsapp-Message-Automation/
│
├── main.py          # Main script
├── .env             # Twilio credentials (ignored in Git)
├── .gitignore       # Prevents sensitive data uploads
└── README.md        # Project documentation
