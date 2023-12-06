'''
Tkinter-Cavas--create_oval
'''
import tkinter as tk

root = tk.Tk()
root.title('my window')

mycanvas = tk.Canvas(root, width=320, height=200)
mycanvas.pack()

mycanvas.create_oval(10, 10, 100, 100) # 圓形
mycanvas.create_oval(110, 10, 200, 100, fill='red') # 圓形
mycanvas.create_oval(210, 10, 300, 100, outline='blue') # 圓形
mycanvas.create_oval(10, 110, 290, 190) # 橢圓

root.mainloop()