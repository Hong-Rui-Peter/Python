# -*- coding: utf-8 -*-
"""1115 課程2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D43oExrFXsA8yfL_y4G6DkBtM9feO9zZ
"""

# Stardard Function
# OS -> Operting System
# Windows 11, 10, 7, XP; MacOS (UNIX); Linux (PC, Androi)

import os
os.system('ls')
print(os.getenv('COMPUTERNAME'))

import pprint
print('Out of function, show global var: ', globals())
print('Out of function, hsow local var: ', locals())
def add(x, y):
  sum = x + y
  print('Inside of function, show global var:')
  pprint.pprint(globals())
  print('Inside of function, show local var:')
  pprint.pprint(locals())
  return sum

ans = add(5, 3)

#iter -> interation
import itertools
nums = itertools.count(100, 1)
for i in range(100):
  num = nums.__next__()
  print(num)

bs = [1, 2, 3, 4]
cy = itertools.repeat(bs)
for j in range(10):
  cyn = cy.__next__()
  print(cyn)

s = itertools.chain('Py', 'thon')
print(list(s))

# enumerate , zip
days = ['Monday', 'Tuesday', 'Wednesday', 'Thusday', 'Friday', 'Saturday']
p = enumerate(days, start=2)
for c, day in p:
  print(c, '. ', day)

do = ['Happy', 'Run', 'Bike', 'Baseball', 'Football', 'Fish', 'Sleep', 'Montain']
week = zip(days, do)
for day, sport in week:
  print(day, sport)

#time
from datetime import datetime, date
now = date.today()
print(now)

now = datetime.now()
print(now)

print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second, now.microsecond)