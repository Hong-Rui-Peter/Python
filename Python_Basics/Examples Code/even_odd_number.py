# 判斷奇偶數

def even_odd_number(num):
    if num % 2 == 0:
        print(f"{num}是偶數")
    else:
        print(f"{num}是奇數")


even_odd_number(int(input("請輸入整數:")))