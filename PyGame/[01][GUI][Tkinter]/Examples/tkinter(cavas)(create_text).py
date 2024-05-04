'''
Tkinter-Cavas--create_text
'''
import tkinter as tk

root = tk.Tk()
root.title('my window')

mycanvas = tk.Canvas(root, width=300, height=200)
mycanvas.pack()

mycanvas.create_text(100, 50, text='Hello World')
mycanvas.create_text(100, 100, text='Python tkinter', font=('Arial', 18))
mycanvas.create_text(0, 0, text='123456', anchor='nw')

root.mainloop()