'''
PyAutoGUI--rightclick、middleclick、leftclick、doubleclick
'''
import pyautogui

xx=100
yy=150


#按右鍵
pyautogui.rightClick(x=xx,y=yy,interval=2)
#按左鍵
pyautogui.leftClick(xx,yy,2)
#連續按左鍵兩次
pyautogui.doubleClick(xx,yy+200,2)
#按中鍵
pyautogui.middleClick(xx+200,yy)



