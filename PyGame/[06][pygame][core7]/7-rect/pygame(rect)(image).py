'''
pygame--Rect--image
'''
import pygame
import sys
 
pygame.init()
 
size = width, height = 800, 600

bg = (255, 255, 255) # RGB 白色
 
# 建立指定大小的視窗 Surface
screen = pygame.display.set_mode(size)
# 設定視窗標題
pygame.display.set_caption("Python Rect-image")

clock = pygame.time.Clock()
 
logo=pygame.image.load("logo.png")
logo_rect=logo.get_rect()


print("X,Y: ",logo_rect.x,logo_rect.y)
print("-"*20)

print("Top: ",logo_rect.top)
print("Left: ",logo_rect.left)
print("Bottom: ",logo_rect.bottom)
print("Right: ",logo_rect.right)
print("-"*20)

print("TopLeft: ",logo_rect.topleft)
print("BottomLeft: ",logo_rect.bottomleft)
print("BottomRight: ",logo_rect.bottomright)
print("TopRight: ",logo_rect.topright)
print("-"*20)

print("MidTop: ",logo_rect.midtop)
print("MidLeft: ",logo_rect.midleft)
print("MidBottom: ",logo_rect.midbottom)
print("MidRight: ",logo_rect.midright)
print("-"*20)

print("Center: ",logo_rect.center)
print("CenterX: ",logo_rect.centerx)
print("CenterY: ",logo_rect.centery)
print("-"*20)

print("Size: ",logo_rect.size)
print("Width: ",logo_rect.width)
print("Height: ",logo_rect.height)
print("-"*20)

print("W: ",logo_rect.w)
print("H: ",logo_rect.h)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg)
        
    screen.blit(logo,logo_rect)
    pygame.display.flip()
    
    clock.tick(10)