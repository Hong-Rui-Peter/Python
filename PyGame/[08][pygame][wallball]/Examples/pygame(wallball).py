'''
Pygame示範程式--Wallball
'''
# 載入模組
import pygame
import random

# 定義環境變數與顏色
WIDTH = 500
HEIGHT = 600
FPS = 200

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ball_c=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
ball_x=100
ball_y=100
dx=-1
dy=-1
radius=20
start=False

# 初始化宣告
pygame.init()
pygame.mixer.init()

#創建螢幕與文字宣告
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wallball")
icon=pygame.image.load("ball.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

myfont = pygame.font.Font(None,60)

# 遊戲迴圈
running = True

while running:
    # 控制游戲刷新速度
    clock.tick(FPS)
    # 處理(監聽)游戲事件
    for event in pygame.event.get():
        # 監聽是否關閉視窗
        if event.type == pygame.QUIT:
            running = False

    # 更新螢幕
    md= pygame.mouse.get_pressed()
    if start==False:
        ball_x, ball_y = pygame.mouse.get_pos()
        if md[2]==True:
            start=True
    else:        
        if md[0]==True:
            start=False
        ball_x=ball_x+dx
        ball_y=ball_y+dy
        # 右牆或左牆碰撞.
        if(ball_x + dx > WIDTH - radius or ball_x + dx < radius):
            dx = -dx
            ball_c=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

        # 下牆或上牆碰撞
        if(ball_y + dy > HEIGHT - radius or ball_y + dy < radius):        
            dy = -dy    
            ball_c=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    # 渲染(繪圖)
    screen.fill(BLACK)
    pygame.draw.circle(screen, ball_c, [ball_x,ball_y], radius)
    
    
    # *after* drawing everything, flip the display
    pygame.display.update()

pygame.quit()