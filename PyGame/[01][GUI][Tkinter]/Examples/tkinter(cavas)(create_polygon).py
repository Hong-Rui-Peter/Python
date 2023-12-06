'''
Tkinter-Cavas--create_polygon
'''
import tkinter as tk

root = tk.Tk()
root.title('my window')

mycanvas = tk.Canvas(root, width=300, height=200)
mycanvas.pack()

mycanvas.create_polygon(40,40, 60,20, 80,40, 80,80, 40,80)
mycanvas.create_polygon(100,40, 120,20, 140,40, 140,80, 100,80, fill='', outline='black')
mycanvas.create_polygon(160,80, 200,80, 180,20, fill='yellow')
mycanvas.create_polygon(220,80, 260,80, 240,20, fill='red', outline='black')

root.mainloop()