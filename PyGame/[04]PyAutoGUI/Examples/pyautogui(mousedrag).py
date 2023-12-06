'''
PyAutoGUI--dragTo、dragRel
'''
import pyautogui

xx=300
yy=150
ss=2

pyautogui.moveTo(100,150,ss)


#拖曳到絕對位置
print(pyautogui.position())
pyautogui.dragTo(xx,yy,ss)
print(pyautogui.position())


#拖曳到相對位置
print(pyautogui.position())
pyautogui.dragRel(xx,yy,ss)
print(pyautogui.position())

