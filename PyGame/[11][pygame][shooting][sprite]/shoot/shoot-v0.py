'''
太空射擊遊戲--V0
'''
import pygame,random

class Bullet(pygame.sprite.Sprite):
    def __init__(self,xx,yy):
        super().__init__()
        self.image=pygame.Surface((10,15))
        self.image.fill(YELLOW)
        self.rect=self.image.get_rect()
        self.speedy=-10
        self.rect.centerx=xx
        self.rect.centery=yy
    def update(self):
        self.rect.y=self.rect.y+self.speedy
        if self.rect.bottom<0:
            self.kill()



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
            self.rect.top=self.rect.top-self.speed
            if self.rect.top<0:
                self.rect.top=0
        if key[pygame.K_DOWN]:
            self.rect.bottom=self.rect.bottom+self.speed
            if self.rect.bottom>HEIGHT:
                self.rect.bottom=HEIGHT
        if key[pygame.K_LEFT]:
            self.rect.left=self.rect.left-self.speed
            if self.rect.left<0:
                self.rect.left=0
        if key[pygame.K_RIGHT]:
            self.rect.right=self.rect.right+self.speed
            if self.rect.right>WIDTH:
                self.rect.right=WIDTH
    def fire(self):
        bullet=Bullet(self.rect.centerx,self.rect.y)
        sprites.add(bullet)
        bullets.add(bullet)
        

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((20,30))
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.rect.centerx=random.randrange(0,WIDTH)
        self.rect.centery=random.randrange(-100,0)
        self.speedx=random.randrange(-3,3)
        self.speedy=random.randrange(3,10)
    def update(self):
        self.rect.x=self.rect.x+self.speedx
        self.rect.y=self.rect.y+self.speedy
        if self.rect.left<0 or self.rect.right>WIDTH or self.rect.bottom>HEIGHT:
            self.rect.centerx=random.randrange(0,WIDTH)
            self.rect.centery=random.randrange(-100,0)
            self.speedx=random.randrange(-3,3)
            self.speedy=random.randrange(3,10)
            
        




WIDTH = 360
HEIGHT = 480
FPS = 30
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)

# 初始化宣告
pygame.init()
pygame.mixer.init()

#創建螢幕與文字宣告
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Shooting Game--V0")
clock = pygame.time.Clock()

myfont = pygame.font.Font("font.ttf",48)


# 遊戲迴圈
running = True

sprites=pygame.sprite.Group() #精靈總群組
ss=Starship()
sprites.add(ss)
bullets=pygame.sprite.Group()

bbs=pygame.sprite.Group() #地雷的精靈群組
for ii in range(8):
    bb=Bomb()
    bbs.add(bb)
    sprites.add(bb)

while running:
    # 控制游戲刷新速度
    clock.tick(FPS)
    # 處理(監聽)游戲事件
    for event in pygame.event.get():
        # 監聽是否關閉視窗
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_F1:
                ss.fire()

    # 更新螢幕
    screen.fill(BLACK)    
    
    # 渲染(繪圖)
    sprites.update()
    
    
    # *after* drawing everything, flip the display
    sprites.draw(screen)
    pygame.display.flip()

pygame.quit()


