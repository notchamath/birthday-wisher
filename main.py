from dotenv import load_dotenv
import smtplib
import os
import random
import datetime as dt
import pandas

birthdays = pandas.read_csv("birthdays.csv")
b_dict = birthdays.to_dict(orient="records")

today = dt.datetime.now()
today_month = today.month
today_date = today.day

todays_bdays = [person for person in b_dict if person["month"] == today_month and person["day"] == today_date]

for person in todays_bdays:
    num = random.randint(1, 3)
    with open(f"letter_templates/letter_{num}.txt") as letter:
        msg = letter.read()
        bday_wish = msg.replace("[NAME]", person["name"])

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
                        to_addrs=person["email"],
                        msg=f"Subject:Happy Birthday!\n\n{bday_wish}"
                            f"\n\n{todays_quote}")

    connection.close()
