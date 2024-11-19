import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class MainDisplay:
    def __init__(self):
        self.main_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    def fill_surface(self, color):
        self.main_display.fill(color)