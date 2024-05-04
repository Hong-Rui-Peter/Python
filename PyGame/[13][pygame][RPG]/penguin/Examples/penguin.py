'''
Pygame--棄兒ㄉ迷宮大冒險
'''
import pygame
import sys
import random

WHITE  = (255, 255, 255)
BLACK  = (  0,   0,   0)
LIME   = (  0, 255,   0)
YELLOW = (255, 255,   0)
ORANGE = (255, 192,   0)
RED    = (255,   0,   0)
PINK   = (255, 128, 255)
VIOLET = (255,   0, 224)
global key, koff, idx, tmr, stage, score, nokori, se_candy

img_bg = [
    pygame.image.load("images/chip00.png"),
    pygame.image.load("images/chip01.png"),
    pygame.image.load("images/chip02.png"),
    pygame.image.load("images/chip03.png")
]
img_pen = [
    pygame.image.load("images/pen00.png"),
    pygame.image.load("images/pen01.png"),
    pygame.image.load("images/pen02.png"),
    pygame.image.load("images/pen03.png"),
    pygame.image.load("images/pen04.png"),
    pygame.image.load("images/pen05.png"),
    pygame.image.load("images/pen06.png"),
    pygame.image.load("images/pen07.png"),
    pygame.image.load("images/pen08.png"),
    pygame.image.load("images/pen09.png"),
    pygame.image.load("images/pen10.png"),
    pygame.image.load("images/pen11.png"),
    pygame.image.load("images/pen_face.png")
]
img_red = [
    pygame.image.load("images/red00.png"),
    pygame.image.load("images/red01.png"),
    pygame.image.load("images/red02.png"),
    pygame.image.load("images/red03.png"),
    pygame.image.load("images/red04.png"),
    pygame.image.load("images/red05.png"),
    pygame.image.load("images/red06.png"),
    pygame.image.load("images/red07.png"),
    pygame.image.load("images/red08.png"),
    pygame.image.load("images/red09.png"),
    pygame.image.load("images/red10.png"),
    pygame.image.load("images/red11.png")
]
img_kuma = [
    pygame.image.load("images/kuma00.png"),
    pygame.image.load("images/kuma01.png"),
    pygame.image.load("images/kuma02.png")
]
img_title = pygame.image.load("images/title.png")
img_ending = pygame.image.load("images/ending.png")

se_candy = None

DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3
ANIMATION = [0, 1, 0, 2]
BLINK = [(255,255,255), (255,255,192), (255,255,128), (255,224,64), (255,255,128), (255,255,192)] 

idx = 0
tmr = 0
stage = 1
score = 0
nokori = 3
candy = 0

pen_x = 0
pen_y = 0
pen_d = 0
pen_a = 0

red_x = 0
red_y = 0
red_d = 0
red_a = 0
red_sx = 0
red_sy = 0

kuma_x = 0
kuma_y = 0
kuma_d = 0
kuma_a = 0
kuma_sx = 0
kuma_sy = 0
kuma_sd = 0

map_data = [] # 迷宮用的清單

