import smtplib
import email_msg
import authentication
from getpass import getpass
# sender email and password check
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = input("Enter Your Gmail!! Sender :")
password = getpass("Sender enter Your password : ")


# Try to log in to server and send email

server = smtplib.SMTP(smtp_server, port)
server.starttls()
server.login(sender_email, password)
receiver_email = input("Enter Receiver's Email : ")
server.sendmail(sender_email, receiver_email, email_msg.message )

print("Otp Sent to your Email please Check your email")

authentication.authen()

server.sendmail(sender_email, receiver_email, email_msg.mes)
