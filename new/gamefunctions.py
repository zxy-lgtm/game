import pygame
import sys

def game_start(gamegui):
    pass

def game_end():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()