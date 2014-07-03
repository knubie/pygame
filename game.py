import sys, pygame
from pygame.locals import *

pygame.init()

size = width, height = 640, 480
speed = [2, 4]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if ballrect.collidepoint(event.pos):
                speed[1] = -10
                if event.pos[0] < ballrect.centerx:
                    speed[0] = speed[0] + ((ballrect.centerx - event.pos[0]) * 0.2)
                else:
                    speed[0] = speed[0] - ((event.pos[0] - ballrect.centerx) * 0.2)

                

    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.bottom > height:
        speed[1] = -speed[1] * 0.9
        if ballrect.bottom > height:
            ballrect.bottom = height

    if abs(speed[1]) > 0:
        speed[1] = speed[1] + 0.4

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
