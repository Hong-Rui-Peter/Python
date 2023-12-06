'''
PyGame--time.Clock()--tick(每秒跑幾次)
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
tmr = 0

while True:
    tmr = tmr + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    txt = font.render(str(tmr), True, WHITE)
    screen.fill(BLACK)
    screen.blit(txt, [300, 200])
    pygame.display.update()
    clock.tick(10) #一秒十次
