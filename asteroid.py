import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_SCALAR, Z1_COLOR, Z2_COLOR, Z3_COLOR

class Asteroid(CircleShape):
    def __init__(self, x, y, z, scale):
        self.z = z
        self.scale = scale
        calc_radius = scale * ASTEROID_SCALAR
        super().__init__(x, y, calc_radius)
    def get_color(self):
        if self.z == 1:
            return Z1_COLOR
        elif self.z == 2:
            return Z2_COLOR
        elif self.z == 3:
            return Z3_COLOR
    def draw(self, screen):
        color = self.get_color()
        pygame.draw.circle(screen, color, self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def get_split_z(self):
        if self.z == 1:
            z_one = 2
            z_two = 3
        elif self.z == 2:
            z_one = 1
            z_two = 3
        else:
            z_one = 1
            z_two = 2
        return z_one, z_two
    def split(self):
        self.kill()
        if self.scale <= 1:
            return
        else:
            angle = random.uniform(20, 50)
            vector_one = self.velocity.rotate(angle)
            vector_two = self.velocity.rotate(-angle)
            z_one, z_two = self.get_split_z()
            new_scale = self.scale - 1
            asteroid_one = Asteroid(self.position.x, self.position.y, z_one, new_scale)
            asteroid_two = Asteroid(self.position.x, self.position.y, z_two, new_scale)
            asteroid_one.velocity = vector_one * 1.2
            asteroid_two.velocity = vector_two * 1.2