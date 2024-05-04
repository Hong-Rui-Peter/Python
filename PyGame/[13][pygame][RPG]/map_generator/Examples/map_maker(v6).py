'''
pygame--地圖產生器--v6--走迷宮
'''

import pygame
import sys
import random

CYAN = (  0, 255, 255)
GRAY = ( 96,  96,  96)

wall=pygame.image.load("wall.jpg")
road=pygame.image.load("road.jpeg")
pp=pygame.image.load("penguin.png")

px=1
py=1

#地圖的格字數
map_w = 15
map_h = 11
w = 48
h= 48

ww=w*map_w
hh=h*map_h

map = []
for y in range(map_h):
    map.append([0]*map_w)

def make_map():
    XP = [ 0, 1, 0,-1]
    YP = [-1, 0, 1, 0]

    #周圍的牆壁
    for x in range(map_w):
        map[0][x] = 1
        map[map_h-1][x] = 1
    for y in range(1, map_h-1):
        map[y][0] = 1
        map[y][map_w-1] = 1

    #內部為一片空白的狀態
    for y in range(1, map_h-1):
        for x in range(1, map_w-1):
            map[y][x] = 0

    #柱子
    for y in range(2, map_h-2, 2):
        for x in range(2, map_w-2, 2):
            map[y][x] = 1

    #於柱子的上下左右建立牆壁
    for y in range(2, map_h-2, 2):
        for x in range(2, map_w-2, 2):
         d = random.randint(0, 3)
         if x > 2: # 從第二欄的柱子開始，不在左側建立牆壁
             d = random.randint(0, 2)
         map[y+YP[d]][x+XP[d]] = 1

pygame.init()
pygame.display.set_caption("地圖產生器--v6--走迷宮")
screen = pygame.display.set_mode((ww, hh))
clock = pygame.time.Clock()

make_map()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if map[py][px+1]==0:
                    px=px+1
            if event.key == pygame.K_LEFT:
                if map[py][px-1]==0:
                    px=px-1
            if event.key == pygame.K_UP:
                if map[py-1][px]==0:
                    py=py-1
            if event.key == pygame.K_DOWN:
                if map[py+1][px]==0:
                    py=py+1
            if event.key == pygame.K_F1:
                make_map()
                px=1
                py=1


    for y in range(map_h):
        for x in range(map_w):
            xx = x*w
            yy = y*h
            if map[y][x] == 0: # 通道
                screen.blit(pygame.transform.scale(road, (w,h)), [x*w, y*h])
            if map[y][x] == 1: # 牆壁
                screen.blit(pygame.transform.scale(wall, (w,h)), [x*w, y*h])
    screen.blit(pygame.transform.scale(pp, (w,h)), [px*w, py*h])

    pygame.display.update()
    clock.tick(30)

