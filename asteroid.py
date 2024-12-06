import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_SCALAR, Z1_COLOR, Z2_COLOR, Z3_COLOR
from biome import Biome, biome_colors

class Asteroid(CircleShape):
    def __init__(self, x, y, z, scale):
        self.z = z
        self.scale = scale
        calc_radius = scale * ASTEROID_SCALAR
        self.biome = Biome.START
        super().__init__(x, y, calc_radius)
    def draw(self, screen, current_biome):
        z1_color, z2_color, z3_color = biome_colors("asteroid", self.biome)
        match self.z:
            case 1:
                color = z1_color
            case 2:
                color = z2_color
            case 3:
                color = z3_color
        pygame.draw.circle(screen, color, self.position, self.radius, 2)
    def update(self, dt, current_biome):
        self.position += self.velocity * dt
    def split(self):
        pass

class StartAsteroid(Asteroid):
    def __init__(self, x, y, z, scale):
        super().__init__(x, y, z, scale)
        self.biome = Biome.START
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
            asteroid_one = StartAsteroid(self.position.x, self.position.y, z_one, new_scale)
            asteroid_two = StartAsteroid(self.position.x, self.position.y, z_two, new_scale)
            asteroid_one.velocity = vector_one * 1.2
            asteroid_two.velocity = vector_two * 1.2