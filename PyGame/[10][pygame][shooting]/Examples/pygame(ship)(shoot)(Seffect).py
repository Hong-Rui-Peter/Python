'''
pygame--starship shoot(special effect)
'''
import pygame
import sys
import math
from pygame.locals import *

# 載入影像
img_galaxy = pygame.image.load("galaxy.png")
img_sship = [
    pygame.image.load("starship.png"),
    pygame.image.load("starship_l.png"),
    pygame.image.load("starship_r.png"),
    pygame.image.load("starship_burner.png")
]
img_weapon = pygame.image.load("bullet.png")

tmr = 0
bg_y = 0

WIDTH=720
HEIGHT=640

ss_x = WIDTH/2
ss_y = HEIGHT/2
ss_d = 0
ss_w=74
ss_h=96

key_spc = 0
key_z = 0

MISSILE_MAX = 200
msl_no = 0
msl_f = [False]*MISSILE_MAX
msl_x = [0]*MISSILE_MAX
msl_y = [0]*MISSILE_MAX
msl_a = [0]*MISSILE_MAX


def move_starship(scrn, key): # 移動我機
    global ss_x, ss_y, ss_d, key_spc, key_z
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
    key_spc = (key_spc+1)*key[K_SPACE]
    if key_spc%5 == 1:
        set_missile(0)
    key_z = (key_z+1)*key[K_z]
    if key_z == 1:
        set_missile(10)
    scrn.blit(img_sship[3], [ss_x-8, ss_y+40+(tmr%3)*2])
    scrn.blit(img_sship[ss_d], [ss_x-37, ss_y-48])


def set_missile(typ): # 設定我機發射的飛彈
    global msl_no
    if typ == 0: # 單發
        msl_f[msl_no] = True
        msl_x[msl_no] = ss_x
        msl_y[msl_no] = ss_y-50
        msl_a[msl_no] = 270
        msl_no = (msl_no+1)%MISSILE_MAX
    if typ == 10: # 彈幕
        for a in range(160, 390, 10):
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = a
            msl_no = (msl_no+1)%MISSILE_MAX


def move_missile(scrn): # 移動飛彈
    for i in range(MISSILE_MAX):
        if msl_f[i] == True:
            msl_x[i] = msl_x[i] + 36*math.cos(math.radians(msl_a[i]))
            msl_y[i] = msl_y[i] + 36*math.sin(math.radians(msl_a[i]))
            img_rz = pygame.transform.rotozoom(img_weapon, -90-msl_a[i], 1.0)
            scrn.blit(img_rz, [msl_x[i]-img_rz.get_width()/2, msl_y[i]-img_rz.get_height()/2])
            if msl_y[i] < 0 or msl_x[i] < 0 or msl_x[i] > WIDTH:
                msl_f[i] = False



def main(): # 主要迴圈
    global tmr, bg_y

    pygame.init()
    pygame.display.set_caption("pygame--starship shoot(special effect)")
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
        move_missile(screen)

        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main()
