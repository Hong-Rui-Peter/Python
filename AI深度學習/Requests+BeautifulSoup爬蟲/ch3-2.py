import requests

url = "https://www.math.thu.edu.tw/"
html = requests.get(url)
html.encoding = "utf-8"
htmllist = html.text.splitlines()
print(htmllist)

n = 0
for row in htmllist:
    if "師資" in row:
        n += 1
    print("出現{}次!".format(n))
