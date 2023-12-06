'''
PyGame--time.set_timer()
'''
import pygame,sys 

pygame.init() 
screen = pygame.display.set_mode((128, 128)) 
clock = pygame.time.Clock() 
counter=10 
text = '10' 
pygame.time.set_timer(pygame.USEREVENT, 1000) 
font = pygame.font.SysFont('Consolas', 30) 
while True: 
    for e in pygame.event.get(): 
        if e.type == pygame.USEREVENT: 
            counter -= 1
            if counter>0:
                text = str(counter)
            else:
                text='boom!' 
        if e.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        else: 
            screen.fill((255, 255, 255)) 
            screen.blit(font.render(text, True, (0, 0, 0)), (32, 48)) 
            pygame.display.flip() 
            clock.tick(60) 
