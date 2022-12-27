import pygame
from settings import *

class Background(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        bg_image = pygame.image.load('graphics/environment/bg.png').convert()
        
        scale_factor = HEIGHT / bg_image.get_height()
        full_height = bg_image.get_height() * scale_factor
        full_width = bg_image.get_width() * scale_factor
        
        self.image = pygame.transform.scale(bg_image, (full_width, full_height))
        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def update(self, dt):
        self.pos.x -= 300 * dt
        self.rect.x = round(self.pos.x)

