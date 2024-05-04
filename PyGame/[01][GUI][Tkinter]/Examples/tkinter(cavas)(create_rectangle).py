'''
Tkinter-Cavas--create_rectangle
'''
import tkinter as tk

root = tk.Tk()
root.title('my window')

mycanvas = tk.Canvas(root, width=400, height=200)
mycanvas.pack()

mycanvas.create_rectangle(10, 10, 90, 100)
mycanvas.create_rectangle(110, 10, 190, 100, dash=(4, 4))
mycanvas.create_rectangle(210, 10, 290, 100, fill='red')
mycanvas.create_rectangle(310, 10, 390, 100, outline='blue')

root.mainloop()