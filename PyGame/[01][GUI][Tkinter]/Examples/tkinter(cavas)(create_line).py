'''
Tkinter-Cavas--create_line
'''
import tkinter as tk

root = tk.Tk()
root.title('my window')

mycanvas = tk.Canvas(root, width=300, height=200)
mycanvas.pack()

mycanvas.create_line(20, 20, 280, 20)
mycanvas.create_line(20, 40, 280, 40, dash=(4, 4))
mycanvas.create_line(20, 60, 280, 60, width=5)
mycanvas.create_line(20, 80, 280, 80, fill='red')

root.mainloop()