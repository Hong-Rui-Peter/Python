'''
消去遊戲--貓咪俄羅斯方塊--點選後配置貓咪
'''
import tkinter
import random


def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1


def draw_neko():
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x*72+60, y*72+60, image=img_neko[neko[y][x]], tag="NEKO")

def drop_neko():
    for y in range(8, -1, -1):
        for x in range(8):
            if neko[y][x] != 0 and neko[y+1][x] == 0:
                neko[y+1][x] = neko[y][x]
                neko[y][x] = 0

def game_main():
    global cursor_x, cursor_y, mouse_c
    drop_neko()
    if 24 <= mouse_x and mouse_x < 24+72*8 and 24 <= mouse_y and mouse_y < 24+72*10:
        cursor_x = int((mouse_x-24)/72)
        cursor_y = int((mouse_y-24)/72)
        if mouse_c == 1:
            mouse_c = 0
            neko[cursor_y][cursor_x] = random.randint(1, 6)
    cvs.delete("CURSOR")
    cvs.create_image(cursor_x*72+60, cursor_y*72+60, image=cursor, tag="CURSOR")
    cvs.delete("NEKO")
    draw_neko()
    root.after(100, game_main)


cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0
neko = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]


root = tkinter.Tk()
root.title("點選後配置貓咪")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

bg = tkinter.PhotoImage(file="./images/neko_bg.png")
cursor = tkinter.PhotoImage(file="./images/neko_cursor.png")
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
game_main()
root.focus_force()
root.mainloop()
