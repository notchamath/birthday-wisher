import smtplib
from dotenv import load_dotenv
import os

load_dotenv('.env')

HOST_SMTP = "smtp.gmail.com"
MY_EMAIL = "notchamath@gmail.com"
PW = os.getenv("PW")

connection = smtplib.SMTP(HOST_SMTP, port=587)
connection.starttls()
connection.login(user=MY_EMAIL, password=PW)
connection.sendmail(from_addr=MY_EMAIL,
                    to_addrs="chamath.contact@gmail.com",
                    msg="Hello World")

connection.close()
