import tkinter as tk
import tkinter.messagebox


def _hit11():
    mydc[entrY11.get()]=entrY12.get()
    entrY11.delete(0,"end")
    entrY12.delete(0,"end")
    



def _hit1():
    global entrY11,entrY12
    wiN1=tk.Toplevel(wiN)
    wiN1.title("新增/修改英文單字!!!")
    wiN1.geometry("500x400+650+350")
    lbL11 = tk.Label(wiN1,text="英文",fg="white",bg="green", font=("Arial", 16), width=30, height=2)
    lbL11.pack()
    entrY11=tk.Entry(wiN1,font=("Arial",20),bd=5)
    entrY11.pack()
    lbL12 = tk.Label(wiN1,text="中文",fg="white",bg="green", font=("Arial", 16), width=30, height=2)
    lbL12.pack()
    entrY12=tk.Entry(wiN1,font=("Arial",20),bd=5)
    entrY12.pack()

    btN11 = tk.Button(wiN1, text="新增/修改", font=("Arial", 24), width=10, height=2, command=_hit11)
    btN11.pack() 
    btN12 = tk.Button(wiN1, text="離開", font=("Arial", 24), width=10, height=2, command=wiN1.destroy)
    btN12.pack() 


def _hit21():
    if entrY21.get() in mydc:
        lbL23["text"]=mydc[entrY21.get()]
        lbL23["text"]="查詢成功囉!!"
    else:
        lbL23["text"]="沒有這個字啦，渾蛋!!"
    entrY21.delete(0,"end")


def _hit22():
    if entrY21.get() in mydc:
        del mydc[entrY21.get()]
        lbL23["text"]="刪除成功囉!!"
    else:
        lbL23["text"]="沒有這個字啦，渾蛋!!"
    entrY21.delete(0,"end")



def _hit2():
    global entrY21,lbL23
    wiN2=tk.Toplevel(wiN)
    wiN2.title("查詢/刪除英文單字!!!")
    wiN2.geometry("500x500+650+350")
    lbL21 = tk.Label(wiN2,text="英文",fg="white",bg="green", font=("Arial", 16), width=30, height=2)
    lbL21.pack()
    entrY21=tk.Entry(wiN2,font=("Arial",20),bd=5)
    entrY21.pack()
    lbL22 = tk.Label(wiN2,text="中文",fg="white",bg="green", font=("Arial", 16), width=30, height=2)
    lbL22.pack()
    lbL23 = tk.Label(wiN2,text="",fg="black",bg="yellow", font=("Arial", 16), width=30, height=2)
    lbL23.pack()

    btN21 = tk.Button(wiN2, text="查詢", font=("Arial", 24), width=10, height=2, command=_hit21)
    btN21.pack() 
    btN22 = tk.Button(wiN2, text="刪除", font=("Arial", 24), width=10, height=2, command=_hit22)
    btN22.pack() 
    btN23 = tk.Button(wiN2, text="離開", font=("Arial", 24), width=10, height=2, command=wiN2.destroy)
    btN23.pack() 

def _hit3():
    return
def _hit4():
    return
def _hit5():
    qQ=tk.messagebox.askokcancel("提示","確定要結束程式嗎???")
    if qQ:
        wiN.destroy()




mydc={}

wiN = tk.Tk()

wiN.title("歡迎使用自製英文字典!!!")

wiN.geometry("600x450+650+350")
wiN.resizable(width=False, height=False)

btN1 = tk.Button(wiN, text="新增/修改單字", font=("Arial", 20), width=20, height=2, command=_hit1,bg="blue",fg="white")
btN2 = tk.Button(wiN, text="查詢/刪除單字", font=("Arial", 20), width=20, height=2, command=_hit2,bg="blue",fg="white")
btN3 = tk.Button(wiN, text="顯示所有單字", font=("Arial", 20), width=20, height=2, command=_hit3,bg="blue",fg="white")
btN4 = tk.Button(wiN, text="英文測驗", font=("Arial", 20), width=20, height=2, command=_hit4,bg="orange",fg="white")
btN5 = tk.Button(wiN, text="結束程式", font=("Arial", 20), width=20, height=2, command=_hit5,bg="red",fg="white")

btN1.pack() 
btN2.pack() 
btN3.pack() 
btN4.pack() 
btN5.pack() 

wiN.mainloop()

