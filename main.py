import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

    updatable = pygame.sprite.Group()
    updatable.add(player)

    drawable = pygame.sprite.Group()
    drawable.add(player)

    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))

        for sprite in updatable:
            sprite.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()


        dt = clock.tick(FPS)/1000


if __name__ == "__main__":
    main()
