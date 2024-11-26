import pygame
from constants import *
from surfaces import MainDisplay, TextDisplay, ProgressDisplay, ShieldProgressDisplay
from player import Player, Shield
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from circleshape import CircleShape
from score import update_score, check_score, set_up_score

def game_loop():
    set_up_score("./local/high_score.txt")
    # set up the groups for classes/objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shield.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    # set up objects representing various entities and values
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    shield = Shield((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()
    current_score = 0
    # set up components necessary for the display and logic
    game_display = MainDisplay()
    score_display = TextDisplay(SCORE_DIMENSIONS, "orange", SCORE_FONT, current_score)
    shield_charge_display = ShieldProgressDisplay(SHIELD_CHARGE_DIMENSIONS, SHIELD_CHARGE_POSITION, SHIELD_CHARGE_PROGRESS_COLOR, SHIELD_CHARGE_RATE_COLOR, shield.current_charge, SHIELD_FULL_CHARGE, SHIELD_RECHARGE_RATE)
    game_clock = pygame.time.Clock()
    dt = 0
    while True:
        # provide a way to close the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                check_score(current_score)
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
        shield_charge_display.update_value(shield.current_charge)
        asteroid_field.cleanup(asteroids)
        # check collision conditions
        for asteroid in asteroids:
            other_asteroids = asteroids.copy()
            other_asteroids.remove(asteroid)
            for other_asteroid in other_asteroids:
                if asteroid.z == other_asteroid.z:
                    if asteroid.check_collisions(other_asteroid):
                        asteroid.split()
                        other_asteroid.split()
            for shot in shots:
                if asteroid.check_collisions(shot):
                    current_score = update_score(asteroid, current_score)
                    score_display.update_value(current_score)
                    shield.asteroid_charge(asteroid)
                    asteroid.split()
                    shot.kill()
            if shield.active:
                if asteroid.check_collisions(shield):
                    shield.collision(asteroid)
            else:
                if asteroid.check_collisions(player):
                    print("Game over!")
                    check_score(current_score)
                    exit()
        # update displayed visuals
        game_display.render_surface(score_display.render_text(), SCORE_POSITION)
        shield_charge_display.render_shield(game_display.main_display, shield)
        pygame.display.flip()

def main():
    pygame.init()
    print("Starting oids!")
    game_loop()

if __name__ == "__main__":
    main()