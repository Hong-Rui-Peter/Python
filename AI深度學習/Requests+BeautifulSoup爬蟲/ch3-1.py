import requests

url = "https://www.math.thu.edu.tw/"
html = requests.get(url)
html.encoding = "utf-8"
print(html.text)
