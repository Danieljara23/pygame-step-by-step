import pygame, sys
from pygame.locals import *

# Inicializa el juego
pygame.init()

screen = pygame.display.set_mode((1000, 600))

# Background
background = pygame.image.load("assets/layer_1.png")
background = pygame.transform.scale(background, (1000, 600))
screen.blit(background,(0, 0))


#Icono y titulo
pygame.display.set_caption("The Dark Knight")
icon = pygame.image.load("assets/idle_knight_1.png")
pygame.display.set_icon(icon)

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    pygame.display.update()