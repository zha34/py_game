# test.py

# size = h, w = 300, 200

# print(h)
# print(w)
# print(size)


import sys, pygame
pygame.init()

size = width, height = 512, 512
speed = [2, 2]
black = 0, 0, 0
gray = 50, 50, 50
stat = 1

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # ballrect = ballrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    if stat == 1: 
    	screen.fill(black)
    	stat *= -1
    else:
    	screen.fill(gray)
    	stat *= -1
    	
    	

    # screen.blit(ball, ballrect)
    pygame.display.flip()