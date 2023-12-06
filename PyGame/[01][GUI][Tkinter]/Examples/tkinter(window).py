'''
tkinter示範程式--基本視窗的應用
'''
#1.載入tkinter
import tkinter as tk

#2.使用tkinter建立一個叫做[wiN]的視窗
wiN = tk.Tk()

#3.設定視窗[標題]
wiN.title("Welcome!!!")

#4.設定視窗[大小]
wiN.geometry("600x400")

#設定視窗顯示位置的方法:100是X軸，200是Y軸
#wiN.geometry("400x300+100+200")

#設定視窗最大化的作法
#wiN.geometry(str(wiN.winfo_screenwidth())+"x"+str(wiN.winfo_screenheight()))

#固定視窗大小的作法
#wiN.resizable(width=False, height=False)

#5.顯示視窗
wiN.mainloop()

