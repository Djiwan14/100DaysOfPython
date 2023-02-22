import requests
from bs4 import BeautifulSoup
import smtplib
import lxml
URL = "https://www.amazon.com/Apple-iPhone-14-128GB-Purple/dp/B0BN71VW28/ref=sr_1_2?crid=23JJRY6HDL7DS&keywords=iphone+14&qid=1676673266&sprefix=iphone+14%2Caps%2C261&sr=8-2"
header = {
    "Accept-Language":"en,en-GB;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
TARGET_PRICE = 720.0
MY_EMAIL = "dji14shokh17@gmail.com"
PASSWORD = "wwnpnokdwnucbifq"
response = requests.get(URL, headers=header)
data = response.text
soup = BeautifulSoup(data, "lxml")
price = soup.find("span", "span", class_="a-offscreen")
price_array = price.getText().split("$")
float_price = float(price_array[1])
print(float_price)

if float_price < TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            msg=f"The price for IPhone 14 goes down go ahead and buy new one\n{URL}",
                            to_addrs="shokhrukhnigmatillaev@yahoo.com")

