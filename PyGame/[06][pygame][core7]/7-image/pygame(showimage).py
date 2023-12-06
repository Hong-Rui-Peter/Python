'''
PyGame--顯示圖片
'''
import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption("第一次以Pygame顯示圖片")
    SIZE=(640,480)
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    img_bg = pygame.image.load("./images/sky.jpg").convert()
    img_p1 = pygame.image.load("./images/person1.jpg").convert()
    img_p2 = pygame.image.load("./images/person2.png").convert()
#    img_p2 = pygame.image.load("./images/person2.png").convert_alpha()
#    img_p1.set_colorkey("white")
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

#        screen.blit(img_bg, (0, 0))
        screen.blit(pygame.transform.scale(img_bg, SIZE), (0, 0))
        screen.blit(pygame.transform.scale(img_p1, (180,180)), (0, 0))
        screen.blit(pygame.transform.scale(img_p2, (180,180)), (200, 0))
        pygame.display.update()
        clock.tick(5)

if __name__ == '__main__':
    main()
