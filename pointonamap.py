import smtplib
import ssl

from email.message import EmailMessage
A = 38.96
B = -77.023
email_sender = 'evanjwassmann@gmail.com'
email_password = 'rinttfpoqyskdbod'
email_receiver = 'evanbandit@gmail.com'

subject = 'Here is my current location'
body = F"""
https://www.google.com/maps/search/?api=1&query={A},{B}"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
#print("https://www.google.com/maps/search/?api=1&query="+str(A)+","+str(B))
#rinttfpoqyskdbod