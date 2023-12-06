'''
pygame--mouse--image move--解答--請消除殘影,並且讓滑鼠位於圖片中心點
'''
import pygame

pygame.init()

clock = pygame.time.Clock()

window_size = [800, 600]
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("解答--請消除殘影,並且讓滑鼠位於圖片中心點")
ball_img=pygame.image.load("ball.png")
ball_img_rs=pygame.transform.scale(ball_img, (100,100))
ball=ball_img_rs.get_rect()

# 顯示圖片到視窗上中間位置

# 這個是決定是否跳出遊戲迴圈的變數
run = False

while not run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
    ball.centerx, ball.centery = pygame.mouse.get_pos()
    

    screen.fill("blue")
    screen.blit(ball_img_rs, ball)
    
    # 更新畫面
    pygame.display.flip()

# 最後記得關閉 pygame
pygame.quit()