import pygame, sys, time
from settings import *
from sprites import Background

class Game():
    def __init__(self) -> None:
        
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Flappy Bird')
        self.clock = pygame.time.Clock()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()

        # sprite setup
        Background(self.all_sprites)

    def run(self):
        last_time = time.time()

        while True:
            # delta time
            dt = time.time() - last_time
            last_time = time.time()

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # game logic
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.screen)

            pygame.display.update()
            self.clock.tick(FRAMERATE)
