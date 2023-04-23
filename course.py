import requests
from bs4 import BeautifulSoup


def get_course(valute: str):
    volutes = xml.find_all("Valute")
    for volute in volutes:
        if volute.CharCode.text == valute.upper():
            return volute.Value.text
    return 'Курс не найден!'


url = "http://www.cbr.ru/scripts/XML_daily.asp?"
response = requests.get(url)
xml = BeautifulSoup(response.content, "xml")
