import pygame,random

# 定義環境變數與顏色
WIDTH = 640
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WH=20

class Bb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((5,10))
        self.image.fill(WHITE)
        self.rect=self.image.get_rect()
    def update(self):
        self.rect.y=self.rect.y-5


class Prey(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((WH,WH))
        self.image.fill(BLUE)
        self.rect=self.image.get_rect()

class Shooter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((WH+5,WH+5))
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH/2
        self.rect.y=HEIGHT-50

ppp=pygame.sprite.Group()
sprites=pygame.sprite.Group()
bbs=pygame.sprite.Group()

for ii in range(60):
    pp=Prey()
    ppp.add(pp)
    pp.rect.x=random.randint(0, WIDTH-WH)
    pp.rect.y=random.randint(0,HEIGHT-100)
    

sprites.add(ppp)
sr=Shooter()
sprites.add(sr)

# 初始化宣告
pygame.init()
pygame.mixer.init()

#創建螢幕與文字宣告
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Shooting Game")
clock = pygame.time.Clock()

myfont = pygame.font.Font(None,60)


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

    
    mouseX, mouseY = pygame.mouse.get_pos()
    sr.rect.x=mouseX
    mBtn1, mBtn2, mBtn3 = pygame.mouse.get_pressed()
    if mBtn1:
        bb=Bb()
        bb.rect.x=mouseX
        bb.rect.y=HEIGHT-75
        bbs.add(bb)
        sprites.add(bbs)

    for b in bbs:
        if b.rect.y<-10:
            b.kill()
        hits = pygame.sprite.spritecollide(b, ppp, True)
        for p in hits:
            bbs.remove(b)
            sprites.remove(b)

        
        
    # 更新螢幕
    sprites.update()
    
    
    # 渲染(繪圖)
    screen.fill(BLACK)
    sprites.draw(screen)
    
    
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()




