# test.py

# size = h, w = 300, 200

# print(h)
# print(w)
# print(size)


import sys, pygame
pygame.init()

size = width, height = 512, 512
speed = [4, 1]
black = 0, 0, 0
gray = 50, 50, 50
stat = 1

screen = pygame.display.set_mode(size)

ball = pygame.image.load("./img/zha5.gif")
bg = pygame.image.load("./img/bg.png")
ballrect = pygame.Rect(256,256,128,128)


clock = pygame.time.Clock()


# mouse_rect = pygame.

while 1: 
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # draw bg
    screen.blit(bg, (0,0) )


    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1] 




    screen.blit(ball, ballrect)




    pygame.display.flip()









