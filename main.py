from dotenv import load_dotenv
import smtplib
import os
import random
import datetime as dt

today = dt.datetime.now()

if today.weekday() == 1:
    with open("quotes.txt") as q_file:
        quotes = q_file.readlines()
        todays_quote = random.choice(quotes)

load_dotenv('.env')

HOST_SMTP = "smtp.gmail.com"
MY_EMAIL = "notchamath@gmail.com"
PW = os.getenv("PW")

connection = smtplib.SMTP(HOST_SMTP, port=587)
connection.starttls()
connection.login(user=MY_EMAIL, password=PW)
connection.sendmail(from_addr=MY_EMAIL,
                    to_addrs="chamath.contact@gmail.com",
                    msg=f"Subject:Hello\n\n{todays_quote}")

connection.close()
