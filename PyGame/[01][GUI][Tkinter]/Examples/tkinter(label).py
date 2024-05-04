'''
tkinter示範程式--label的應用
'''
#1.載入tkinter
import tkinter as tk

#2.使用tkinter建立一個叫做[wiN]的視窗
wiN = tk.Tk()

#3.設定視窗[標題]
wiN.title("Welcome!!!")

#4.設定視窗[大小]
wiN.geometry("800x600")

#5.建立一個叫做[lbL]的[label]物件,並做相關屬性設定
lbL = tk.Label(wiN,text="Hello!! Nice to see you!!",fg="white",bg="green", font=("Arial", 16), width=50, height=3)

#6.放置標籤(設定顯示位置)，預設為TOP
lbL.pack()

#7.顯示視窗
wiN.mainloop()

