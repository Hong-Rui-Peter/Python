'''
tkinter示範程式--listbox的應用
'''
import tkinter as tk


def _hit1():
    listBox.insert(tk.END, enteR.get())
    enteR.delete(0,tk.END)
def _hit2():
    listBox.delete(0,tk.END)


wiN = tk.Tk()
wiN.title("Welcome!!!")
wiN.geometry("600x500")

enteR=tk.Entry(wiN,font=("Arial",16),bd=5)
enteR.pack() 

btN1 = tk.Button(wiN, text="加入!!",fg="green", font=("Arial", 16), width=10, height=2, command=_hit1)
btN1.pack() 
btN2 = tk.Button(wiN, text="清除!!",fg="blue", font=("Arial", 16), width=10, height=2, command=_hit2)
btN2.pack() 

listBox=tk.Listbox(wiN, font=("Arial", 20), width=40)
listBox.pack(side=tk.BOTTOM)


wiN.mainloop()

