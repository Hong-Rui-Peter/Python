'''
Pygame示範程式--wallball--sprite版
'''
# 載入模組
import pygame,random

class Ball(pygame.sprite.Sprite):
    def __init__(self,initial_position):
        super().__init__()
        self.image=pygame.image.load("ball.png")
        self.image=pygame.transform.scale(self.image, [50, 50])
        self.rect=self.image.get_rect()
        self.rect.topleft=initial_position
    def move(self,xx,yy):
        self.rect.x+=xx
        self.rect.y+=yy


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
pygame.display.set_caption("My Game--wallball--sprite")
clock = pygame.time.Clock()

myfont = pygame.font.Font(None,60)


# 遊戲迴圈
running = True
start=False

ball1=Ball((WIDTH/2,HEIGHT/2))

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
        ball1.rect.centerx, ball1.rect.centery = pygame.mouse.get_pos()
        if md[2]==True:
            start=True
    else:        
        if md[0]==True:
            start=False
        ball1.rect.move(sx,sy)
        if ball1.rect.left<0 or ball1.rect.right>WIDTH:
            sx=-sx
            FPS = random.randint(150,300)
        if ball1.rect.top<0 or ball1.rect.bottom>HEIGHT:
            sy=-sy
            bg=(random.randint(0,255),random.randint(0,255),random.randint(0,255))    
    
    
    # 渲染(繪圖)
    screen.fill(bg)
    
    
    # *after* drawing everything, flip the display
    screen.blit(ball1.image, ball1.rect)
    pygame.display.flip()

pygame.quit()