'''
bind--KeyPress--keycode
'''
import tkinter
def key_down(e):
    global key
    key = e.keycode
    label["text"] = key


root = tkinter.Tk()
root.title("取得鍵盤代碼")
label = tkinter.Label(font=("Times New Roman", 80))
label.pack()
key = 0

root.bind("<KeyPress>", key_down)
root.focus_force()
root.mainloop()
