'''
Pygame Racer--場景繪製+道路左右彎
'''
import pygame
import sys
import math

BOARD = 120 #道路板子數量
CMAX = BOARD*4  #賽道長度
curve = [0]*CMAX    #道路彎曲方向的列表


def make_course():  #建立賽道資料的函式(用三角函數計算並代入道路的彎曲狀態)
    for i in range(360):
        curve[BOARD+i] = int(5*math.sin(math.radians(i)))


pygame.init()
pygame.display.set_caption("Pygame Racer--場景繪製+道路左右彎")
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

    screen.blit(img_bg, [0, 0])

    # 根據繪圖資料繪製道路
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

