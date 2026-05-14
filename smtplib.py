'''
smtplib:
----------

-->This provides a client to sending emails via the simple mail transfer protocol(SMTP).
'''
import smtplib

from email.message import EmailMessage

sender_email="sender_mail@gmail.com"

password="Automated password generator"

receiver_email="receiver_mail@gmail.com"
msg=EmailMessage()
msg['Subject']="Python Email Automation"
msg['From']=sender_email
msg['To']=receiver_email

msg.set_content("Hello Student,This email is sent using python.")

server = smtplib.SMTP_SSL("smtp.gmail.com",465)

server.login(sender_email,password)

server.send_message(msg)

server.quit()

print("Email Sent Successfully")
























