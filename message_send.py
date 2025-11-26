import smtplib
import ssl

from email.message import EmailMessage

email = "ENTER YOUR EMAIL ID"
app_password = "ENTER YOUR APP PASSWORD"
receivers =[
           "ENTER MULTIPLE EMAIL  "
]

msg = EmailMessage()
msg['from'] = email
msg['to'] = ", ".join(receivers)
msg['subject'] = "hello you are my best friend"

msg.set_content("hello you are my best friend")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email, app_password)
    server.send_message(msg)                                                                                            