import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from logger import log_state
from player import Player

pyver = pygame.version.vernum

def main():
    print(f"Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Make Player
    player_x_start = SCREEN_WIDTH / 2
    player_y_start = SCREEN_HEIGHT / 2
    player = Player(PLAYER_RADIUS, player_x_start, player_y_start)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    # Game loop start --------------------------------------------------------------
    while (True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
   
        dt = clock.tick(60) / 1000
    
    # Game loop end -----------------------------------------------------------------

if __name__ == "__main__":
    main()
