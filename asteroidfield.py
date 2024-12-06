import pygame
import random
from asteroid import Asteroid, StartAsteroid
from constants import *
from biome import Biome, biome_colors

class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, position, z_value, scale, velocity, biome):
        match biome:
            case Biome.START:
                asteroid = StartAsteroid(position.x, position.y, z_value, scale)
                asteroid.velocity = velocity

    def update(self, dt, current_biome):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0
            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            scale = random.randint(1, ASTEROID_KINDS)
            z_value = random.randint(1, 3)
            biome = current_biome
            self.spawn(position, z_value, scale, velocity, biome)

    def cleanup(self, asteroids):
        top_x = -ASTEROID_MAX_RADIUS
        bottom_x = SCREEN_WIDTH + ASTEROID_MAX_RADIUS
        left_y = -ASTEROID_MAX_RADIUS
        right_y = SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
        for asteroid in asteroids:
            if asteroid.position.x < top_x or asteroid.position.x > bottom_x:
                asteroid.kill()
            if asteroid.position.y < left_y or asteroid.position.y > right_y:
                asteroid.kill()