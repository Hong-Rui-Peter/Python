from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.google.com/")
if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())
