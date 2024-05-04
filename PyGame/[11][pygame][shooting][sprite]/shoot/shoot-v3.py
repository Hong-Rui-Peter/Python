'''
太空射擊遊戲--V3
'''
import pygame,random,time

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
        self.radius=self.rect.width/2
        self.rect.centerx=WIDTH/2
        self.rect.centery=HEIGHT*0.75
        self.speed=10
        self.life=300
    def update(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.image=pygame.transform.scale(img_ss, (40,50))
            self.rect.top=self.rect.top-self.speed
            if self.rect.top<0:
                self.rect.top=0
        if key[pygame.K_DOWN]:
            self.image=pygame.transform.scale(img_ss, (40,50))
            self.rect.bottom=self.rect.bottom+self.speed
            if self.rect.bottom>HEIGHT:
                self.rect.bottom=HEIGHT
        if key[pygame.K_LEFT]:
            self.image=pygame.transform.scale(img_ssl, (40,50))
            self.rect.left=self.rect.left-self.speed
            if self.rect.left<0:
                self.rect.left=0
        if key[pygame.K_RIGHT]:
            self.image=pygame.transform.scale(img_ssr, (40,50))
            self.rect.right=self.rect.right+self.speed
            if self.rect.right>WIDTH:
                self.rect.right=WIDTH
    def fire(self):
        s_sound.play()
        bullet=Bullet(self.rect.centerx,self.rect.y)
        sprites.add(bullet)
        bullets.add(bullet)
        

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.transform.scale(img_bb[random.randint(0,4)], (40,40))
        self.rect=self.image.get_rect()
        self.radius=self.rect.width/2
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
            

class Boom(pygame.sprite.Sprite):
    def __init__(self,center):
        super().__init__()
        self.image=img_boom[0]
        self.rect=self.image.get_rect()
        self.rect.center=center
        self.frame=0
        self.last=pygame.time.get_ticks()
        self.rate=100
    def update(self):
        now=pygame.time.get_ticks()
        if now-self.last>self.rate:
            self.last=now
            self.frame=self.frame+1
            if self.frame==len(img_boom):
                self.kill()
            else:
                self.image=img_boom[self.frame]
        

def _show_start():
    screen.blit(img_bg,[0,0])
    text1=myfont.render("PYGAME射擊遊戲", False, YELLOW)
    screen.blit(text1,[50,100])
    text2=myfont.render("按任意鍵，遊戲開始", False, YELLOW)
    screen.blit(text2,[50,300])
    pygame.display.update()
    wait=True
    while wait:
        for event in pygame.event.get():
            if event.type==pygame.KEYUP:
                wait=False
    

WIDTH = 360
HEIGHT = 480
FPS = 20
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)

scores=0
# 初始化宣告
pygame.init()
pygame.mixer.init()

#創建螢幕與文字宣告
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Shooting Game--V3")
clock = pygame.time.Clock()

myfont = pygame.font.Font("font.ttf",32)

img_bg=pygame.image.load("./image/galaxy.png").convert()
img_ss=pygame.image.load("./image/starship.png").convert()
img_ssl=pygame.image.load("./image/starship_l.png").convert()
img_ssr=pygame.image.load("./image/starship_r.png").convert()
img_burner=pygame.image.load("./image/burner.png").convert()

img_bt=pygame.image.load("./image/bullet.png").convert()
img_bb=[pygame.image.load("./image/bomb0.png").convert(),
        pygame.image.load("./image/bomb1.png").convert(),
        pygame.image.load("./image/bomb2.png").convert(),
        pygame.image.load("./image/bomb3.png").convert(),
        pygame.image.load("./image/bomb4.png").convert()]

img_boom=[pygame.image.load("./image/explosion1.png").convert(),
        pygame.image.load("./image/explosion2.png").convert(),
        pygame.image.load("./image/explosion3.png").convert(),
        pygame.image.load("./image/explosion4.png").convert(),
        pygame.image.load("./image/explosion5.png").convert()]



# 遊戲迴圈
pygame.mixer.music.load("./sound/bgm.ogg")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
s_sound=pygame.mixer.Sound("./sound/shot.ogg")
pygame.mixer.Sound.set_volume(s_sound, 0.2)
e_sound=pygame.mixer.Sound("./sound/explosion.ogg")
pygame.mixer.Sound.set_volume(e_sound, 0.5)
over_sound=pygame.mixer.Sound("./sound/gameover.ogg")
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

_show_start()
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
    screen.blit(img_burner,[ss.rect.centerx-8,ss.rect.bottom+random.randint(-2,5)])
    text=myfont.render("SCORES:"+str(scores), False, YELLOW)
    screen.blit(text,[5,5])
    pygame.draw.rect(screen,RED,(50,50,ss.life,25))
    pygame.draw.rect(screen,WHITE,(50,50,300,25),5)
    
    # 渲染(繪圖)
    sprites.update()
    hits=pygame.sprite.groupcollide(bullets, bbs, True, True)
    for hit in hits:
        e_sound.play()
        scores=scores+100
        bb=Bomb()
        bbs.add(bb)
        sprites.add(bb)
        boom=Boom(hit.rect.center)
        sprites.add(boom)
    die=pygame.sprite.spritecollide(ss, bbs, True ,pygame.sprite.collide_circle)
    if die:
        ss.life=ss.life-100
        if ss.life<=0:
            over_sound.play()
            time.sleep(5)
            break

        
    
    # *after* drawing everything, flip the display
    sprites.draw(screen)
    pygame.display.flip()

pygame.quit()


