'''
Pygame示範程式--My StarShip--v0
'''
# 載入模組
import pygame
import random

# 定義環境變數與顏色
WIDTH = 360
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# 初始化宣告
pygame.init()
pygame.mixer.init()

#創建螢幕與文字宣告
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My StarShip--v0")
clock = pygame.time.Clock()
myfont = pygame.font.Font("font.ttf", 48)


class Starship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((35,25))
        self.image.fill(WHITE)
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH/2
        self.rect.centery=HEIGHT*0.75
        self.speed=10
    def update(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.rect.y-=self.speed
            if self.rect.top<0:
                self.rect.top=0
        if key[pygame.K_DOWN]:
            self.rect.y+=self.speed
            if self.rect.bottom>HEIGHT:
                self.rect.bottom=HEIGHT
        if key[pygame.K_LEFT]:
            self.rect.x-=self.speed
            if self.rect.left<0:
                self.rect.left=0
        if key[pygame.K_RIGHT]:
            self.rect.x+=self.speed
            if self.rect.right>WIDTH:
                self.rect.right=WIDTH
    def fire(self):
        bullet=Bullet(self.rect.centerx-5,self.rect.top)
        sprites.add(bullet)
        bullets.add(bullet)
            
class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((20,30))
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(0,WIDTH-self.rect.width)
        self.rect.y=random.randrange(-100,0)
        self.speedx=random.randrange(-3,3) 
        self.speedy=random.randrange(3,10)
    def update(self):
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.top>HEIGHT or self.rect.left<0 or self.rect.right>WIDTH:
            self.rect.x=random.randrange(0,WIDTH-self.rect.width)
            self.rect.y=random.randrange(-100,0)
            self.speedy=random.randrange(2,10)
            self.speedx=random.randrange(-4,4)
        

class Bullet(pygame.sprite.Sprite):
    def __init__(self,xx,yy):
        super().__init__()
        self.image=pygame.Surface((10,25))
        self.image.fill(GREEN)
        self.rect=self.image.get_rect()
        self.rect.centerx=xx
        self.rect.centery=yy
        self.speedy=-10
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<0:
            self.kill()

        
    
sprites=pygame.sprite.Group()
bombs=pygame.sprite.Group()
bullets=pygame.sprite.Group()
starship=Starship()
sprites.add(starship)
for i in range(10):
    bomb=Bomb()
    sprites.add(bomb)
    bombs.add(bomb)



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
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                starship.fire()

    # 更新遊戲
    sprites.update()
    
    
    # 渲染(繪圖)
    screen.fill(BLACK)
    
    
    # 更新螢幕
    sprites.draw(screen)
    pygame.display.flip()

pygame.quit()