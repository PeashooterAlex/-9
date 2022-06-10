from bs4 import BeatifulSoup
import requests

response = requests.get("https://minfin.com.ua/ua/currency/usd/")


if response.status_code == 200:
    soup = BeatifulSoup(response.text, features="html.parse")
    soup_list = soup.find_all("span",{"class": "mfm-posr"})
    res = soup_list[-1]
    print("today 1$ in ₴ is:", res.text)
    print("okay... do you want see how many $ is... for example... 50₴? yeah? so print here amount of $:")

cash = input()
print("and...", cash, "equals:", cash // res.text)