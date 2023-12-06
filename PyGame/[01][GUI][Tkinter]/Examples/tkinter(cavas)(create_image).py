'''
Tkinter-Cavas--create_image
'''
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('my window')
#root.geometry('500x500')
img = Image.open('image1.jpg')
img2 = ImageTk.PhotoImage(img)


mycanvas = tk.Canvas(root, width=img.size[0], height=img.size[1])
mycanvas.pack()

mycanvas.create_image(0,0, anchor=tk.NW, image=img2)

root.mainloop()