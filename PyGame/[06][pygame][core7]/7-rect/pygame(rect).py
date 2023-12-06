'''
pygame--Rect
'''
import pygame
import sys
 
pygame.init()
 
size = width, height = 300, 300

bg = (255, 255, 255) # RGB 白色
 
# 建立指定大小的視窗 Surface
screen = pygame.display.set_mode(size)
# 設定視窗標題
pygame.display.set_caption("Python Rect")

clock = pygame.time.Clock()
 
rect1 = pygame.Rect(0, 0, 100, 50)
rect2 = pygame.Rect(50, 50, 200, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg)
    
    pygame.draw.rect(screen, (255, 0, 0), rect1)
    pygame.draw.rect(screen, (0, 255, 0), rect2)
    pygame.draw.rect(screen, (0, 0, 255), rect1.fit(rect2))
    
    pygame.display.flip()
    
    clock.tick(10)