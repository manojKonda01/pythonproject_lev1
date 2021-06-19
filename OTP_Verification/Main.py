import smtplib
import email_msg
import authentication
from getpass import getpass

# sender email and password check
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "jackyspirrel@gmail.com"
password = getpass("Type your password and press enter: ")


# Try to log in to server and send email

server = smtplib.SMTP(smtp_server, port)
server.starttls()
server.login(sender_email, password)
receiver_email = input('Enter Your Email : ')
server.sendmail('&&&&&&&&&&&', receiver_email, email_msg.message )

print("Otp Sent to your Email please Check your email")

authentication.authen()