import requests
from bs4 import BeautifulSoup

url = "https://www.taiwanlottery.com.tw/index_new.aspx"
html = requests.get(url)
sp = BeautifulSoup(html.text, "html.parser")  # 拆解格式
sp.title
datas = sp.find("div", class_="contents_box02")  # 找到的第1筆
print(
    datas.find("div", class_="contents_mine_tx02")
    .find("span", class_="font_black15")
    .text
)
nums = datas.find_all("div", class_="ball_tx ball_green")
# nums
print("開出順序: ")

for i in range(0, 6):
    print(nums[i].text, end=" ")

print("\n大小順序: ")

for i in range(6, 12):
    print(nums[i].text, end=" ")

print("\n特別號: ", datas.find("div", class_="ball_red").text)
