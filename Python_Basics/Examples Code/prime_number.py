"""
找出 1 到 n 之間的質數


參考資料:
[1] 神奇的質數
http://epaper.gotop.com.tw/pdf/ACL047800.pdf


規則: 
無法被 1 和 自已 以外的數字整除 (整除代表餘數為 0)，即為質數


例如 1 ~ 1000 以內的質數:
2   3   5   7  11  13  17  19  23  29 31  37  41  43  47  53  59  61  67 
71 73  79  83  89  97 101 103 107 109 113 127 131 137 139 149 151 
157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 
241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 
347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 
439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 
547 557 563 569 571 577 587 593 599 601 607 613 617 619 631 641 
643 647 653 659 661 673 677 683 691 701 709 719 727 733 739 743 
751 757 761 769 773 787 797 809 811 821 823 827 829 839 853 857 
859 863 877 881 883 887 907 911 919 929 937 941 947 953 967 971 
977 983 991 997
"""

# 放置質數的列表變數
list_prime_number = []

# 初始狀態，用來判斷是否為質數 (先假設處理的數字為質數)
isPrimeNumber = True

# 數字範別 (1 到 自訂的 num)
num = 100

# 每次執行一個 i，內部的 j 都會執行完一次迴圈
for i in range(2, num + 1):

    # i 都會跟 2 ~ i 之間的值相除
    for j in range(2, i):

        # 只要 i 被 j 整除，例如 4(i) % 2(j) == 0，代表 i 不是質數
        if i % j == 0:

            # 修改狀態為「非質數」
            isPrimeNumber = False

            # 確認非質數，則直接跳出迴圈，不用將 j 整個比對過一輪，增加效率
            break

    # 計算過程中，isPrimeNumber 沒有被改為 False，代表 i 沒有被 j 整除，i 是質數
    if isPrimeNumber == True:

        # 將 i 加入質數列表
        list_prime_number.append(i)

    # 改回原先的狀態，方便下一次判斷
    isPrimeNumber = True

# 檢視質數列表，例如 [2, 3, 5, 7]
print(list_prime_number)
