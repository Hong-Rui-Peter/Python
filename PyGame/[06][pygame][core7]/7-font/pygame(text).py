'''
PyGame--顯示文字
'''
import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

def main():
    pygame.init()
    pygame.display.set_caption("在Pygame顯示文字")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 80)
#    font = pygame.font.Font("font.ttf", 80)
#    font = pygame.font.Font('C:\\Windows\\Fonts\\CENTURY.TTF', 80)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        txt = font.render("Hello!!  Pygame!!", False, WHITE)
        screen.blit(txt, [100, 200])
        new_text = pygame.transform.rotozoom(txt, 45, 0.5)
        screen.blit(new_text, (100, 200))        
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
