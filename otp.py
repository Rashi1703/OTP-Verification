import os
import math
import random
import smtplib
import ssl
from email.message import EmailMessage

digit="123456789"
OTP=""
for i in range(6):
    OTP=OTP+str(random.randrange(1,9))
    
msg=OTP+" is your one time password"
email_sender = 'rashijain1710@gmail.com'
email_password = 'aqqnlmcvllgpgdvv'
email_receiver =input("Enter your email id:")
subject = 'OTP Verification'
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(msg)
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

d = input("Enter Your OTP >>: ")
if(d == OTP):
    print("Verified")
else:
    print("Check your OTP again")



