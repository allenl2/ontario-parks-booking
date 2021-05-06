#from bs4 import BeautifulSoup
import requests

URL = 'https://reservations.ontarioparks.com/'
page = requests.get(URL)

print(page.headers)
