"""import smtplib


my_email = "hihello2405@gmail.com"
password="gdwaoiwzpupscepw"
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()

    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,to_addrs="harinidonthula@gmail.com",
                        msg="Subject:Hello\n\nThis is the body of the email")

"""

import datetime as dt
import smtplib
import random

time_now=dt.datetime.now()
week_day=time_now.weekday()
my_email = "hihello2405@gmail.com"
password="gdwaoiwzpupscepw"

with open("quotes.txt", "r") as file:
    file=file.readlines()
    random_quote=random.choice(file)

if week_day==2:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="harinidonthula@gmail.com",
                            msg=f"Subject:Hello\n\n{random_quote}")
