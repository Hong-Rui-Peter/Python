# ptrhon爬蟲範例
import requests

param = {
    "date": "20230601",
    "stockNo": "2330",
    "response": "csv",
}  # GET時要帶的參數(token)
url = "https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY"  # 台積電股票網址
r = requests.get(url, param)

# 將爬到的資料寫入crawler_test.txt存在路徑C:\Users\hongr\OneDrive\桌面:
with open(
    r"C:/Users/hongr/OneDrive/桌面/Programming Language/Python/Python_Basics/Examples Code/crawler/crawler_test.txt",
    "w+",
) as f:
    f.write(r.text)
