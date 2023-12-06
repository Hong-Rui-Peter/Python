'''
Pygame示範程式--small
'''
import pygame

pygame.init()

screen = pygame.display.set_mode((480,300))
pygame.display.set_caption("My Game")


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
#    pygame.display.update()


pygame.quit()