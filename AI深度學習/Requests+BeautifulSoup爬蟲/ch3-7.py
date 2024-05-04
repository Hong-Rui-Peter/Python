import requests
from bs4 import BeautifulSoup

google_url = "https://www.google.com.tw/search"
my_params = {"q": "開學"}
r = requests.get(google_url, params=my_params)

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, "html.parser")
    print(soup.prettify())
    items = soup.select('div.kCrYT > a[href^="/url"]')
    for i in items:
        print("標題:" + i.text)
        print("網址:" + i.get("href"))
