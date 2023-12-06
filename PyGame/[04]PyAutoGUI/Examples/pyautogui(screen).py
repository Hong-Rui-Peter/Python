'''
PyAutoGUI--size、onScreen、position
'''
import pyautogui

#取得螢幕大小
sw,sh=pyautogui.size()
print(sw,sh)

#判斷某個座標是否在螢幕上

print(pyautogui.onScreen(100,100))
print(pyautogui.onScreen(2000,2000))

#取得滑鼠目前位置
mx,my=pyautogui.position()
print(mx,my)

