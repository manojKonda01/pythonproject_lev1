import string
import random

OTP = "".join([random.choice(string.digits) for i in range(6)])