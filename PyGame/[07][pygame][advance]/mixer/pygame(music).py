'''
PyGame--音樂與音效
'''
import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
CYAN  = (  0, 255, 255)

def main():
    pygame.init()
    pygame.display.set_caption("第一個利用Pygame輸出音效的程式")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)
    vv=0.5
    pygame.mixer.music.set_volume(vv)


    try:
        pygame.mixer.music.load("music.ogg")
        sound1 = pygame.mixer.Sound("soundeffect.ogg")
    except:
        print("找不到ogg檔案或是未與音訊裝置連接")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_p]:
            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.play(-1)
        elif key[pygame.K_s]:
            if pygame.mixer.music.get_busy() == True:
                pygame.mixer.music.stop()
        elif key[pygame.K_SPACE]:
            sound1.play()
        elif key[pygame.K_UP]:
            if vv<1:
                vv=vv+0.1
                pygame.mixer.music.set_volume(vv)
        elif key[pygame.K_DOWN]:
            if vv>0:
                vv=vv-0.1
                pygame.mixer.music.set_volume(vv)

        pos = pygame.mixer.music.get_pos()
        txt1 = font.render("BGM pos"+str(pos), True, WHITE)
        txt2 = font.render("[P]lay bgm : [S]top bgm : [SPACE] se", True, CYAN)
        screen.fill(BLACK)
        screen.blit(txt1, [100, 100])
        screen.blit(txt2, [100, 200])
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
