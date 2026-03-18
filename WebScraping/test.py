from bs4 import BeautifulSoup
import requests

URL = "https://www.w3schools.com/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

print(soup)