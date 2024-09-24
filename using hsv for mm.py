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

    cx, cy = screen.get_width()/2, screen.get_height()/ 2

    h = math.atan2(y - cy,x - cx) * 180 / math.pi

    if h < 0:
        h += 360

    s = math.sqrt((x-cx)**2 + (y-cy)**2)

    if s > 100:
        s = 100

    mycolor.hsva = (h, s, 100)


    pygame.draw.circle(screen, mycolor, (cx, cy), 100)

    pygame.display.flip()
pygame.quit()