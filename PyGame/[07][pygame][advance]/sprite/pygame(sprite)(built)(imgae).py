'''
pygame--sprite--創建一個圖片精靈
'''
import pygame,sys
pygame.init()

class Car(pygame.sprite.Sprite):
    def __init__(self,filename,initial_position):
        pygame.sprite.Sprite.__init__(self)
#        super().__init__()
        self.image=pygame.image.load(filename)
        self.image.set_colorkey("white")        
        self.image=pygame.transform.scale(self.image, [188, 188])
        self.rect=self.image.get_rect()
        self.rect.topleft=initial_position

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen=pygame.display.set_mode([640,480])
    screen.fill([0,0,0])
    c1=Car("car5.jpg",[0,0])
    c2=Car("car2.jpg",[0,300])
    screen.blit(c1.image,c1.rect)
    screen.blit(c2.image,c2.rect)
    pygame.display.update()
            
            
            