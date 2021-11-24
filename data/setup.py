import os
import pygame

# constants defining screen size
WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pandaball")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
OTHER = (100,100,100)
RED = (220,20,60)

FPS = 60
ROTATION_MAX_RIGHT = 11
ROTATION_MAX_LEFT = -11

COURT_WIDTH = 4
COURT_HEIGHT = 4

TIME_PER_UPDATE = 16.0  #Milliseconds
