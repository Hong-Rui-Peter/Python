'''
TQC+ 程式語言Python 302 迴圈偶數連加

1. 題目說明:
請開啟PYD302.py檔案，依下列題意進行作答，依輸入值計算偶數的總和，使輸出值符合題意要求。作答完成請另存新檔為PYA302.py再進行評分。

2. 設計說明：
請使用迴圈敘述撰寫一程式，讓使用者輸入兩個正整數a、b（a < b），利用迴圈計算從a開始的偶數連加到b的總和。例如：輸入a=1、b=100，則輸出結果為2550（2 + 4 + … + 100 = 2550）。

3. 輸入輸出：
輸入說明
兩個正整數（a、b，且a < b）

輸出說明
計算從a開始的偶數連加到b的總和

範例輸入
14
1144
範例輸出
327714
'''
a = eval(input())
b = eval(input())
sum = 0
for n in range(a, b + 1):
    if n % 2 == 0:
        sum += n
print(sum)