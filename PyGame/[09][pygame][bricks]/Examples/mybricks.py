'''
Pygame--我的第一個遊戲--打磚塊
'''
import pygame,random

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("ball.png")
        self.image=pygame.transform.scale(self.image, [30,30])
        self.rect=self.image.get_rect()
        self.sx=10
        self.sy=-10
        self.rect.x=WIDTH/2-15
        self.rect.y=HEIGHT-80
        

class Brick(pygame.sprite.Sprite):
    def __init__(self,xx,yy,cc):
        super().__init__()
        self.image=pygame.Surface((bw,bh))
        self.image.fill(cc)
        self.rect=self.image.get_rect()
        self.rect.x=xx
        self.rect.y=yy        


class Pad(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((150,20))
        self.image.fill((255,0,255))
        self.rect=self.image.get_rect()
        self.rect.x=WIDTH/2-75
        self.rect.y=HEIGHT-50
        self.speedx=10        
        



#定義環境常數
WIDTH=640
HEIGHT=480
FPS=30
row=5
col=8
bw=80
bh=20
COLOR=(0,0,0)

pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My First Game--打磚塊")
pygame.display.set_icon(pygame.image.load("icon.png"))
clock = pygame.time.Clock()


sprites=pygame.sprite.Group()
bricks=pygame.sprite.Group()
for ii in range(col):
    for jj in range(row):
        c=(random.randrange(0, 255),random.randrange(0, 255),random.randrange(0, 255))
        brick=Brick(ii*bw,jj*bh,c)
        bricks.add(brick)
        sprites.add(brick)
        
    
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sprites.update()    
    screen.fill(COLOR)
    sprites.draw(screen)
    pygame.display.flip()


pygame.quit()