'''
PyAutoGUI--PAUSE
'''
import pyautogui

#在每次調用PyAutoGUI的函數後設置2.5秒的暫停：

pyautogui.PAUSE=2.5

#為了防止程序出問題，當鼠標移動到屏幕左上角，會引發pyautogui.FailSafeException錯誤進而中止程序。關閉命令如下（不建議關閉）：

pyautogui.FAILSAFE=False
