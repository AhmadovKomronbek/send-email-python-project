from datetime import datetime
import pandas as pd
from email.message import EmailMessage
import ssl
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# starter data
data_csv = pd.read_csv("data.csv")
data_dict = data_csv.to_dict(orient="records")
now_time = datetime.now()
with open("data_struckture.txt") as file:
    struck = file.read()

# functions
def check_data_time(user_time, time_now):
    user_day = user_time["day"]
    user_month = user_time["month"]
    time_day = int(time_now.strftime("%d"))
    time_month = int(time_now.strftime("%m"))
    if user_day == time_day and user_month == time_month:
        return True

def send_email(email, name):
    global struck

    email_sender = os.environ.get("EMAIL")
    email_password = os.environ.get("TOKEN")

    email_receiver = email

    subject = f"Salom {name}"
    body = struck.replace("[name]", f"{name}")

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        print("sented")

# main code
for row in data_dict:
    if check_data_time(row, now_time):
        send_email(row["email"], row["name"])
