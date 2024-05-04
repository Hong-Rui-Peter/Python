import pygame,sys
pygame.init()

size = (800,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pos = [size[0]/2, size[1]/2]
speed = 5
joystick = None

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if joystick:
        tt=joystick.get_button(0)
        rr=joystick.get_button(1)
        bb=joystick.get_button(2)
        ll=joystick.get_button(3)
        
        if ll:
            pos[0] -= speed
        if rr:
            pos[0] += speed 
        if tt:
            pos[1] -= speed 
        if bb:
            pos[1] += speed 
            
    else:
        if pygame.joystick.get_count() > 0:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            print("joystick initialized")

    screen.fill((0, 0, 255))
    pygame.draw.rect(screen, (255,255,255), (pos[0],pos[1], 10, 10))
    pygame.display.flip()