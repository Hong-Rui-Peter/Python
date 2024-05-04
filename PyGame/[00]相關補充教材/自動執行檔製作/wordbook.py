'''
林照陽的自製英文字典
'''
def _hit1():
    myDict[entrY1.get()]=entrY2.get()
    entrY1.delete(0,tk.END)
    entrY2.delete(0,tk.END)


def _hit2():
    wiN1=tk.Toplevel(wiN)
    wiN1.title("Hello!!!")
    wiN1.geometry("400x600")
    btN1 = tk.Button(wiN1, text="回主選單", font=("Arial", 12), width=10, height=2, command=wiN1.destroy)
    btN1.pack() 
    sBar=tk.Scrollbar(wiN1)
    sBar.pack(side=tk.RIGHT,fill=tk.Y)
    
    listBox=tk.Listbox(wiN1, font=("Arial", 20),yscrollcommand=sBar.set,height=50,bg="lime")
    listBox.pack(side=tk.BOTTOM, fill=tk.BOTH)
    sBar.config(command=listBox.yview)
    
    for ii in myDict.items():
        listBox.insert(tk.END, str(ii))



import tkinter as tk


myDict=dict()

wiN = tk.Tk()

wiN.title("Welcome!!!")

wiN.geometry("600x300")

lbL1 = tk.Label(wiN,text="請輸入英文",fg="white",bg="green", font=("Arial", 16), width=15, height=2)
lbL1.pack()

entrY1=tk.Entry(wiN,font=("Arial",16),bd=5)
entrY1.pack()
lbL2 = tk.Label(wiN,text="請輸入中文",fg="white",bg="green", font=("Arial", 16), width=15, height=2)
lbL2.pack()
entrY2=tk.Entry(wiN,font=("Arial",16),bd=5)
entrY2.pack()

btN1 = tk.Button(wiN,bg="blue",fg="white", text="新增單字!!", font=("Arial", 16), width=10, height=2, command=_hit1)
btN1.pack() 
btN2 = tk.Button(wiN,bg="blue",fg="white", text="顯示單字!!", font=("Arial", 16), width=10, height=2, command=_hit2)
btN2.pack() 

wiN.mainloop()

