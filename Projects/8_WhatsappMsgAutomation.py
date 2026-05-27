# Step 1 - Install reqiured libraries

from twilio.rest import Client
from datetime import datetime , timedelta
import time
from dotenv import load_dotenv
import os


load_dotenv()


# Step 2 - Twilio credentials

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid,auth_token)


# Step 3 - define send message function 

def sendWhatsappMessage(recipient_number,message_body):
    try:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body= message_body,
            to= f"whatsapp:{recipient_number}"
        )
        print(f"Message sent successfully! Message SID{message.sid}")

    except Exception as e:
        print("An error occured")



# step 4 - User input 

name = input("Enter the recipient name : ")
recipientNumber = input("Enter the recipient Whatsapp number with country code : ")
message_body = input(f"Enter the msg you want to send to {name} : ")


# Step 5 - parse date/time and calculate delay

date_str = input("Enter the date to send the message (YYYY-MM-DD) : ")
time_str = input("Enter the time to send the mesaage (HH:MM in 24 Hour format) : ")


scheduled_datetime = datetime.strptime(f"{date_str} {time_str}" , "%Y-%m-%d %H:%M")
current_datetime = datetime.now()


time_difference = scheduled_datetime - current_datetime
delay_seconds = time_difference.total_seconds()


if delay_seconds <=0 :
    print("The specified time is in the past. Please enter a future date and time")
else:
    print(f"Message scheduled to be sent to {name} at {scheduled_datetime}.")

    time.sleep(delay_seconds)

    sendWhatsappMessage(recipientNumber,message_body)    