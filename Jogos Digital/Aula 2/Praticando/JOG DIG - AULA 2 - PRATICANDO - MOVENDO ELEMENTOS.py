import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

tank = pygame.image.load('tanque.jpg').convert()

x, y = 100, 100  # Posição inicial do tanque
move_x, move_y = 0, 0  # Movimento em X e Y
speed = 5  # Velocidade de movimento

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -speed
            if event.key == K_RIGHT:
                move_x = speed
            if event.key == K_UP:
                move_y = -speed
            if event.key == K_DOWN:
                move_y = speed
        
        if event.type == KEYUP:
            if event.key in (K_LEFT, K_RIGHT):
                move_x = 0
            if event.key in (K_UP, K_DOWN):
                move_y = 0

    x += move_x
    y += move_y

    screen.fill((255, 255, 255))  # Fundo branco
    screen.blit(tank, (x, y))  # Renderiza o tanque na nova posição

    pygame.display.update()