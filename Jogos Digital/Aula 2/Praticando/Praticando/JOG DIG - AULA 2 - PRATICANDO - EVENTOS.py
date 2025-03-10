import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (1200, 800)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

tank = pygame.image.load('tanque.png').convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Obtém a posição atual do mouse
    x, y = pygame.mouse.get_pos()
    
    screen.fill((255, 255, 255))  # Fundo branco
    screen.blit(tank, (x, y))  # Renderiza o tanque na posição do mouse

    pygame.display.update()