import pygame
from game import Game

pygame.init()

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grape Harvest")

clock = pygame.time.Clock()

game = Game(screen)

game.run()