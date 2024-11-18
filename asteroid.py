import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_SCALAR

class Asteroid(CircleShape):
    def __init__(self, x, y, scale):
        self.scale = scale
        calc_radius = scale * ASTEROID_SCALAR
        super().__init__(x, y, calc_radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.scale <= 1:
            return
        else:
            angle = random.uniform(20, 50)
            vector_one = self.velocity.rotate(angle)
            vector_two = self.velocity.rotate(-angle)
            new_scale = self.scale - 1
            asteroid_one = Asteroid(self.position.x, self.position.y, new_scale)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_scale)
            asteroid_one.velocity = vector_one * 1.2
            asteroid_two.velocity = vector_two * 1.2