import pygame, sys
from pygame.locals import *

# Inicializa el juego
pygame.init()

screen = pygame.display.set_mode(500, 400)
pygame.display.set_caption("Mi primera pantalla")

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()