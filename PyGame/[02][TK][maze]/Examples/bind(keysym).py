'''
bind--KeyPress--keysym
'''
import tkinter

def key_down(e):
    global key
    key = e.keysym
    label["text"] = key

def main_proc():
    root.after(100, main_proc)

root = tkinter.Tk()
root.title("取得鍵盤字符")
root.bind("<KeyPress>", key_down)
label = tkinter.Label(font=("Times New Roman", 80))
label.pack()

key = ""
main_proc()
root.focus_force()
root.mainloop()
