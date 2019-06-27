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

    position = position.move(speed)

    if position.left<0 or position.right>width:
        turtle = pygame.transform.flip(turtle,True,False)
        speed[0] = -speed[0]
    if position.top<0 or position.bottom>height:
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(turtle,position)
    pygame.display.filp()
