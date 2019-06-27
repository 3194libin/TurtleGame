import pygame
import sys

pygame.init()

size = width,height = 600,400
speed = [-2,1]
bg = (255,255,255)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("初次见面，请大家多多关照！")

turtle = pygame.image.load('turtle.jpg')
position = turtle.get_rect()

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = [-1,0]
            if event.type == pygame.K_RIGHT:
                speed = [1, 0]
            if event.type == pygame.K_UP:
                speed = [0,-1]
            if event.type == pygame.K_DOWN:
                speed = [0,1]
    position = position.move(speed)

    if position.left<0 or position.right>width:
        turtle = pygame.transform.flip(turtle,True,False)
        speed[0] = -speed[0]
    if position.top<0 or position.bottom>height:
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(turtle,position)
    pygame.display.flip()
    pygame.time.delay(10)
