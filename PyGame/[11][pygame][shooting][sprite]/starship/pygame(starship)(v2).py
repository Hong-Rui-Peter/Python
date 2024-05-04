'''
MyPygame--My StarShip--v2
'''
import pygame
import sys
import random,os


#遊戲初始設定
WIDTH=720
HEIGHT=640
FPS=60
bg_y = 0

pygame.init()
pygame.display.set_caption("MyPygame--My StarShip--v2")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
myfont = pygame.font.Font("font.ttf", 48)

img_galaxy = pygame.image.load("./image/galaxy.png").convert()
#img_galaxy = pygame.image.load(os.path.join("image","galaxy.png")).convert()
img_starship = pygame.image.load("./image/starship.png").convert()
img_starshipl = pygame.image.load("./image/starship_l.png").convert()
img_starshipr = pygame.image.load("./image/starship_r.png").convert()
img_bullet = pygame.image.load("./image/bullet.png").convert()
img_burner= pygame.image.load("./image/burner.png").convert()
img_bombs = []
for ii in range(5):
    img_bombs.append(pygame.image.load(os.path.join("image",f"bomb{ii}.png")).convert())

img_boom=[]
for ii in range(1,6):
    img_expl=pygame.image.load(os.path.join("image",f"explosion{ii}.png")).convert()
    img_boom.append(pygame.transform.scale(img_expl, (50,50)))


class Starship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(img_starship,(40,40))
        self.rect=self.image.get_rect()
        self.radius=self.rect.width/2
        self.rect.centerx=WIDTH/2
        self.rect.centery=HEIGHT*0.75
        self.speed=10
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.image = pygame.transform.scale(img_starship,(40,40))
            self.rect.y -= self.speed
            if self.rect.top < 0:
                self.rect.top = 0
        if key[pygame.K_DOWN]:
            self.image = pygame.transform.scale(img_starship,(40,40))
            self.rect.y += self.speed
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
        if key[pygame.K_LEFT]:
            self.image = pygame.transform.scale(img_starshipl,(40,40))
            self.rect.x -= self.speed
            if self.rect.left < 0:
                self.rect.left = 0
        if key[pygame.K_RIGHT]:
            self.image = pygame.transform.scale(img_starshipr,(40,40))
            self.rect.x += self.speed
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
    def fire(self):
        bullet=Bullet(self.rect.centerx,self.rect.top)
        sprites.add(bullet)
        bullets.add(bullet)
        

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        xy=random.choice([25,30,35,40,45,50])
        self.image = pygame.transform.scale(random.choice(img_bombs),(xy,xy))
        self.rect=self.image.get_rect()
        self.radius=self.rect.width/2
        self.rect.x=random.randrange(0,WIDTH-self.rect.width)
        self.rect.y=random.randrange(-100,0)
        self.speedy=random.randrange(2,10)
        self.speedx=random.randrange(-4,4)
    def update(self):
        self.rect.y+=self.speedy       
        self.rect.x+=self.speedx     
        if self.rect.top>HEIGHT or self.rect.left<0 or self.rect.right>WIDTH:
            self.rect.x=random.randrange(0,WIDTH-self.rect.width)
            self.rect.y=random.randrange(-100,0)
            self.speedy=random.randrange(2,10)
            self.speedx=random.randrange(-4,4)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,xx,yy):
        super().__init__()
        self.image = img_bullet
        self.rect=self.image.get_rect()
        self.rect.centerx=xx
        self.rect.centery=yy
        self.speedy=-10
    def update(self):
        self.rect.y+=self.speedy       
        if self.rect.bottom<0:
            self.kill()

   
class Boom(pygame.sprite.Sprite):
    def __init__(self,center):
        super().__init__()
        self.image = img_boom[0]
        self.rect=self.image.get_rect()
        self.rect.center=center
        self.frame=0
        self.last=pygame.time.get_ticks()
        self.rate=200
    def update(self):
        now= pygame.time.get_ticks()
        if now-self.last>self.rate:
            self.last=now
            self.frame+=1
            if self.frame==len(img_boom):
                self.kill()
            else:
                self.image=img_boom[self.frame]
  
            

sprites=pygame.sprite.Group()
bullets=pygame.sprite.Group()
bombs=pygame.sprite.Group()
starship=Starship()
sprites.add(starship)
for i in range(10):
    bomb=Bomb()
    sprites.add(bomb)
    bombs.add(bomb)



while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                starship.fire()
            

    # 更新遊戲

    sprites.update()
    collides=pygame.sprite.groupcollide(bombs,bullets,True,True)
    for collide in collides:
        bomb=Bomb()
        bombs.add(bomb)
        sprites.add(bomb)
        boom=Boom(collide.rect.center)
        sprites.add(boom)
    die=pygame.sprite.spritecollide(starship, bombs, False, pygame.sprite.collide_circle)
    if die:
        pygame.quit()
        sys.exit()
        


    # 更新畫面
    bg_y = (bg_y+4)%HEIGHT
    screen.blit(img_galaxy, [0, bg_y-HEIGHT])
    screen.blit(img_galaxy, [0, bg_y])
    screen.blit(img_burner,(starship.rect.centerx-9,starship.rect.y+starship.rect.height+random.randint(-2,5)))

    sprites.draw(screen)
    pygame.display.update()


