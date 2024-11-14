import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape

def game_loop():
    # set up the groups for classes/objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    # set up several components necessary for the logic within the loop
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
        # set the timing of the loop
        dt_ms = game_clock.tick(60) # 60 fps
        dt = dt_ms / 1000 # converting to seconds
        # draw background
        screen.fill("black")
        # main logic to check updates, redraw objects, and refresh the displayed screen
        for entity in updatable:
            entity.update(dt)
        for entity in drawable:
            entity.draw(screen)
        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game over!")
                exit()
        pygame.display.flip()

def main():
    pygame.init()
    print("Starting asteroids!")
    game_loop()

if __name__ == "__main__":
    main()