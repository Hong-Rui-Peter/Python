'''
Pygame示範程式--wallball--rect版
'''
# 載入模組
import pygame,random

# 定義環境變數與顏色
WIDTH = 360
HEIGHT = 480
FPS = 200

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
bg=BLACK


sx=1
sy=1

# 初始化宣告
pygame.init()
pygame.mixer.init()

#創建螢幕與文字宣告
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game--wallball--rect")
clock = pygame.time.Clock()

myfont = pygame.font.Font(None,60)

ball_img=pygame.image.load("ball.png")
ball_img_rs=pygame.transform.scale(ball_img, (50,50))
ball=ball_img_rs.get_rect()

# 遊戲迴圈
running = True
start=False

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
        ball.centerx, ball.centery = pygame.mouse.get_pos()
        if md[2]==True:
            start=True
    else:        
        if md[0]==True:
            start=False
        ball=ball.move(sx,sy)
        if ball.left<0 or ball.right>WIDTH:
            sx=-sx
            FPS = random.randint(150,300)
        if ball.top<0 or ball.bottom>HEIGHT:
            sy=-sy
            bg=(random.randint(0,255),random.randint(0,255),random.randint(0,255))    
    
    
    # 渲染(繪圖)
    screen.fill(bg)
    
    
    # *after* drawing everything, flip the display
    screen.blit(ball_img_rs, ball)
    pygame.display.flip()

pygame.quit()