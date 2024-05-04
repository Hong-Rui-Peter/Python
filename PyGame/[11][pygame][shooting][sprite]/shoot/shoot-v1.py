'''
太空射擊遊戲--V1
'''
import pygame,random

class Bullet(pygame.sprite.Sprite):
    def __init__(self,xx,yy):
        super().__init__()
        self.image=pygame.transform.scale(img_bt, (15,40))
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
        self.image=pygame.transform.scale(img_ss, (40,50))
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
        self.image=pygame.transform.scale(img_bb[random.randint(0,4)], (40,40))
        self.rect=self.image.get_rect()
        self.rect.centerx=random.randrange(0,WIDTH)
        self.rect.centery=random.randrange(-100,0)
        self.speedx=random.randrange(-4,4)
        self.speedy=random.randrange(3,10)
    def update(self):
        self.rect.x=self.rect.x+self.speedx
        self.rect.y=self.rect.y+self.speedy
        if self.rect.right<0 or self.rect.left>WIDTH or self.rect.bottom>HEIGHT:
            self.rect.centerx=random.randrange(0,WIDTH)
            self.rect.centery=random.randrange(-100,0)
            self.speedx=random.randrange(-4,4)
            self.speedy=random.randrange(3,10)
            
        



WIDTH = 360
HEIGHT = 480
FPS = 20
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)

# 初始化宣告
pygame.init()
pygame.mixer.init()

#創建螢幕與文字宣告
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Shooting Game--V1")
clock = pygame.time.Clock()

myfont = pygame.font.Font("font.ttf",48)

img_bg=pygame.image.load("./image/galaxy.png").convert()
img_ss=pygame.image.load("./image/starship.png").convert()
img_bt=pygame.image.load("./image/bullet.png").convert()
img_bb=[pygame.image.load("./image/bomb0.png").convert(),
        pygame.image.load("./image/bomb1.png").convert(),
        pygame.image.load("./image/bomb2.png").convert(),
        pygame.image.load("./image/bomb3.png").convert(),
        pygame.image.load("./image/bomb4.png").convert()]

# 遊戲迴圈
running = True
bg_y=0
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
    speed=10
    bg_y = (bg_y+speed)%WIDTH
    screen.blit(img_bg, [bg_y-WIDTH, 0])
    screen.blit(img_bg, [bg_y, 0])
    
    # 渲染(繪圖)
    sprites.update()
    hits=pygame.sprite.groupcollide(bullets, bbs, True, True)
    for hit in hits:
        bb=Bomb()
        bbs.add(bb)
        sprites.add(bb)
    die=pygame.sprite.spritecollide(ss, bbs, False)
    if die:
        break

        
    
    # *after* drawing everything, flip the display
    sprites.draw(screen)
    pygame.display.flip()

pygame.quit()


