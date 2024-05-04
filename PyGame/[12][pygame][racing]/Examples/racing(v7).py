'''
Pygame Racer--場景繪製+樹、海、船與廣告看板
'''
import pygame
import sys
import math

WHITE = (255, 255, 255)
YELLOW= (255, 224,   0)

DATA_LR = [0, 0, 0, 0, 0, 0, 0, 0, 0]
DATA_UD = [0,-2,-4,-6,-4,-2, 2, 4, 2]
CLEN = len(DATA_LR)

BOARD = 120
CMAX = BOARD*CLEN
curve = [0]*CMAX
updown = [0]*CMAX
object_left = [0]*CMAX
object_right = [0]*CMAX


def make_course():
    for i in range(CLEN):
        lr1 = DATA_LR[i]
        lr2 = DATA_LR[(i+1)%CLEN]
        ud1 = DATA_UD[i]
        ud2 = DATA_UD[(i+1)%CLEN]
        for j in range(BOARD):
            pos = j+BOARD*i
            curve[pos] = lr1*(BOARD-j)/BOARD + lr2*j/BOARD
            updown[pos] = ud1*(BOARD-j)/BOARD + ud2*j/BOARD
            if j == 90:
                object_right[pos] = 1 # 看板
            if j%12 == 0:
                object_left[pos] = 2 # 椰子樹
            if j%20 == 0:
                    object_left[pos] = 3 # 遊艇
            if j%12 == 6:
                object_left[pos] = 9 # 大海


def draw_obj(bg, img, x, y, sc):
    img_rz = pygame.transform.rotozoom(img, 0, sc)
    w = img_rz.get_width()
    h = img_rz.get_height()
    bg.blit(img_rz, [x-w/2, y-h])


pygame.init()
pygame.display.set_caption("Pygame Racer--場景繪製+樹、海、船與廣告看板")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

img_bg = pygame.image.load("image/bg.png").convert()
img_sea = pygame.image.load("image/sea.png").convert_alpha()
img_obj = [
    None,
    pygame.image.load("image/board.png").convert_alpha(),
    pygame.image.load("image/tree.png").convert_alpha(),
    pygame.image.load("image/boat.png").convert_alpha()
]

# 計算道路板子的基本形狀
BOARD_W = [0]*BOARD
BOARD_H = [0]*BOARD
BOARD_UD = [0]*BOARD
for i in range(BOARD):
    BOARD_W[i] = 10+(BOARD-i)*(BOARD-i)/12
    BOARD_H[i] = 3.4*(BOARD-i)/BOARD
    BOARD_UD[i] = 2*math.sin(math.radians(i*1.5))

make_course()

car_y = 0
vertical = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] == 1:
        car_y = (car_y+1)%CMAX

    # 計算繪製道路用的X座標與路面高低
    di = 0
    ud = 0
    board_x = [0]*BOARD
    board_ud = [0]*BOARD
    for i in range(BOARD):
        di += curve[(car_y+i)%CMAX]
        ud += updown[(car_y+i)%CMAX]
        board_x[i] = 400 - BOARD_W[i]/2 + di/2
        board_ud[i] = ud/30

    horizon = 400 + int(ud/3) # 計算地平線的座標
    sy = horizon # 開始繪製道路的位置

    vertical = vertical - di*key[pygame.K_UP]/30 # 背景的垂直位置
    if vertical < 0:
        vertical += 800
    if vertical >= 800:
        vertical -= 800

    # 繪製草地
    screen.fill((0, 56, 255)) # 天空的顏色
    screen.blit(img_bg, [vertical-800, horizon-400])
    screen.blit(img_bg, [vertical, horizon-400])
    screen.blit(img_sea, [board_x[BOARD-1]-780, sy]) # 最遠的大海

    # 根據繪圖用資料繪製道路
    for i in range(BOARD-1, 0, -1):
        ux = board_x[i]
        uy = sy - BOARD_UD[i]*board_ud[i]
        uw = BOARD_W[i]
        sy = sy + BOARD_H[i]*(600-horizon)/200
        bx = board_x[i-1]
        by = sy - BOARD_UD[i-1]*board_ud[i-1]
        bw = BOARD_W[i-1]
        col = (160,160,160)
        pygame.draw.polygon(screen, col, [[ux, uy], [ux+uw, uy], [bx+bw, by], [bx, by]])

        if int(car_y+i)%10 <= 4: # 左右的黃線
            pygame.draw.polygon(screen, YELLOW, [[ux, uy], [ux+uw*0.02, uy], [bx+bw*0.02, by], [bx, by]])
            pygame.draw.polygon(screen, YELLOW, [[ux+uw*0.98, uy], [ux+uw, uy], [bx+bw, by], [bx+bw*0.98, by]])
        if int(car_y+i)%20 <= 10: # 白線
            pygame.draw.polygon(screen, WHITE, [[ux+uw*0.24, uy], [ux+uw*0.26, uy], [bx+bw*0.26, by], [bx+bw*0.24, by]])
            pygame.draw.polygon(screen, WHITE, [[ux+uw*0.49, uy], [ux+uw*0.51, uy], [bx+bw*0.51, by], [bx+bw*0.49, by]])
            pygame.draw.polygon(screen, WHITE, [[ux+uw*0.74, uy], [ux+uw*0.76, uy], [bx+bw*0.76, by], [bx+bw*0.74, by]])

        scale = 1.5*BOARD_W[i]/BOARD_W[0]
        obj_l = object_left[int(car_y+i)%CMAX] # 道路左邊的物體
        if obj_l == 2: # 椰子樹
            draw_obj(screen, img_obj[obj_l], ux-uw*0.05, uy, scale)
        if obj_l == 3: # 遊艇
            draw_obj(screen, img_obj[obj_l], ux-uw*0.5, uy, scale)
        if obj_l == 9: # 大海
            screen.blit(img_sea, [ux-uw*0.5-780, uy])
        obj_r = object_right[int(car_y+i)%CMAX] # 道路右邊的物體
        if obj_r == 1: # 看板
            draw_obj(screen, img_obj[obj_r], ux+uw*1.3, uy, scale)

    pygame.display.update()
    clock.tick(60)

