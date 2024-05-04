'''
Pygame Racer--2.背景連動
'''
# 載入模組
import pygame,math


def make_course():  #建立賽道資料的函式(用三角函數計算並代入道路的彎曲狀態)
    for i in range(360):
        curve[BOARD+i] = int(8*math.sin(math.radians(i)))

# 定義環境變數與顏色
WIDTH = 800
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BOARD=120
CMAX=4*BOARD
curve=[0]*CMAX

BOARD_W=[0]*BOARD
BOARD_H=[0]*BOARD
car_y = 0
vv=0

for ii in range(BOARD):
    BOARD_W[ii]=10+(BOARD-ii)*(BOARD-ii)/12
    BOARD_H[ii]=3.4*(BOARD-ii)/BOARD

make_course()


# 初始化宣告
pygame.init()
pygame.mixer.init()



#創建螢幕與文字宣告
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game--racing-V2")
clock = pygame.time.Clock()
img_bg = pygame.image.load("image/bg.png").convert()

myfont = pygame.font.Font(None,60)


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
    key=pygame.key.get_pressed()
    if key[pygame.K_UP]:
        car_y=(car_y+1)%CMAX

    # 更新螢幕
    di=0
    board_x=[0]*BOARD
    for jj in range(BOARD):
        di=di+curve[(car_y+jj)%CMAX]
        board_x[jj] = 400 - BOARD_W[jj]/2 + di/2
    
    
    
    # 渲染(繪圖)
    vv=vv-di*key[pygame.K_UP]/30
    if vv<0:
        vv=vv+800
    if vv>=800:
        vv=vv-800
        
    screen.blit(img_bg,[vv-800,0])
    screen.blit(img_bg,[vv,0])

    sy = 400 # 開始繪製道路的位置
    for i in range(BOARD-1,0,-1):
        ux = board_x[i]
        uy = sy
        uw = BOARD_W[i]
        sy = sy + BOARD_H[i]
        bx = board_x[i-1]
        by = sy
        bw = BOARD_W[i-1]
        col = (168,168,168)
        pygame.draw.polygon(screen, col, [[ux, uy], [ux+uw, uy], [bx+bw, by], [bx, by]])

            
    
    
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()