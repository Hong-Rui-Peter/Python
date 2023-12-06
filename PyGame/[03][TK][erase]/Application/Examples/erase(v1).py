'''
消去遊戲--貓咪俄羅斯方塊--主畫面(一)
'''
import tkinter

root = tkinter.Tk()
root.title("主畫面(一)")
root.resizable(False, False)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

bg = tkinter.PhotoImage(file="./images/neko_bg.png")

#圖片的中心點:(912/2，768/2)=(456，384)
cvs.create_image(456, 384, image=bg)
root.focus_force()
root.mainloop()
