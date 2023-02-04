import smtplib
import ssl
import os


def send_email(message):
    # standard host name
    host = "smtp.gmail.com"
    # standard port number
    port = 465

    username = "ktjanzen42@gmail.com"
    password = os.getenv("GOOGLE_APP_PASSWORD")

    receiver = "ktjanzen42@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

