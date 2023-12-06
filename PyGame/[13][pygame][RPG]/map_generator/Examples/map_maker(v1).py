'''
pygame--地圖產生器--v1
'''

import pygame
import sys

CYAN = (  0, 255, 255)
GRAY = ( 96,  96,  96)

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


pygame.init()
pygame.display.set_caption("地圖產生器--v1")
screen = pygame.display.set_mode((ww, hh))
clock = pygame.time.Clock()

make_map()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                make_map()

    for y in range(map_h):
        for x in range(map_w):
            xx = x*w
            yy = y*h
            if map[y][x] == 0: # 通道
                pygame.draw.rect(screen, CYAN, [xx, yy, w, h])
            if map[y][x] == 1: # 牆壁
                pygame.draw.rect(screen, GRAY, [xx, yy, w, h])

    pygame.display.update()
    clock.tick(2)

