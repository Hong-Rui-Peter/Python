'''
pygame--sprite--創建一個方塊精靈
'''
import pygame,sys
pygame.init()

class Brick(pygame.sprite.Sprite):
    def __init__(self,color,initial_position):
        pygame.sprite.Sprite.__init__(self)
#        super().__init__()
        self.image = pygame.Surface([30,30])
        self.rect=self.image.get_rect()
        self.image.fill(color)
        self.rect.topleft=initial_position

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen=pygame.display.set_mode([640,480])
    screen.fill([255,255,255])
    b1=Brick([255,0,0],[50,100])
    b2=Brick([0,255,0],[150,200])
    screen.blit(b1.image,b1.rect)
    screen.blit(b2.image,b2.rect)
    pygame.display.update()
            
            
            