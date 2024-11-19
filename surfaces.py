import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class MainDisplay:
    def __init__(self):
        self.main_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    def fill_surface(self, color):
        self.main_display.fill(color)
    def render_surface(self, surface, position):
        self.main_display.blit(surface, position)

class TextDisplay:
    def __init__(self, dimensions, color, font, value):
        self.dimensions = dimensions
        self.text_color = color
        self.text_font = font
        self.text_value = value
    def update_value(self, new_value):
        self.text_value = new_value
    def render_text(self):
        text_surface = pygame.Surface(self.dimensions, pygame.SRCALPHA)
        text_surface.fill((0, 0, 0, 0), None)
        text = self.text_font.render(str(self.text_value), False, self.text_color)
        text_surface.blit(text, (0, 0))
        return text_surface