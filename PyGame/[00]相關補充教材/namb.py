'''
tkinter示範程式--listbox+scrollbar的應用
'''
import tkinter as tk
import random

ans=random.sample("0123456789", 4)

cc=1


def _hit1():
    global cc
    aa=bb=0
    for ii in range(4):
        if enteR.get()[ii]==ans[ii]:
            aa=aa+1
        elif enteR.get()[ii] in ans:
            bb=bb+1
    listBox.insert(tk.END, str(cc)+"."+enteR.get()+"----"+str(aa)+"A"+str(bb)+"B")
    if aa==4:
        listBox.insert(tk.END,"恭喜老爺!!賀喜夫人!!您猜對啦!!!")
        
    enteR.delete(0,tk.END)
    cc=cc+1

def _hit2():
    global ans,cc
    ans=random.sample("0123456789", 4)
    cc=1
    listBox.delete(0,tk.END)


    
def _hit3():
    qQ=tk.messagebox.askokcancel("提示","確定要結束程式嗎???")
    if qQ:
        wiN.destroy()


wiN = tk.Tk()
wiN.title("幾A幾B遊戲大進擊!!!")
wiN.configure(bg="darkgray")
wiN.geometry("600x500+350+50")

enteR=tk.Entry(wiN,font=("Arial",16),bd=5,bg="yellow")
enteR.pack() 

btN1 = tk.Button(wiN, text="猜猜看!!",bg="black",fg="white", font=("Arial", 16), width=10, height=2, command=_hit1)
btN1.pack() 
btN2 = tk.Button(wiN, text="再玩一次!!",bg="black",fg="white", font=("Arial", 16), width=10, height=2, command=_hit2)
btN2.pack() 
btN3 = tk.Button(wiN, text="離開!!",bg="black",fg="white", font=("Arial", 16), width=10, height=2, command=_hit3)
btN3.pack() 

sBar=tk.Scrollbar(wiN)
sBar.pack(side=tk.RIGHT,fill=tk.Y)

listBox=tk.Listbox(wiN, font=("Arial", 20),yscrollcommand=sBar.set,bg="black",fg="white")
listBox.pack(side=tk.BOTTOM, fill=tk.BOTH)
sBar.config(command=listBox.yview)

wiN.mainloop()

