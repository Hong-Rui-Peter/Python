'''
幾A幾B遊戲大進擊!!!
'''
import tkinter as tk
import tkinter.messagebox
import random

kk=3

ans=random.sample("0123456789", kk)

cc=1

def _restart():
    wiN.title("幾A幾B遊戲大進擊---"+str(kk)+"個數字!!!")
    listBox.delete(0,tk.END)

def _hit1():
    global cc,kk,ans
    aa=bb=0
    for ii in range(kk):
        if enteR.get()[ii]==ans[ii]:
            aa=aa+1
        elif enteR.get()[ii] in ans:
            bb=bb+1
    listBox.insert(tk.END, str(cc)+"."+enteR.get()+"----"+str(aa)+"A"+str(bb)+"B")
    if aa==kk:
        listBox.insert(tk.END,"恭喜破關!!!")
        kk=kk+1
        ans=random.sample("0123456789", kk)
        cc=0
        wiN.after(3000,_restart)
        
    enteR.delete(0,tk.END)
    cc=cc+1

    
def _hit2():
    qQ=tk.messagebox.askokcancel("提示","確定要結束程式嗎???")
    if qQ:
        wiN.destroy()


wiN = tk.Tk()
wiN.title("幾A幾B遊戲大進擊---"+str(kk)+"個數字!!!")
wiN.configure(bg="darkgray")
wiN.geometry("600x500+350+50")

enteR=tk.Entry(wiN,font=("Arial",16),bd=5,bg="yellow")
enteR.pack() 

btN1 = tk.Button(wiN, text="猜猜看!!",bg="black",fg="white", font=("Arial", 16), width=10, height=2, command=_hit1)
btN1.pack() 
btN2 = tk.Button(wiN, text="離開!!",bg="black",fg="white", font=("Arial", 16), width=10, height=2, command=_hit2)
btN2.pack() 

sBar=tk.Scrollbar(wiN)
sBar.pack(side=tk.RIGHT,fill=tk.Y)

listBox=tk.Listbox(wiN, font=("Arial", 20),yscrollcommand=sBar.set,bg="black",fg="white")
listBox.pack(side=tk.BOTTOM, fill=tk.BOTH)
sBar.config(command=listBox.yview)

wiN.mainloop()

