import pygame
from constants import *
from surfaces import MainDisplay
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from circleshape import CircleShape

def game_loop():
    # set up the groups for classes/objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    # set up several components necessary for the logic within the loop
    game_display = MainDisplay()
    game_clock = pygame.time.Clock()
    dt = 0
    # set up objects representing player and asteroid field
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()
    while True:
        # provide a way to close the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # set the state of the loop each tick
        game_display.fill_surface("black")
        dt_ms = game_clock.tick(60) # 60 fps
        dt = dt_ms / 1000 # converting to seconds
        # main logic
        # update and draw entities
        for entity in updatable:
            entity.update(dt)
        for entity in drawable:
            entity.draw(game_display.main_display)
        # check lose condition
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collisions(shot):
                    asteroid.split()
                    shot.kill()
            if asteroid.check_collisions(player):
                print("Game over!")
                exit()
        # update displayed visuals
        pygame.display.flip()

def main():
    pygame.init()
    print("Starting asteroids!")
    game_loop()

if __name__ == "__main__":
    main()