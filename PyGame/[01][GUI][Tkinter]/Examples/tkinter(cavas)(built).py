'''
Tkinter-Cavas--built
'''
import tkinter as tk

root = tk.Tk()
root.title('my window')

mycanvas = tk.Canvas(root, width=300, height=200)
mycanvas.pack()

root.mainloop()