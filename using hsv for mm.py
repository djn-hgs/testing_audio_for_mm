import math

import pygame

pygame.init()

screen = pygame.display.set_mode((640, 240))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    mycolor = pygame.Color(0, 0 , 0)

    x,y = pygame.mouse.get_pos()

    a = math.atan2(y - screen.get_height()/ 2,x - screen.get_width()/2 ) * 180 / math.pi

    if a < 0:
        a += 360


    mycolor.hsva = (a, 100, 100)


    pygame.draw.circle(screen, mycolor, (screen.get_width()/2, screen.get_height()/2), 100)

    pygame.display.flip()
pygame.quit()