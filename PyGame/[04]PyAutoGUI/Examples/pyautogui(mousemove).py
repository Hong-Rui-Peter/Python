'''
PyAutoGUI--moveTo、moveRel
'''
import pyautogui

xx=500
yy=300
ss=2

#移動到絕對位置
print(pyautogui.position())
pyautogui.moveTo(xx,yy,ss)
print(pyautogui.position())


#移動到相對位置
print(pyautogui.position())
pyautogui.moveRel(xx,yy,ss)
print(pyautogui.position())