def set_stage(): # 設定關卡資料
    global map_data, candy
    global red_sx, red_sy
    global kuma_sx, kuma_sy, kuma_sd

    if stage == 1:
        map_data = [
        [0,1,1,1,1,0,0,1,1,1,1,0],
        [0,2,3,3,2,1,1,2,3,3,2,0],
        [0,3,0,0,3,3,3,3,0,0,3,0],
        [0,3,1,1,3,0,0,3,1,1,3,0],
        [0,3,2,2,3,0,0,3,2,2,3,0],
        [0,3,0,0,3,1,1,3,0,0,3,0],
        [0,3,1,1,3,3,3,3,1,1,3,0],
        [0,2,3,3,2,0,0,2,3,3,2,0],
        [0,0,0,0,0,0,0,0,0,0,0,0]
        ]
        candy = 32
        red_sx = 630
        red_sy = 450
        kuma_sd = -1

    if stage == 2:
        map_data = [
        [0,1,1,1,1,1,1,1,1,1,1,0],
        [0,2,2,2,3,3,3,3,2,2,2,0],
        [0,3,3,0,2,1,1,2,0,3,3,0],
        [0,3,3,1,3,3,3,3,1,3,3,0],
        [0,2,1,3,3,3,3,3,3,1,2,0],
        [0,3,3,0,3,3,3,3,0,3,3,0],
        [0,3,3,1,2,1,1,2,1,3,3,0],
        [0,2,2,2,3,3,3,3,2,2,2,0],
        [0,0,0,0,0,0,0,0,0,0,0,0]
        ]
        candy = 38
        red_sx = 630
        red_sy = 90
        kuma_sx = 330
        kuma_sy = 270
        kuma_sd = DIR_LEFT

    if stage == 3:
        map_data = [
        [0,1,0,1,0,1,1,1,1,1,1,0],
        [0,2,1,3,1,2,2,3,3,3,3,0],
        [0,2,2,2,2,2,2,3,3,3,3,0],
        [0,2,1,1,1,2,2,1,1,1,1,0],
        [0,2,2,2,2,3,3,2,2,2,2,0],
        [0,1,1,2,0,2,2,0,1,1,2,0],
        [0,3,3,3,1,1,1,0,3,3,3,0],
        [0,3,3,3,2,2,2,0,3,3,3,0],
        [0,0,0,0,0,0,0,0,0,0,0,0]
        ]
        candy = 23
        red_sx = 630
        red_sy = 450
        kuma_sx = 330
        kuma_sy = 270
        kuma_sd = DIR_RIGHT

    if stage == 4:
        map_data = [
        [0,1,1,1,1,1,1,1,1,1,1,0],
        [0,3,3,3,3,3,3,3,3,3,3,0],
        [0,3,0,3,3,1,3,0,3,0,3,0],
        [0,3,1,0,3,3,3,0,3,1,3,0],
        [0,3,3,0,1,1,1,0,3,3,3,0],
        [0,3,0,1,3,3,3,1,3,1,1,0],
        [0,3,1,3,3,1,3,3,3,3,3,0],
        [0,3,3,3,3,3,3,3,3,3,3,0],
        [0,0,0,0,0,0,0,0,0,0,0,0]
        ]
        candy = 50
        red_sx = 150
        red_sy = 270
        kuma_sx = 510
        kuma_sy = 270
        kuma_sd = DIR_UP

    if stage == 5:
        map_data = [
        [0,1,0,1,1,1,1,1,1,1,1,0],
        [0,2,0,3,3,3,3,3,3,3,3,0],
        [0,2,0,3,0,1,3,3,1,0,3,0],
        [0,2,0,3,0,3,3,3,3,0,3,0],
        [0,2,1,3,1,1,3,3,1,1,3,0],
        [0,2,2,3,3,3,3,3,3,3,3,0],
        [0,2,1,1,1,1,2,1,1,1,1,0],
        [0,3,3,3,3,3,3,3,3,3,3,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        ]
        candy = 40
        red_sx = 630
        red_sy = 450
        kuma_sx = 390
        kuma_sy = 210
        kuma_sd = DIR_RIGHT


def set_chara_pos(): # 角色的起始位置
    global pen_x, pen_y, pen_d, pen_a
    global red_x, red_y, red_d, red_a
    global kuma_x, kuma_y, kuma_d, kuma_a
    pen_x = 90
    pen_y = 90
    pen_d = DIR_DOWN
    pen_a = 3
    red_x = red_sx
    red_y = red_sy
    red_d = DIR_DOWN
    red_a = 3
    kuma_x = kuma_sx
    kuma_y = kuma_sy
    kuma_d = kuma_sd
    kuma_a = 0


def draw_txt(scrn, txt, x, y, siz, col): # 陰影文字
    fnt = pygame.font.Font(None, siz*2)
    sur = fnt.render(txt, True, BLACK)
    x = x - sur.get_width()/2
    y = y - sur.get_height()/2
    scrn.blit(sur, [x+2, y+2])
    sur = fnt.render(txt, True, col)
    scrn.blit(sur, [x, y])


def draw_screen(scrn): # 繪製遊戲畫面
    for y in range(9):
        for x in range(12):
            scrn.blit(img_bg[map_data[y][x]], [x*60, y*60])
    scrn.blit(img_pen[pen_a], [pen_x-30, pen_y-30])
    scrn.blit(img_red[red_a], [red_x-30, red_y-30])
    if kuma_sd != -1:
        scrn.blit(img_kuma[kuma_a], [kuma_x-30, kuma_y-30])
    draw_txt(scrn, "SCORE "+str(score), 200, 30, 30, WHITE)
    draw_txt(scrn, "STAGE "+str(stage), 520, 30, 30, LIME)
    for i in range(nokori):
        scrn.blit(img_pen[12], [60+i*50, 500])


def check_wall(cx, cy, di, dot): # 確認每個方向是否有牆壁
    chk = False
    if di == DIR_UP:
        mx = int((cx-30)/60)
        my = int((cy-30-dot)/60)
        if map_data[my][mx] <= 1: # 左上
            chk = True
        mx = int((cx+29)/60)
        if map_data[my][mx] <= 1: # 右上
            chk = True
    if di == DIR_DOWN:
        mx = int((cx-30)/60)
        my = int((cy+29+dot)/60)
        if map_data[my][mx] <= 1: # 左下
            chk = True
        mx = int((cx+29)/60)
        if map_data[my][mx] <= 1: # 右下
            chk = True
    if di == DIR_LEFT:
        mx = int((cx-30-dot)/60)
        my = int((cy-30)/60)
        if map_data[my][mx] <= 1: # 左上
            chk = True
        my = int((cy+29)/60)
        if map_data[my][mx] <= 1: # 左下
            chk = True
    if di == DIR_RIGHT:
        mx = int((cx+29+dot)/60)
        my = int((cy-30)/60)
        if map_data[my][mx] <= 1: # 右上
            chk = True
        my = int((cy+29)/60)
        if map_data[my][mx] <= 1: # 右下
            chk = True
    return chk


def move_penpen(key): # 移動penpen
    global score, candy, pen_x, pen_y, pen_d, pen_a
    if key[pygame.K_UP] == 1:
        pen_d = DIR_UP
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_y = pen_y - 20
    elif key[pygame.K_DOWN] == 1:
        pen_d = DIR_DOWN
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_y = pen_y + 20
    elif key[pygame.K_LEFT] == 1:
        pen_d = DIR_LEFT
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_x = pen_x - 20
    elif key[pygame.K_RIGHT] == 1:
        pen_d = DIR_RIGHT
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_x = pen_x + 20
    pen_a = pen_d*3 + ANIMATION[tmr%4]
    mx = int(pen_x/60)
    my = int(pen_y/60)
    if map_data[my][mx] == 3: # 取得糖果了嗎？
        score = score + 100
        map_data[my][mx] = 2
        candy = candy - 1
        se_candy.play()


def move_enemy(): # 移動red
    global idx, tmr, red_x, red_y, red_d, red_a
    speed = 10
    if red_x%60 == 30 and red_y%60 == 30:
        red_d = random.randint(0, 6)
        if red_d >= 4:
            if pen_y < red_y:
                red_d = DIR_UP
            if pen_y > red_y:
                red_d = DIR_DOWN
            if pen_x < red_x:
                red_d = DIR_LEFT
            if pen_x > red_x:
                red_d = DIR_RIGHT
    if red_d == DIR_UP:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_y = red_y - speed
    if red_d == DIR_DOWN:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_y = red_y + speed
    if red_d == DIR_LEFT:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_x = red_x - speed
    if red_d == DIR_RIGHT:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_x = red_x + speed
    red_a = red_d*3 + ANIMATION[tmr%4]
    if abs(red_x-pen_x) <= 40 and abs(red_y-pen_y) <= 40:
        idx = 2
        tmr = 0


def move_enemy2(): # 移動kumagon
    global idx, tmr, kuma_x, kuma_y, kuma_d, kuma_a
    speed = 5
    if kuma_sd == -1:
        return
    if kuma_d == DIR_UP:
        if check_wall(kuma_x, kuma_y, kuma_d, speed) == False:
            kuma_y = kuma_y - speed
        else:
            kuma_d = DIR_DOWN
    elif kuma_d == DIR_DOWN:
        if check_wall(kuma_x, kuma_y, kuma_d, speed) == False:
            kuma_y = kuma_y + speed
        else:
            kuma_d = DIR_UP
    elif kuma_d == DIR_LEFT:
        if check_wall(kuma_x, kuma_y, kuma_d, speed) == False:
            kuma_x = kuma_x - speed
        else:
            kuma_d = DIR_RIGHT
    elif kuma_d == DIR_RIGHT:
        if check_wall(kuma_x, kuma_y, kuma_d, speed) == False:
            kuma_x = kuma_x + speed
        else:
            kuma_d = DIR_LEFT
    kuma_a = ANIMATION[tmr%4]
    if abs(kuma_x-pen_x) <= 40 and abs(kuma_y-pen_y) <= 40:
        idx = 2
        tmr = 0


pygame.init()
pygame.display.set_caption("Pygame--棄兒ㄉ迷宮大冒險")
screen = pygame.display.set_mode((720, 540))
clock = pygame.time.Clock()
se_candy = pygame.mixer.Sound("sounds/candy.ogg")

set_stage()
set_chara_pos()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                screen = pygame.display.set_mode((720, 540), pygame.FULLSCREEN)
            if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                screen = pygame.display.set_mode((720, 540))

    key = pygame.key.get_pressed()
    tmr = tmr + 1
    draw_screen(screen)

    if idx == 0: # 標題畫面
        screen.blit(img_title, [360-320, 200-100])
        if tmr%10 < 5:
            draw_txt(screen, "Press SPACE !", 360, 380, 30, YELLOW)
        if key[pygame.K_F1] == 1:
            stage = 1
            score = 0
            nokori = 3
            set_stage()
            set_chara_pos()
            idx = 1
            tmr = 0

    if idx == 1: # 玩遊戲
        move_penpen(key)
        move_enemy()
        move_enemy2()
        if candy == 0:
            idx = 4
            tmr = 0
        if tmr == 1:
            pygame.mixer.music.load("sounds/bgm.ogg")
            pygame.mixer.music.play(-1)

    if idx == 2: # 被敵人攻擊
        draw_txt(screen, "Die", 360, 270, 40, ORANGE)
        if tmr == 1:
            pygame.mixer.music.stop()
            nokori = nokori - 1
        if tmr == 5:
            pygame.mixer.music.load("sounds/miss.ogg")
            pygame.mixer.music.play(0)
        if tmr == 50:
            if nokori == 0:
                idx = 3
                tmr = 0
            else:
                set_chara_pos()
                idx = 1
                tmr = 0

    if idx == 3: # 遊戲結束
        draw_txt(screen, "GAME OVER", 360, 270, 40, RED)
        if tmr == 50:
            idx = 0

    if idx == 4: # 過關
        if stage < 5:
            draw_txt(screen, "STAGE CLEAR", 360, 270, 40, PINK)
        else:
            draw_txt(screen, "ALL STAGE CLEAR!", 360, 270, 40, VIOLET)
        if tmr == 1:
            pygame.mixer.music.stop()
        if tmr == 5:
            pygame.mixer.music.load("sounds/clear.ogg")
            pygame.mixer.music.play(0)
        if tmr == 50:
            if stage < 5:
                stage = stage + 1
                set_stage()
                set_chara_pos()
                idx = 1
                tmr = 0
            else:
                idx = 5
                tmr = 0

    if idx == 5: # 結尾
        if tmr < 60:
            xr = 8*tmr
            yr = 6*tmr
            pygame.draw.ellipse(screen, BLACK, [360-xr, 270-yr, xr*2, yr*2])
        else:
            pygame.draw.rect(screen, BLACK, [0, 0, 720, 540])
            screen.blit(img_ending, [360-120, 300-80])
            draw_txt(screen, "Congratulations!", 360, 160, 40, BLINK[tmr%6])
        if tmr == 300:
            idx = 0

    pygame.display.update()
    clock.tick(10)

