# 氣泡排序法


def sort(n):
    for i in range(0, len(n) - 1):
        for j in range(0, len(n) - 1):
            if int(n[j]) > int(n[j + 1]):  # 如果前大於後
                # 前後交換
                temp = n[j + 1]
                n[j + 1] = n[j]
                n[j] = temp
    print(n)


sort(input("請輸入整數陣列:").split())
