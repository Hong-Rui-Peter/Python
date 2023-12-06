'''
Pygame Racer--4.上下坡起伏+道路標線
'''
# 載入模組
import pygame,math


def make_course():  #建立賽道資料的函式(用三角函數計算並代入道路的彎曲狀態)
    for i in range(CMAX):
        updown[i] = int(8*math.sin(math.radians(i)))

# 定義環境變數與顏色
WIDTH = 800
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW= (255, 224,   0)

BOARD=120
CMAX=4*BOARD
curve=[0]*CMAX
updown = [0]*CMAX

BOARD_W=[0]*BOARD
BOARD_H=[0]*BOARD
BOARD_UD=[0]*BOARD
car_y = 0
vv=0

for ii in range(BOARD):
    BOARD_W[ii]=10+(BOARD-ii)*(BOARD-ii)/12
    BOARD_H[ii]=3.4*(BOARD-ii)/BOARD
    BOARD_UD[ii] = 2*math.sin(math.radians(ii*1.5))

make_course()


# 初始化宣告
pygame.init()
pygame.mixer.init()



#創建螢幕與文字宣告
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game--racing-V4")
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
    ud=0
    board_x=[0]*BOARD
    board_ud=[0]*BOARD
    for jj in range(BOARD):
        di += curve[(car_y+jj)%CMAX]
        ud += updown[(car_y+jj)%CMAX]
        board_x[jj] = 400 - BOARD_W[jj]/2 + di/2
        board_ud[jj] = ud/30
    
    hh=400+int(ud/3)
    sy = hh # 開始繪製道路的位置
    
    
    # 渲染(繪圖)
    vv=vv-di*key[pygame.K_UP]/100
    if vv<0:
        vv=vv+800
    if vv>=800:
        vv=vv-800
        
    screen.fill((0, 56, 255)) # 天空的顏色
    screen.blit(img_bg,[vv-800,hh-400])
    screen.blit(img_bg,[vv,hh-400])

    for i in range(BOARD-1,0,-1):
        ux = board_x[i]
        uy = sy - BOARD_UD[i]*board_ud[i]
        uw = BOARD_W[i]
        sy = sy + BOARD_H[i]*(600-hh)/200
        bx = board_x[i-1]
        by = sy - BOARD_UD[i-1]*board_ud[i-1]
        bw = BOARD_W[i-1]
        col = (160,160,160)
        pygame.draw.polygon(screen, col, [[ux, uy], [ux+uw, uy], [bx+bw, by], [bx, by]])
        
        #標黃線
        if int(car_y+i)%15<=5:
            pygame.draw.polygon(screen, YELLOW, [[ux, uy], [ux+uw*0.04, uy], [bx+bw*0.04, by], [bx, by]])
            pygame.draw.polygon(screen, YELLOW, [[ux+uw*0.96, uy], [ux+uw, uy], [bx+bw, by], [bx+bw*0.96, by]])
        #標白線
        if int(car_y+i)%15<=5:
            pygame.draw.polygon(screen, WHITE, [[ux+uw*0.24, uy], [ux+uw*0.26, uy], [bx+bw*0.26, by], [bx+bw*0.24, by]])
            pygame.draw.polygon(screen, WHITE, [[ux+uw*0.48, uy], [ux+uw*0.52, uy], [bx+bw*0.52, by], [bx+bw*0.48, by]])
            pygame.draw.polygon(screen, WHITE, [[ux+uw*0.74, uy], [ux+uw*0.76, uy], [bx+bw*0.76, by], [bx+bw*0.74, by]])
            
            
    
    
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()