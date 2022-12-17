import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 47.497913  # Your latitude
MY_LONG = 19.040236  # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude and MY_LONG-5 <= iss_longitude:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    else:
        return False

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        my_email = "dji14shokh17@gmail.com"
        pwd = "wwnpnokdwnucbifq"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=pwd)
            connection.sendmail(from_addr=my_email, msg="Subject: Look up\n\n The iss is over your head, so look up",
                                to_addrs="shokhrukhnigmatillaev@yahoo.com")




