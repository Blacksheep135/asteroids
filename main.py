import pygame
from constants import *
import player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    dt = 0
    pl = player.player(x, y)
    
    player.containers = (updatable, drawable)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)
            
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