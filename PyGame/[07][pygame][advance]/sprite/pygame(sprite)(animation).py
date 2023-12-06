'''
pygame--sprite--使用圖片精靈群製作動畫
'''
import pygame,sys
import random
pygame.init()
class Car(pygame.sprite.Sprite):
    def __init__(self,filename,initial_position,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(filename)
        self.image=pygame.transform.scale(self.image, [88, 88])
        self.rect=self.image.get_rect()
        self.rect.topleft=initial_position
        self.speed=speed
    def move(self):
        self.rect=self.rect.move(self.speed)
        if self.rect.bottom < 0:   #當小車底部到達視窗頂部時，讓小車從下面出來    
            self.rect.top=480
            
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])
fn="car3.png"
locationgroup=([150,200],[350,300],[250,200])
Cargroup=pygame.sprite.Group()
for loc in locationgroup:
    speed=[0,random.choice([-10,-1])]
    Cargroup.add(Car(fn,loc,speed))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.time.delay(20)
    screen.fill([255,255,255])
    for carlist in Cargroup.sprites():
        carlist.move()
        screen.blit(carlist.image,carlist.rect)
    pygame.display.update()
    
    
    
    