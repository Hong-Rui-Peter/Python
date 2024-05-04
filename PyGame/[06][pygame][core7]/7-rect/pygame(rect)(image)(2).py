import pygame

pygame.init()

window_size = [800, 600]
screen = pygame.display.set_mode(window_size)
screen.fill("blue")
ball_img=pygame.image.load("ball.png")
ball_img_rs=pygame.transform.scale(ball_img, (100,100))
ball=ball_img_rs.get_rect(center=screen.get_rect().center)

# 顯示圖片到視窗上中間位置
screen.blit(ball_img_rs, ball)

# 這個是決定是否跳出遊戲迴圈的變數
run = False

while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
    # 更新畫面
    pygame.display.flip()

# 最後記得關閉 pygame
pygame.quit()