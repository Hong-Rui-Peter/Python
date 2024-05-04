'''
tkinter示範程式--button+messagebox的應用
'''
def _hit1():
    tk.messagebox.showinfo("提示","多言必失!!!")
    
def _hit2():
    tk.messagebox.showwarning("警告","大雨特報!!!")

def _hit3():
    tk.messagebox.showerror("錯誤","電腦即將爆炸!!!")

def _hit4():
    qQ=tk.messagebox.askokcancel("提示","確定要結束程式嗎???")
    if qQ:
        wiN.destroy()
    

#1.載入tkinter
import tkinter as tk

#2.使用tkinter建立一個叫做[wiN]的視窗
wiN = tk.Tk()

#3.設定視窗[標題]
wiN.title("Welcome!!!")

#4.設定視窗[大小]
wiN.geometry("800x600")

#5.建立[button]物件,並做相關屬性設定
btN1 = tk.Button(wiN, text="提示訊息",bg="blue", font=("Arial", 16), width=15, height=3, command=_hit1)
btN2 = tk.Button(wiN, text="警告訊息",bg="yellow", font=("Arial", 16), width=15, height=3, command=_hit2)
btN3 = tk.Button(wiN, text="錯誤訊息",bg="red", font=("Arial", 16), width=15, height=3, command=_hit3)
btN4 = tk.Button(wiN, text="結束程式",bg="green", font=("Arial", 16), width=15, height=3, command=_hit4)

#6.放置按鈕(設定顯示位置)
btN1.pack()
btN2.pack(side=tk.LEFT)
btN3.pack(side=tk.RIGHT)
btN4.pack(side=tk.BOTTOM)

#7.顯示視窗
wiN.mainloop()

