'''
Pygame示範程式--display
'''
# 載入模組
import pygame

# 定義環境變數與顏色
WIDTH = 360
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# 初始化宣告
pygame.init()
pygame.mixer.init()

#創建螢幕與文字宣告
#print(pygame.display.Info())
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
#screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.NOFRAME)
#screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
#print(pygame.display.Info())

pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

myfont = pygame.font.Font(None,60)

icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)
# 遊戲迴圈
running = True

while running:
    # 控制游戲刷新速度
    clock.tick(FPS)
    # 處理(監聽)游戲事件
    for event in pygame.event.get():
        # 監聽是否關閉視窗
        if event.type == pygame.QUIT:
            running = False

    # 更新螢幕
    
    
    
    # 渲染(繪圖)
    screen.fill(BLACK)
    
    
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()