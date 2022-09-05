#!python3 

# Libraries and Classes
import pygame, sys
from settings import *
from level import Level

# Initialize pygame
pygame.init()

# Define screen and frames per second
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Instances
level = Level(level_map, screen)

# Main game loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((118, 168, 216))
    level.run()

    pygame.display.update()
    clock.tick(60)
