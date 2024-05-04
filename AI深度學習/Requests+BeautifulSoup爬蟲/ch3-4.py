import requests

# url = "https://www.momoshop.com.tw/main/Main.jsp"
url = "https://translate.google.com/?hl=zh-TW&tab=TT"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    "AppleWebKit/537.36 (KHTML, like Gecko)"
    "Chrome/63.0.3239.132 Safari/537.36"
}

html = requests.get(url)
html.encoding = "utf-8"
print(html.status_code)
