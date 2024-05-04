'''
Pygame Racer--上下坡起伏
'''
import pygame
import sys
import math

BOARD = 120
CMAX = BOARD*3
curve = [0]*CMAX
updown = [0]*CMAX


def make_course():
    for i in range(CMAX):
        updown[i] = int(5*math.sin(math.radians(i)))


pygame.init()
pygame.display.set_caption("Pygame Racer--上下坡起伏")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

img_bg = pygame.image.load("image/bg.png").convert()

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
        if (car_y+i)%12 == 0:
            col = (255,255,255)
        pygame.draw.polygon(screen, col, [[ux, uy], [ux+uw, uy], [bx+bw, by], [bx, by]])

    pygame.display.update()
    clock.tick(60)

