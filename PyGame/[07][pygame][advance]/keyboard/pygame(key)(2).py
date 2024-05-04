'''
PyGame--使用key來接收按鍵輸入
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
    pygame.display.set_caption("第2個Pygame接收按鍵輸入的程式")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    img=pygame.image.load("logo.png")
    
    ll=200
    tt=200
    ww=200
    hh=100
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        kk = pygame.key.get_pressed()
        if kk[pygame.K_RIGHT]:
            ll=ll-5
        if kk[pygame.K_LEFT]:
            ll=ll+5
        if kk[pygame.K_UP]:
            tt=tt+5
        if kk[pygame.K_DOWN]:
            tt=tt-5
        if kk[pygame.K_SPACE]:
            ww=ww+50
            hh=hh+50

        screen.fill(BLACK)
        screen.blit(pygame.transform.scale(img, (ww,hh)), (ll, tt))

        pygame.display.update()
        clock.tick(10)
        
if __name__ == '__main__':
    main()
