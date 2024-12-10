import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, SHIELD_ACTIVE_COLOR
from biome import biome_colors

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    def draw(self, screen, current_biome):
        color = SHIELD_ACTIVE_COLOR
        pygame.draw.circle(screen, color, self.position, self.radius, 2)
    def update(self, dt, current_biome):
        self.position += self.velocity * dt