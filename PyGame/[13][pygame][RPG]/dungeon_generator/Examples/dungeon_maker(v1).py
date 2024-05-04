'''
Pygame--擴增地圖--1.先全部填滿牆壁
'''
import pygame
import sys
import random

BLACK = (  0,   0,   0)
CYAN  = (  0, 255, 255)
GRAY  = ( 96,  96,  96)

MAZE_W = 11
MAZE_H = 9
maze = []
for y in range(MAZE_H):
    maze.append([0]*MAZE_W)

DUNGEON_W = MAZE_W*3
DUNGEON_H = MAZE_H*3
dungeon = []
for y in range(DUNGEON_H):
    dungeon.append([0]*DUNGEON_W)

imgWall = pygame.image.load("wall.png")
imgFloor = pygame.image.load("floor.png")

def make_dungeon(): # 自動產生地下城
    XP = [ 0, 1, 0,-1]
    YP = [-1, 0, 1, 0]
    #周圍的牆壁
    for x in range(MAZE_W):
        maze[0][x] = 1
        maze[MAZE_H-1][x] = 1
    for y in range(1, MAZE_H-1):
        maze[y][0] = 1
        maze[y][MAZE_W-1] = 1
    #迷宮內部一片空白的狀態
    for y in range(1, MAZE_H-1):
        for x in range(1, MAZE_W-1):
            maze[y][x] = 0
    #柱子
    for y in range(2, MAZE_H-2, 2):
        for x in range(2, MAZE_W-2, 2):
            maze[y][x] = 1
    #在柱子的上下左右建立牆壁
    for y in range(2, MAZE_H-2, 2):
        for x in range(2, MAZE_W-2, 2):
         d = random.randint(0, 3)
         if x > 2: # 從第二欄的柱子開始，不在左側建立牆壁
             d = random.randint(0, 2)
         maze[y+YP[d]][x+XP[d]] = 1

    # 根據迷宮建立地下城
    #將所有格子設定為牆壁
    for y in range(DUNGEON_H):
        for x in range(DUNGEON_W):
            dungeon[y][x] = 9

pygame.init()
pygame.display.set_caption("Pygame--擴增地圖--1.先全部填滿牆壁")
screen = pygame.display.set_mode((1056, 432))
clock = pygame.time.Clock()

make_dungeon()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                make_dungeon()

    # 顯示確認用的迷宮
    for y in range(MAZE_H):
        for x in range(MAZE_W):
            X = x*48
            Y = y*48
            if maze[y][x] == 0:
                pygame.draw.rect(screen, CYAN, [X,Y,48,48])
            if maze[y][x] == 1:
                pygame.draw.rect(screen, GRAY, [X,Y,48,48])

    # 繪製地下城
    for y in range(DUNGEON_H):
        for x in range(DUNGEON_W):
            X = x*16+528
            Y = y*16
            if dungeon[y][x] == 0:
                screen.blit(imgFloor, [X, Y])
            if dungeon[y][x] == 9:
                screen.blit(imgWall, [X, Y])

    pygame.display.update()
    clock.tick(2)

