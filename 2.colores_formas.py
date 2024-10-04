import pygame, sys
from pygame.locals import *
from config import *

# Inicializa el juego
pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Mi primera pantalla")

screen.fill(WHITE)

rect_1 = pygame.draw.rect(screen, RED, (100, 50, 100,50))
line_1 = pygame.draw.line(screen,GREEN,(100, 104), (199, 104), 2 )
circle_1 = pygame.draw.circle(screen, BLACK, (122, 250), 20, 21)
elipse_1 = pygame.draw.ellipse(screen, H61CD35, (275, 200, 40, 80), 10)

points = [(100, 300), (100, 100), (150, 100)]
polygon_1 = pygame.draw.polygon(screen, (0, 150, 255), points)

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    pygame.display.update()