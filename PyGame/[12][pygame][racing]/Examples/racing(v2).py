'''
Pygame Racer--背景連動
'''
import pygame
import sys
import math

BOARD = 120
CMAX = BOARD*4
curve = [0]*CMAX


def make_course():
    for i in range(360):
        curve[BOARD+i] = int(5*math.sin(math.radians(i)))


pygame.init()
pygame.display.set_caption("Pygame Racer--背景連動")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

img_bg = pygame.image.load("image/bg.png").convert()

# 計算道路板子的基本形狀
BOARD_W = [0]*BOARD
BOARD_H = [0]*BOARD
for i in range(BOARD):
    BOARD_W[i] = 10+(BOARD-i)*(BOARD-i)/12
    BOARD_H[i] = 3.4*(BOARD-i)/BOARD

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

    # 計算繪製道路用的X座標
    di = 0
    board_x = [0]*BOARD
    for i in range(BOARD):
        di += curve[(car_y+i)%CMAX]
        board_x[i] = 400 - BOARD_W[i]/2 + di/2

    sy = 400 # 開始繪製道路的位置

    vertical = vertical - di*key[pygame.K_UP]/30 # 背景的垂直位置
    if vertical < 0:
        vertical += 800
    if vertical >= 800:
        vertical -= 800

    screen.blit(img_bg, [vertical-800, 0])
    screen.blit(img_bg, [vertical, 0])

    # 根據繪圖用資料繪製道路
    for i in range(BOARD-1, 0, -1):
        ux = board_x[i]
        uy = sy
        uw = BOARD_W[i]
        sy = sy + BOARD_H[i]
        bx = board_x[i-1]
        by = sy
        bw = BOARD_W[i-1]
        col = (160,160,160)
        if (car_y+i)%12 == 0:
            col = (255,255,255)
        pygame.draw.polygon(screen, col, [[ux, uy], [ux+uw, uy], [bx+bw, by], [bx, by]])

    pygame.display.update()
    clock.tick(60)

