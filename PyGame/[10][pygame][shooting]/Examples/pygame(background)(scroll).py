'''
pygame--background scroll
'''
import pygame
import sys

# 載入影像
img_galaxy = pygame.image.load("galaxy.png")

bg_y = 0
WIDTH=720
HEIGHT=640

def main(): # 主要迴圈
    global bg_y

    pygame.init()
    pygame.display.set_caption("pygame--background scroll")
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 捲動背景
        speed=4
        bg_y = (bg_y+speed)%HEIGHT
        screen.blit(img_galaxy, [0, bg_y-HEIGHT])
        screen.blit(img_galaxy, [0, bg_y])

        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()
