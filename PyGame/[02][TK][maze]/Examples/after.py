'''
after--時間控制
'''
import tkinter
tmr = 0
def count_up():
    global tmr
    tmr = tmr + 1
    label["text"] = tmr
    root.after(1000,count_up)

root = tkinter.Tk()
label = tkinter.Label(font=("Times New Roman", 80))
label.pack()
count_up()

root.mainloop()
