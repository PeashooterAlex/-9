from bs4 import BeautifulSoup
import requests

print("Hello this is exchange rates in gryvni and calc gryvni to any currency. Choose the currency")
print("1: Dollar")
print("2: Euro")
print("3: Rubl")
print("4: GBP")
print("5: Yen")
print("6: Yuan")
print("7: Canadian Dollar")
print("8: Zloty")
print("9: B. Rubl")
print("10: Iran Rial")

choose = input()
if choose == 1:
    response = requests.get("https://minfin.com.ua/ua/currency/usd/")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("span",{"class": "mfm-posr"})
        res = soup_list[-1]
        print("today 1$ in ₴ is:", res.text)
        print("okay... do you want see how many $ is... for example... 50₴? yeah? so print here amount of ₴:")
    cash = input()
    print("and...", cash, "equals:", cash // res.text)

elif choose == 2:
    response = requests.get("https://minfin.com.ua/ua/currency/eur/")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("span", {"class": "mfm-posr"})
        res = soup_list[-1]
        print("today 1€ in ₴ is:", res.text)
        print("okay... do you want see how many € is... for example... 50₴? yeah? so print here amount of ₴:")
    cash = input()
    print("and...", cash, "equals:", cash // res.text)

elif choose == 3:
    print("ещё раз такое увижу. забаню на гит хабе или где ты смотришь код?")
    exit(time.time(10))

elif choose == 4:
    response = requests.get("https://minfin.com.ua/ua/currency/gbp/")
    if response.status_code == 200:
        soup = BeatifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("span", {"class": "mfm-posr"})
        res = soup_list[-1]
        print("today 1£ in ₴ is:", res.text)
        print("okay... do you want see how many £ is... for example... 50₴? yeah? so print here amount of ₴:")
    cash = input()
    print("and...", cash, "equals:", cash // res.text)

elif choose == 5:
    response = requests.get("https://minfin.com.ua/ua/currency/jpy/")
    if response.status_code == 200:
        soup = BeatifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("span", {"class": "mfm-posr"})
        res = soup_list[-1]
        print("today 1¥ in ₴ is:", res.text)
        print("okay... do you want see how many ¥ is... for example... 50₴? yeah? so print here amount of ₴:")
    cash = input()
    print("and...", cash, "equals:", cash // res.text)

elif choose == 6:
    response = requests.get("https://minfin.com.ua/ua/currency/cny/")
    if response.status_code == 200:
        soup = BeatifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("span", {"class": "mfm-posr"})
        res = soup_list[-1]
        print("today 1¥ in ₴ is:", res.text)
        print("okay... do you want see how many ¥ is... for example... 50₴? yeah? so print here amount of ₴:")
    cash = input()
    print("and...", cash, "equals:", cash // res.text)

elif choose == 7:
    response = requests.get("https://minfin.com.ua/ua/currency/cad/")
    if response.status_code == 200:
        soup = BeatifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("span", {"class": "mfm-posr"})
        res = soup_list[-1]
        print("today 1C$ in ₴ is:", res.text)
        print("okay... do you want see how many C$ is... for example... 50₴? yeah? so print here amount of ₴:")
    cash = input()
    print("and...", cash, "equals:", cash // res.text)

elif choose == 8:
    response = requests.get("https://minfin.com.ua/ua/currency/pln/")
    if response.status_code == 200:
        soup = BeatifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("span", {"class": "mfm-posr"})
        res = soup_list[-1]
        print("today 1zł in ₴ is:", res.text)
        print("okay... do you want see how many zł is... for example... 50₴? yeah? so print here amount of ₴:")
    cash = input()
    print("and...", cash, "equals:", cash // res.text

elif choose == 9:
    response = requests.get("https://minfin.com.ua/ua/currency/byn/")
    if response.status_code == 200:
        soup = BeatifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("span", {"class": "mfm-posr"})
        res = soup_list[-1]
        print("today 1Br in ₴ is:", res.text)
        print("okay... do you want see how many Br is... for example... 50₴? yeah? so print here amount of ₴:")
    cash = input()
    print("and...", cash, "equals:", cash // res.text

elif choose == 10:
    response = requests.get("https://minfin.com.ua/ua/currency/byn/")
    if response.status_code == 200:
        soup = BeatifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("span", {"class": "mfm-posr"})
        res = soup_list[-1]
        print("today 1Ir in ₴ is:", res.text)
        print("okay... do you want see how many Ir is... for example... 50₴? yeah? so print here amount of ₴:")
    cash = input()
    print("and...", cash, "equals:", cash // res.text