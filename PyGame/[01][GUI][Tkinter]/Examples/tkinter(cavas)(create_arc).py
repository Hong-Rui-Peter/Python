'''
Tkinter-Cavas--create_arc
'''
import tkinter as tk

root = tk.Tk()
root.title('my window')

mycanvas = tk.Canvas(root, width=350, height=200)
mycanvas.pack()

mycanvas.create_arc(10, 10, 100, 100)
mycanvas.create_arc(110, 10, 200, 100, extent=45)
mycanvas.create_arc(210, 10, 300, 100, extent=180)

mycanvas.create_arc(10, 110, 100, 210, style=tk.ARC)
mycanvas.create_arc(110, 110, 200, 210, style=tk.PIESLICE)
mycanvas.create_arc(210, 110, 300, 210, style=tk.CHORD)

root.mainloop()