import pygame, sys
from pygame.locals import *
from config import *

# Inicializa el juego
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
# Background
background = pygame.image.load("assets/layer_1.png").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

x = 0



#Icono y titulo
pygame.display.set_caption("The Dark Knight")
icon = pygame.image.load("assets/idle_knight_1.png")
pygame.display.set_icon(icon)

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  relative_x = x % background.get_rect().width
  screen.blit(background,(relative_x - background.get_rect().width, 0))
  if relative_x < SCREEN_WIDTH:
    screen.blit(background, (relative_x, 0))
  x-=1
  pygame.display.update()
  clock.tick(FPS)
