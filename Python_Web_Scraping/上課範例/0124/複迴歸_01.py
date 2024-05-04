# -*- coding: utf-8 -*-
"""複迴歸_01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c2wnR7F_FcFXVDRkElB3MmEzVFTILRbJ
"""

# 運用獲得的資料 -> AI -> 資料分析, 或是建立模型去協助人類預測或是回答問題
# AI: 機器學習 (ML, Machine Learning); 類神經網路 (NN, Neuro Network)
# ML: 單純線性迴歸 (Smiple Liner Regression) y = ax + b
# 多元線性迴歸: y = a1x1 + a2x2 + a3x3 +..... + b
# 波士頓房價
# CRIM 城鎮犯罪率; ZN 住宅用地超過 700 坪; INDUS 非商業用地比例; NOX; CHAS 河; RM 房間數; AGE: 房齡; DIS 就業中心距離, RAD, TAX, PTRATIO B
# LSTAT -> 房價

from sklearn import datasets
#data = datasets.load_boston().data

import pandas as pd
import numpy as np

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

#5分鐘時間完成到這個部分: 7:02
#資料切割: 80% 模型的訓練; 20% 驗證模型的準確性
from sklearn.model_selection import train_test_split
data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.2)
print(data_train.shape)
print(data_test.shape)
print(target_train.shape)
#3分鐘練習, 7:14

#建立一個多元線性迴歸的預測模型
from sklearn.linear_model import LinearRegression
regr_model = LinearRegression()
regr_model.fit(data_train, target_train)
#3分鐘完成, 訓練模型 7:23

pre = regr_model.predict(data_test)
print(pre.round(1))
print(target_test)

#模型的評估方法
#3分鐘練習, 第一節課10分鐘休息 7: 40 繼續

#模型評估方法 1：決定係數 (迴歸)
print(regr_model.score(data_train, target_train).round(3))
# 0 <> 1, 至少大於 0.7, 0.999
print(regr_model.score(data_test, target_test).round(3))
# Overfitting
#0.734
#0.751
# 3 分鐘練習, 7:51

#模型評估方法 2：圖形:殘差圖 (residual plot)
import matplotlib.pyplot as plt
x = np.arange(pre.size)
y = x*0
plt.scatter(x, pre - target_test)
plt.plot(x, y, color='orange') # 劃出 y= 0 的基礎線
plt.show()
#5分鐘練習, 8:04

#模型評估方法 3：平均絕對誤差 (MAE, mean absolute error)
from sklearn.metrics import mean_absolute_error
print(mean_absolute_error(target_test, pre).round(2))
#3分鐘練習, 8:11