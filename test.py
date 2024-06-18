# from datetime import datetime
#
# hozirgi_vaqt = datetime.now()
# day = hozirgi_vaqt.strftime("%Y")
# print(day)

# mcxs chux adtg kwwh
from email.message import EmailMessage
import ssl
import smtplib

email_sender = "komronhtmlcss@gmail.com"
email_password = "mcxs chux adtg kwwh"

email_receiver = "komronahmadov@yahoo.com"

subject = "ey inson"
body = ":)"

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    print("yes yes yes")


