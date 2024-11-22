import pygame
from constants import *

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
        text = self.text_font.render(str(self.text_value), False, self.text_color)
        text_surface.blit(text, (0, 0))
        return text_surface

class ProgressDisplay:
    def __init__(self, dimensions, position, progress_color, rate_color, value, maximum, rate):
        self.dimensions = dimensions
        self.inner_dimensions = (dimensions[0] - 8, dimensions[1] - 8)
        self.position = position
        self.inner_position = (position[0] + 4, position[1] + 4)
        self.progress_color = progress_color
        self.rate_color = rate_color
        self.value = value
        self.maximum = maximum
        self.rate = rate
    def update_value(self, new_value):
        self.value = new_value
    def render_frame(self, surface):
        frame_rect = pygame.Rect(self.position[0], self.position[1], self.dimensions[0], self.dimensions[1])
        frame = pygame.draw.rect(surface, "orange", frame_rect, 2)
    def render_rate(self, surface, progress):
        rate_rect = pygame.Rect(self.inner_position, (((self.inner_dimensions[0] * progress) + self.rate), self.inner_dimensions[1]))
        rate_bar = pygame.draw.rect(surface, self.rate_color, rate_rect)
    def render_bar(self, surface, progress):
        progress_rect = pygame.Rect(self.inner_position, ((self.inner_dimensions[0] * progress), self.inner_dimensions[1]))
        progress_bar = pygame.draw.rect(surface, self.progress_color, progress_rect)
    def render_progress(self, game_display):
        progress = self.value / self.maximum
        self.render_frame(game_display)
        self.render_rate(game_display, progress)
        self.render_bar(game_display, progress)
    def render_full(self, game_display, color):
        full_rect = pygame.Rect(self.inner_position, ((self.inner_dimensions[0]), self.inner_dimensions[1]))
        full_bar = pygame.draw.rect(game_display, color, full_rect)

class ShieldProgressDisplay(ProgressDisplay):
    def __init__(self, dimensions, position, progress_color, rate_color, value, maximum, rate):
        super().__init__(dimensions, position, progress_color, rate_color, value, maximum, rate)
    def render_shield(self, game_display, shield):
        if shield.active:
            self.render_frame(game_display)
            self.render_full(game_display, SHIELD_ACTIVE_COLOR)
        else:
            self.render_progress(game_display)