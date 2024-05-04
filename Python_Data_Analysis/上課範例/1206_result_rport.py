# -*- coding: utf-8 -*-
"""Result_Rport.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mSgDKxy_yGlQzFwYZd-rd--p_ERVnPoT
"""

# 我的成果報告 學生:林青霞
# 1.1 Machine Learing (ML): Climate data, Regressin, KNN, Logistic
# 1.2 CNN, Gradio
# 1.3 Self improvement
# 2. Python, Colab, Comment 註解說明
# 3. Code 程式語言
# 4. Result 成果

!pip install gradio

import gradio as gr

# 寫一個測試的 function 搭配使用 gradio
def bmi_cal(h, w):
  h = float(h)/100
  w = float(w)
  bmi = w/(h**2)
  message = f"Your BMI is {bmi:.2f}."
  return message

# 呼叫測試
bmi_cal(178, 78)

iface = gr.Interface(bmi_cal,
                     inputs=["number","number"],
                     outputs="text")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.utils import to_categorical #1,2,3,4
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train.shape

y_train.shape

x_test.shape

n = 9455
x_train[n]
print(y_train[n])
plt.imshow(x_train[n], cmap='Greys')

x_train = x_train.reshape(60000, 784)/255
x_test = x_test.reshape(10000, 784)/255
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

model = Sequential()
model.add(Dense(100, input_dim=784, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(loss='mse', optimizer=SGD(learning_rate=0.087), metrics=['accuracy'])

model.summary() #rest time 8:20

model.fit(x_train, y_train, batch_size=100, epochs=20)

x_test[5].shape

inp = x_test[5].reshape(1, 784)

model.predict(inp)

y_predict = np.argmax(model.predict(x_test), axis=-1)

n = 20
print('the predict number is:', y_predict[n])
plt.imshow(x_test[n].reshape(28,28), cmap='Greys');

from ipywidgets import interact_manual

def test(no):
  plt.imshow(x_test[no].reshape(28, 28), cmap='Greys')
  print("My CNN model say the number is:", y_predict[no])

interact_manual(test, no=(0, 9999))

score = model.evaluate(x_test, y_test)

print('loss:', score[0])
print('accu: ', score[1])

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd '/content/drive/My Drive/Colab Notebooks'

model.save('my_dnn_model')