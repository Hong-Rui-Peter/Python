'''
PyAutoGUI--screenshot
'''
import pyautogui

screen=pyautogui.screenshot()

print(type(screen))

screen.save("screen.jpg")

screen.show()














