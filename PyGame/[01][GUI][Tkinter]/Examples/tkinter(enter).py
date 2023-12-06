'''
tkinter示範程式--enter的應用
'''
def _hit():
    wiN.title(enteR.get())

import tkinter as tk

wiN = tk.Tk()

wiN.title("Welcome!!!")

wiN.geometry("600x300")

lbL = tk.Label(wiN,text="請輸入你的遺言: ",fg="white",bg="green", font=("Arial", 16), width=15, height=2)
lbL.pack(side=tk.LEFT)

enteR=tk.Entry(wiN,font=("Arial",16),bd=5)
#enteR=tk.Entry(wiN,font=("Arial",16),bd=5,show="?")
enteR.pack(side=tk.LEFT)

btN = tk.Button(wiN, text="送出!!", font=("Arial", 16), width=10, height=2, command=_hit)
btN.pack(side=tk.BOTTOM) 

wiN.mainloop()

