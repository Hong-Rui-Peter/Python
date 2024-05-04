# -*- coding: utf-8 -*-
"""簡單線性迴歸_01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YebbWCOLgPibGOLtag8WLXmrMr7DAV7u
"""

#作業:
#簡單線性迴歸 (Simple Linear Regression): 由現有的資料建立一條線, 從這條線可以看出資料的相關性, 而獲得對未來發展的預測。
#適合：預測, 資料之間的變項有相關性

# 85度C: 蒐集氣溫與店營業額的資料
# 氣溫：29, 28, 34, 31, 25, 29, 32, 31, 24, 33, 25, 31, 26, 30
# 營業額 (單位千元)：7.7, 6.2, 9.3, 8.4, 5.9, 6.4, 8.0, 7.5, 5.8, 9.1, 5.1, 7.3, 6.5, 8.4

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

temp = np.array([29, 28, 34, 31, 25, 29, 32, 31, 24, 33, 25, 31, 26, 30])
income = np.array([7.7, 6.2, 9.3, 8.4, 5.9, 6.4, 8.0, 7.5, 5.8, 9.1, 5.1, 7.3, 6.5, 8.4])
# data (X)-> label (target 答案 y)
X = pd.DataFrame(temp, columns=['氣溫'])
target = pd.DataFrame(income, columns=['營業額'])
y = target['營業額']

lm = LinearRegression()
lm.fit(X, y)
print('迴歸係數: ', lm.coef_)
print('截距: ', lm.intercept_)
# y = 0.37X - 3.636

# 預測氣溫 11, 30 度營業營應該是多少?
new_temp = pd.DataFrame(np.array([12, 30]), columns=['氣溫'])
pred = lm.predict(new_temp)
print(pred)
# 5分鐘練習, 7:40

#繪圖表示
#第一節課休息, 7:50 繼續
import matplotlib.pyplot as plt
plt.scatter(temp, income)
ra = lm.predict(X)
plt.plot(temp, ra, color='blue')
plt.plot(new_temp['氣溫'], pred, color='red', marker='o', markersize=10)
plt.title('An AI model predict Income')
#5分鐘練習, 8:05