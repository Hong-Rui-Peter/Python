'''
消去遊戲--貓咪俄羅斯方塊--利用二維列表管理格子
'''
import tkinter


def draw_neko():
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x*72+60, y*72+60, image=img_neko[neko[y][x]])


neko = [
[1, 0, 0, 0, 0, 0, 7, 7],
[0, 2, 0, 0, 0, 0, 7, 7],
[0, 0, 3, 0, 0, 0, 0, 0],
[0, 0, 0, 4, 0, 0, 0, 0],
[0, 0, 0, 0, 5, 0, 0, 0],
[0, 0, 0, 0, 0, 6, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 2, 3, 4, 5, 6]
]

root = tkinter.Tk()
root.title("利用二維列表管理格子")
root.resizable(False, False)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

bg = tkinter.PhotoImage(file="./images/neko_bg.png")
img_neko = [
    None,
    tkinter.PhotoImage(file="./images/neko1.png"),
    tkinter.PhotoImage(file="./images/neko2.png"),
    tkinter.PhotoImage(file="./images/neko3.png"),
    tkinter.PhotoImage(file="./images/neko4.png"),
    tkinter.PhotoImage(file="./images/neko5.png"),
    tkinter.PhotoImage(file="./images/neko6.png"),
    tkinter.PhotoImage(file="./images/neko_niku.png")
]

cvs.create_image(456, 384, image=bg)
draw_neko()
root.focus_force()
root.mainloop()
