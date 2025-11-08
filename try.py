from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Twilio credentials (⚠️ Replace with your actual credentials securely)
account_sid = 'ACdba7d37f83a20cdf5dd0fb5ecf7dceae'
auth_token = '02a70dbab2d3d7368e96ea6e766d8c28'
client = Client(account_sid, auth_token)

# Function to send WhatsApp message
def send_whatsapp_sms(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',  # Twilio sandbox number
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f"✅ Message sent successfully! MESSAGE SID: {message.sid}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# User input
recipient_number = input("Enter the recipient's WhatsApp number with country code (e.g., +919876543210): ")
name = input("Enter the recipient's name: ")
message_body = input(f"Enter the message to send via WhatsApp to {name}: ")

# Parse date and time and calculate delay
date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM in 24-hour format): ")

try:
    schedule_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    current_datetime = datetime.now()

    # Calculate delay in seconds
    time_difference = schedule_datetime - current_datetime
    delay_seconds = time_difference.total_seconds()

    if delay_seconds <= 0:
        print(f"⚠️ The specified time {schedule_datetime} is in the past. Please enter a future date and time.")
    else:
        print(f"⏰ Message scheduled to be sent to {name} at {schedule_datetime}.")
        # Wait until the scheduled time
        time.sleep(delay_seconds)
        # Send the message
        send_whatsapp_sms(recipient_number, message_body)

except ValueError:
    print("❌ Invalid date or time format. Please use YYYY-MM-DD and HH:MM (24-hour format).")
