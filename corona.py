import config
from bs4 import BeautifulSoup
import requests

# this file scrapes for the cases and deaths in the uk

page = requests.get('https://www.worldometers.info/coronavirus/country/uk/')
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

info = soup.find_all(class_='maincounter-number')


def get_cases():
    cases = info[0].get_text()
    tc = cases.split("\n")
    totalCases = tc[1]
    return totalCases


def get_deaths():
    deaths = info[1].get_text()
    td = deaths.split("\n")
    totalDeaths = td[1]
    return totalDeaths
