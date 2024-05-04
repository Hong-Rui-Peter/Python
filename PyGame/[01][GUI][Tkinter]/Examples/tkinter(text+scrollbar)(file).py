'''
tkinter示範程式--text+scrollbar+openfile+savefile的應用
'''
import tkinter as tk
from tkinter import filedialog

def _hit1():
    fname = filedialog.askopenfilename(title="開啟文件")
    if fname !="":
        filE=open(fname,"r",encoding="utf-8")
        stR=filE.read()
        filE.close()
        texT.insert(tk.END, stR)
        
    
def _hit2():
    fname = filedialog.asksaveasfilename(title="保存文件")
    if fname !="":
        filE=open(fname,"w",encoding="utf-8")
        filE.write(texT.get(1.0,tk.END))
        filE.close()



wiN = tk.Tk()
wiN.title("Welcome!!!")
wiN.geometry("600x500")


btN1 = tk.Button(wiN, text="開檔!!",fg="green", font=("Arial", 16), width=10, height=2, command=_hit1)
btN1.pack() 
btN2 = tk.Button(wiN, text="存檔!!",fg="blue", font=("Arial", 16), width=10, height=2, command=_hit2)
btN2.pack() 

sBar=tk.Scrollbar(wiN)
sBar.pack(side=tk.RIGHT,fill=tk.Y)

texT=tk.Text(wiN, font=("Arial", 20),yscrollcommand=sBar.set)
texT.pack(side=tk.BOTTOM, fill=tk.BOTH)
sBar.config(command=texT.yview)

wiN.mainloop()

