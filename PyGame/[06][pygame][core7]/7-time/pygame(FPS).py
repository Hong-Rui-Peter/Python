'''
Pygame示範程式--FPS
'''
# 載入模組
import time
import pygame

# 定義環境變數
WIDTH = 360
HEIGHT = 480
FPS = 30

# 定義顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 初始化宣告
pygame.init()
pygame.mixer.init()

#創建螢幕與文字宣告
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game--FPS")
clock = pygame.time.Clock()

myfont = pygame.font.Font(None,60)

# 遊戲迴圈
running = True
count = 0
start = time.time()

while running:
    # 控制游戲刷新速度
    clock.tick(FPS)
    # 處理(監聽)游戲事件
    for event in pygame.event.get():
        # 監聽是否關閉視窗
        if event.type == pygame.QUIT:
            running = False

    # 更新螢幕
    count=count+1
    now = time.time()
    try:
        fps = count/(now-start)
    except:
        fps=1
        continue
    fpsImage = myfont.render(str(fps), True, WHITE)
    # 渲染(繪圖)
    screen.fill(BLACK)
    screen.blit(fpsImage, (10, 100))
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()