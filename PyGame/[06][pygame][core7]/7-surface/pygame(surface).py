'''
pygame--Surface示範
'''
import sys
import pygame

SIZE=(480,640)
SIZE2=(240,320)

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('pygame Surface')
screen.fill('black')

#face = pygame.Surface(SIZE)
face = pygame.Surface(screen.get_size())
#face = pygame.Surface(SIZE2)
#face.set_alpha(2)
face.fill(color='pink')

img=pygame.image.load("logo.png")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
#    screen.blit(face, (0, 0))
#    screen.blit(pygame.transform.scale(img, SIZE), (0, 0))
#    face.blit(pygame.transform.scale(img, SIZE), (0, 0))
#    face.blit(pygame.transform.scale(img, SIZE2), (0, 0))
    pygame.display.flip() #更新屏幕內容

    