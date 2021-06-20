from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import otp_generator
sub = "OTP Validation "
body = """
This OTP is Sent as a part of small python project 
Don't Worry
Enter This OTP
""" + otp_generator.OTP
msg = MIMEMultipart()
msg["Subject"] = sub
msg.attach(MIMEText(body, "plain"))
message = msg.as_string()
subb = "OTP Verified " + u'\u263A'
bod = """
OTP Verified Successfully
Thank You \u263A
"""
m = MIMEMultipart()
m["Subject"] = subb
m.attach(MIMEText(bod, "plain"))
mes = m.as_string()
