'''
pygame--sprite--創建一個圖片精靈群--作業--種草
'''
import pygame,sys,random
pygame.init()

class Grass(pygame.sprite.Sprite):
    def __init__(self,filename,initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(filename)
        self.image=pygame.transform.scale(self.image, [44, 44])
        self.rect=self.image.get_rect()
        self.rect.center=initial_position

grass=["grass1.jpg","grass2.png","grass6.jpg","grass3.jpg","grass4.jpg","grass5.jpg"]
clock = pygame.time.Clock()


Grassgroup=pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        
    screen=pygame.display.set_mode([640,480])
    screen.fill([255,255,255])
    xy = pygame.mouse.get_pos()
    mbtn=pygame.mouse.get_pressed()
    if mbtn[0]:
        fn=random.choice(grass)
        Grassgroup.add(Grass(fn,xy))
    
    Grassgroup.draw(screen)
#    for grasslist in Grassgroup.sprites():
#        screen.blit(grasslist.image,grasslist.rect)    

    pygame.display.update()
            
    clock.tick(10)
            
            