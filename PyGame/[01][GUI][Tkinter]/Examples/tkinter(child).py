'''
tkinter示範程式--子視窗的應用
'''
def _hit():
    wiN1=tk.Toplevel(wiN)
    wiN1.title("Hello!!!")
    wiN1.geometry("400x300")
    btN1 = tk.Button(wiN1, text="say 88", font=("Arial", 12), width=10, height=2, command=wiN1.destroy)
    btN1.pack() 


#1.載入tkinter
import tkinter as tk

#2.使用tkinter建立一個叫做[wiN]的視窗
wiN = tk.Tk()

#3.設定視窗[標題]
wiN.title("Welcome!!!")

#4.設定視窗[大小]
wiN.geometry("600x400")

#5.建立一個叫做[btN]的[button]物件,並做相關屬性設定
btN = tk.Button(wiN, text="hit me", font=("Arial", 12), width=10, height=2, command=_hit)

#6.放置按鈕(設定顯示位置)
btN.pack() 

#7.顯示視窗
wiN.mainloop()

