'''
pygame--starship move
'''
import pygame
import sys
from pygame.locals import *

# 載入影像
img_galaxy = pygame.image.load("galaxy.png")
img_sship = [
    pygame.image.load("starship.png"),
    pygame.image.load("starship_l.png"),
    pygame.image.load("starship_r.png"),
    pygame.image.load("starship_burner.png")
]

tmr = 0
bg_y = 0

WIDTH=720
HEIGHT=640

ss_x = WIDTH/2
ss_y = HEIGHT/2
ss_d = 0
ss_w=74
ss_h=96

def move_starship(scrn, key): # 移動我機
    global ss_x, ss_y, ss_d
    ss_d = 0
    if key[K_UP] == 1:
        ss_y = ss_y - 20
        if ss_y < ss_h/2:
            ss_y = ss_h/2
    if key[K_DOWN] == 1:
        ss_y = ss_y + 20
        if ss_y > HEIGHT-ss_h/2:
            ss_y = HEIGHT-ss_h/2
    if key[K_LEFT] == 1:
        ss_d = 1
        ss_x = ss_x - 20
        if ss_x < ss_w/2:
            ss_x = ss_w/2
    if key[K_RIGHT] == 1:
        ss_d = 2
        ss_x = ss_x + 20
        if ss_x > WIDTH-ss_w/2:
            ss_x = WIDTH-ss_w/2
    scrn.blit(img_sship[3], [ss_x-8, ss_y+40])
#    scrn.blit(img_sship[3], [ss_x-8, ss_y+40+(tmr%3)*2])
    scrn.blit(img_sship[ss_d], [ss_x-ss_w/2, ss_y-ss_h/2])


def main(): # 主要迴圈
    global tmr, bg_y

    pygame.init()
    pygame.display.set_caption("pygame--starship move")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 捲動背景
        bg_y = (bg_y+16)%HEIGHT
        screen.blit(img_galaxy, [0, bg_y-HEIGHT])
        screen.blit(img_galaxy, [0, bg_y])

        key = pygame.key.get_pressed()
        move_starship(screen, key)

        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main()
