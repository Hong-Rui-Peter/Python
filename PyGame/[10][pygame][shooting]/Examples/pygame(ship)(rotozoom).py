'''
pygame--rotozoom的用法
'''
import pygame
import sys

img_galaxy = pygame.image.load("galaxy.png")
img_sship = pygame.image.load("starship.png")

WIDTH=720
HEIGHT=640

def main():
    pygame.init()
    pygame.display.set_caption("Pygame--rotozoom的用法")
    screen = pygame.display.set_mode(((WIDTH,HEIGHT)))
    clock = pygame.time.Clock()
    ang = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(img_galaxy, [0, 0])

        ang = (ang+1)%360
        img_rz = pygame.transform.rotozoom(img_sship, ang, 1.0)
        x = WIDTH/2 - img_rz.get_width()/2
        y = HEIGHT/2 - img_rz.get_height()/2
        screen.blit(img_rz, [x, y])

        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()
