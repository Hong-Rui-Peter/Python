'''
?A?B大挑戰
'''
import tkinter as tk
import random

def _hit1():
    global cc,nn,answer
    aa=0
    bb=0
    qq=list(enteR.get())
    for ii in range(nn):
        if qq[ii]==answer[ii]:
            aa=aa+1
        elif qq[ii] in answer:
            bb=bb+1
    
    listBox.insert(0, str(cc)+"."+enteR.get()+"--"+str(aa)+"A"+str(bb)+"B")
    enteR.delete(0,tk.END)
    cc=cc+1
    if aa==nn:
        listBox.insert(0,"恭喜老爺!!賀喜夫人!!您猜對啦!!!")

        
    
def _hit2():
    global cc,answer,nn
    listBox.delete(0,tk.END)
    nn=nn+1
    answer=random.sample("0123456789", nn)
    cc=1
    wiN.title("?A?B大挑戰---"+str(nn)+"個數字!!!")


def _hit3():
    qQ=tk.messagebox.askokcancel("提示","確定要結束程式嗎???")
    if qQ:
        wiN.destroy()

nn=3
answer=random.sample("0123456789", nn)
cc=1
wiN = tk.Tk()
wiN.title("?A?B大挑戰---"+str(nn)+"個數字!!!")
wiN.geometry("600x500+300+100")
wiN.resizable(width=False, height=False)
wiN.configure(bg="black")

enteR=tk.Entry(wiN,font=("Arial",16),bd=5)
enteR.pack() 

btN1 = tk.Button(wiN, text="我猜!!",fg="yellow",bg="green", font=("Arial", 16), width=10, height=1, command=_hit1)
btN1.pack() 
btN2 = tk.Button(wiN, text="繼續挑戰!!",fg="yellow",bg="blue", font=("Arial", 16), width=10, height=1, command=_hit2)
btN2.pack() 
btN3 = tk.Button(wiN, text="離開!!",fg="yellow",bg="red", font=("Arial", 16), width=10, height=1, command=_hit3)
btN3.pack() 

sBar=tk.Scrollbar(wiN)
sBar.pack(side=tk.RIGHT,fill=tk.Y)

listBox=tk.Listbox(wiN, font=("標楷體", 24),yscrollcommand=sBar.set,bg="gray",fg="white",height=50)
listBox.pack(side=tk.BOTTOM, fill=tk.BOTH)
sBar.config(command=listBox.yview)

wiN.mainloop()

