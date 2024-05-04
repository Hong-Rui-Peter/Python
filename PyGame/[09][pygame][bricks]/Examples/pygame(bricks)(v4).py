'''
Pygame示範程式--打磚塊(v4)--完成版
'''
# 載入模組
import pygame
import random

# 定義環境變數與顏色
WIDTH = 360
HEIGHT = 480
FPS = 30

COLOR=(0,0,0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("ball.png")
        self.image=pygame.transform.scale(self.image, [30, 30])
        self.rect=self.image.get_rect()
        self.speedx=10
        self.speedy=-10
        self.rect.x=WIDTH/2-15
        self.rect.y=HEIGHT-80
    def update(self):
        global running,COLOR
        if gstart==True:
            self.rect.x+=self.speedx
            if self.rect.right>=WIDTH:
                self.speedx=-self.speedx
                COLOR=(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
            if self.rect.left<=0:
                self.speedx=-self.speedx
                COLOR=(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
            self.rect.y+=self.speedy
            if self.rect.top<=0:
                self.speedy=-self.speedy
            if self.rect.bottom>=HEIGHT:
                running = False
           
        
class Pad(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((150,20))
        self.image.fill(GREEN)
        self.rect=self.image.get_rect()
        self.rect.x=WIDTH/2-70
        self.rect.y=HEIGHT-50
        self.speedx=10
    def update(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x-=self.speedx
            if self.rect.left<0:
                self.rect.left=0
            if gstart==False:
                ball.rect.x-=self.speedx
                if ball.rect.left<0:
                    ball.rect.left=1
        if key[pygame.K_RIGHT]:
            self.rect.x+=self.speedx
            if gstart==False:
                ball.rect.x+=self.speedx
                if ball.rect.right>WIDTH:
                    ball.rect.right=WIDTH-1
            if self.rect.right>WIDTH:
                self.rect.right=WIDTH
        
class Brick(pygame.sprite.Sprite):
    def __init__(self,xx,yy,cc):
        super().__init__()
        self.image=pygame.Surface((60,20))
        self.image.fill(cc)
        self.rect=self.image.get_rect()
        self.rect.x=xx
        self.rect.y=yy




# 初始化宣告
pygame.init()
pygame.mixer.init()

#創建螢幕與文字宣告
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game--打磚塊(v4)--完成版")
clock = pygame.time.Clock()

myfont = pygame.font.Font(None,60)


sprites=pygame.sprite.Group()
ball=Ball()
sprites.add(ball)
pad=Pad()
sprites.add(pad)
bricks=pygame.sprite.Group()
for ii in range(6):
    for jj in range(5):
        ccc=(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        brick=Brick(ii*60,jj*20,ccc)
        bricks.add(brick)
        sprites.add(brick)


# 遊戲迴圈
running = True
gstart = False

while running:
    # 控制游戲刷新速度
    clock.tick(FPS)
    # 處理(監聽)游戲事件
    for event in pygame.event.get():
        # 監聽是否關閉視窗
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                gstart=True

    # 更新遊戲
    sprites.update()    
    nice=pygame.sprite.collide_rect(ball, pad)
    if nice:
        ball.speedy=-ball.speedy
    hit=pygame.sprite.spritecollide(ball, bricks, True)
    if hit:
        ball.speedy=-ball.speedy
        
    
    
    # 渲染(繪圖)
    screen.fill(COLOR)
    
    
    # *after* drawing everything, flip the display
    sprites.draw(screen)
    pygame.display.flip()

pygame.quit()