'''
pygame--sprite--創建一個圖片精靈群
'''
import pygame,sys
pygame.init()

class Car(pygame.sprite.Sprite):
    def __init__(self,filename,initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(filename)
        self.image=pygame.transform.scale(self.image, [88, 88])
        self.rect=self.image.get_rect()
        self.rect.topleft=initial_position

fn="grass.png"

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen=pygame.display.set_mode([640,480])
    screen.fill([255,255,255])
    locationgroup=([0,0],[200,200],[300,0])
    Cargroup=pygame.sprite.Group()
    for loc in locationgroup:
        Cargroup.add(Car(fn,loc))
    
    for carlist in Cargroup.sprites():
        screen.blit(carlist.image,carlist.rect)    
    pygame.display.update()
            
            
            