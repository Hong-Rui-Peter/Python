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
    def update(self):
        global running
        if gstart:
            self.rect.x=self.rect.x+self.sx
            if self.rect.right>WIDTH:
                self.sx=-self.sx
            elif self.rect.x<0:
                self.sx=-self.sx
            self.rect.y=self.rect.y+self.sy
            if self.rect.top<0:
                self.sy=-self.sy
#            elif self.rect.bottom>HEIGHT:
#                self.sy=-self.sy
        if self.rect.top>HEIGHT:
            running=False
                
        

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
        self.speedx=15 
    def update(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if self.rect.x>0:
                self.rect.x=self.rect.x-self.speedx
            if gstart==False:    
                ball.rect.x=ball.rect.x-self.speedx 
                if ball.rect.x<0:
                    ball.rect.x=1
        elif key[pygame.K_RIGHT]:
            if self.rect.right<WIDTH:
                self.rect.x=self.rect.x+self.speedx
            if gstart==False:    
                ball.rect.x=ball.rect.x+self.speedx 
                if ball.rect.right>WIDTH:
                    ball.rect.right=WIDTH-1
        

def _newbricks():
    for ii in range(col):
        for jj in range(row):
            c=(random.randrange(0, 255),random.randrange(0, 255),random.randrange(0, 255))
            brick=Brick(ii*bw,jj*bh,c)
            bricks.add(brick)
            sprites.add(brick)



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

ball=Ball()
pad=Pad()

sprites=pygame.sprite.Group()
bricks=pygame.sprite.Group()
sprites.add(ball)
sprites.add(pad)
_newbricks()

kick=pygame.mixer.Sound("kick.mp3")
punch=pygame.mixer.Sound("punch.mp3")
pygame.mixer.mixer.set_volume(0.5)        
gstart=False    
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                gstart = True

    sprites.update() 
    if pygame.sprite.collide_rect(ball, pad):
        punch.play()
        ball.sy=-ball.sy
        if len(bricks)==0:
            _newbricks()
            
    if pygame.sprite.spritecollide(ball, bricks, True):
        kick.play()
        ball.sy=-ball.sy
        
    screen.fill(COLOR)
    sprites.draw(screen)
    pygame.display.flip()


pygame.quit()