import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from circleshape import *
from Shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    Shot = pygame.sprite.Group()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    dt = 0
    
    shot.containers = (Shot, updatable, drawable)
    player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    pl = player(x, y)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)

        for obj in asteroid:
            for b in Shot:
                if b.check_collision(obj):
                    b.kill()
                    obj.split()
            if obj.check_collision(pl):
                print("Game over!")
                sys.exit()
            
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        


# This line ensures the main() function is only called when this
# file is run directly; it won't run if it's imported as a module.
if __name__ == "__main__":
    main()