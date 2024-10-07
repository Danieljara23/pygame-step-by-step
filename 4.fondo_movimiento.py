import pygame, sys
import math
from pygame.locals import *
from config import *

# Inicializa el juego
pygame.init()
clock = pygame.time.Clock()


#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Endlesss Scroll ")


# Load Image
bg = pygame.image.load("assets/bg.png").convert()
[bg_width, bg_height] = bg.get_size()
bg_rect = bg.get_rect()

# game variables
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1


# game loop
run = True
while run:
  clock.tick(FPS)

  #drawing scrolling bg
  for i in range(0, tiles):
    screen.blit(bg,(i * bg_width + scroll,0))
    bg_rect.x = i * bg_width + scroll
    pygame.draw.rect(screen, (255, 0, 0), bg_rect, 1)

  # scroll backgroundn
  scroll -= 5

  # Reset scroll
  if abs(scroll) > bg_width:
    scroll = 0  
  
  #event handler
  for event in pygame.event.get():
    if event.type == QUIT:
      run = False
  
  pygame.display.update()
  


pygame.quit()