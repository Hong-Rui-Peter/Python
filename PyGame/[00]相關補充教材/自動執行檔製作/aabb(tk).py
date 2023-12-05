'''
tkinter示範程式--listbox+scrollbar的應用
'''
import tkinter as tk
import random
import tkinter.messagebox

def _gg():
    ans=set()
    while True:
        ans.add(random.randint(0,9))
        if len(ans)==4:
            break
    return list(ans)


def _hit1():
    global cc
    aa=0
    bb=0
    nn=enteR.get()
    for ii in range(4):
        if int(nn[ii])==anss[ii] :
            aa=aa+1
        elif int(nn[ii]) in anss:
            bb=bb+1
    ss=str(cc)+"."+str(aa)+"A"+str(bb)+"B"  
    listBox.insert(tk.END, ss)
    if aa==4:
        listBox.insert(tk.END, "沒看過這種天才!!啊!!")
    cc=cc+1
    enteR.delete(0,tk.END)
    
def _hit2():
    global cc,anss
    cc=1
    anss=_gg()  
    listBox.delete(0,tk.END)
    
def _hit3():
    qQ=tk.messagebox.askokcancel("提示","確定要結束程式嗎???")
    if qQ:
        wiN.destroy()
    


wiN = tk.Tk()
wiN.title("Welcome!!!")
wiN.geometry("600x500")

enteR=tk.Entry(wiN,font=("Arial",16),bd=5)
enteR.pack() 

btN1 = tk.Button(wiN, text="猜猜看!!",fg="green", font=("Arial", 16), width=10, height=1, command=_hit1)
btN1.pack() 
btN2 = tk.Button(wiN, text="重玩一遍!!",fg="blue", font=("Arial", 16), width=10, height=1, command=_hit2)
btN2.pack() 
btN3 = tk.Button(wiN, text="離開!!",fg="blue", font=("Arial", 16), width=10, height=1, command=_hit3)
btN3.pack() 

sBar=tk.Scrollbar(wiN)
sBar.pack(side=tk.RIGHT,fill=tk.Y)

listBox=tk.Listbox(wiN, font=("Arial", 20),yscrollcommand=sBar.set)
listBox.pack(side=tk.BOTTOM, fill=tk.BOTH)
sBar.config(command=listBox.yview)

cc=1
anss=_gg()  



wiN.mainloop()

