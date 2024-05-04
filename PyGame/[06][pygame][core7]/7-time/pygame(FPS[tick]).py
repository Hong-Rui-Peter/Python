'''
PyGame--pygame.time.Clock.get_fps()
'''
import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

pygame.init()
pygame.display.set_caption("Pygame-clock.tick")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 80)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fps=clock.get_fps()

    txt = font.render(str(fps), True, WHITE)
    screen.fill(BLACK)
    screen.blit(txt, [300, 200])
    pygame.display.update()
    clock.tick(30) #一秒30次
