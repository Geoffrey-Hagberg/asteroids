import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, SHIELD_RADIUS, SHIELD_ACTIVE_COLOR, SHIELD_INACTIVE_COLOR, SHIELD_FULL_CHARGE, SHIELD_RECHARGE_RATE, SHIELD_RECHARGE_SCALAR
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 # used in rotate and movement
        self.timer = 0 # used in shot cooldown timing
    def triangle(self): # defining the triangle representation within the circle object
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, "orange", self.triangle(), 2)
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
#    def move(self, dt):
#        forward = pygame.Vector2(0, 1).rotate(self.rotation)
#        self.position += forward * PLAYER_SPEED * dt
    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        spawn_position = self.position + forward * self.radius
        shot = Shot(spawn_position.x, spawn_position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN
    def update(self, dt):
        if self.timer > 0:
            self.timer -= dt
        keys = pygame.key.get_pressed()
#        if keys[pygame.K_w]:
#            self.move(dt)
#        if keys[pygame.K_s]:
#            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()

class Shield(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHIELD_RADIUS)
        self.active = True
        self.current_charge = 0
    def draw(self, screen):
        if self.active:
            color = SHIELD_ACTIVE_COLOR
        else:
            color = SHIELD_INACTIVE_COLOR
        pygame.draw.circle(screen, color, self.position, self.radius, 2)
    def update(self, dt):
        if not self.active:
            if self.current_charge >= SHIELD_FULL_CHARGE:
                self.active = True
                self.current_charge = 0
            else:
                self.current_charge += SHIELD_RECHARGE_RATE
    def asteroid_charge(self, asteroid):
        if not self.active:
            charge = asteroid.scale * SHIELD_RECHARGE_SCALAR
            self.current_charge += charge
    def collision(self, asteroid):
        self.active = False
        asteroid.kill()