'''
PyGame--使用event來偵測鍵盤
'''
import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

def main():
    pygame.init()
    pygame.display.set_caption("Pygame-event-keyboard")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                txt1 = font.render("UNICODE: "+str(event.unicode), True, WHITE, GREEN)
                txt2 = font.render("K  E  Y: "+str(event.key), True, WHITE, BLUE)
                txt3 = font.render("M  O  D: "+str(event.mod), True, WHITE, RED)
                screen.fill(BLACK)
                screen.blit(txt1, [100, 100])
                screen.blit(txt2, [100, 200])
                screen.blit(txt3, [100, 300])
#                if event.key == pygame.K_ESCAPE:
                if event.key == 27:
                    pygame.quit()
                    sys.exit()
                    
        pygame.display.update()
        clock.tick(10)
        
if __name__ == '__main__':
    main()
