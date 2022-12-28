import pygame
from settings import *

class Background(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        bg_image = pygame.image.load('graphics/environment/bg2.png').convert()
        
        scale_factor = HEIGHT / bg_image.get_height()
        full_height = bg_image.get_height() * scale_factor
        full_width = bg_image.get_width() * scale_factor
        full_sized_image = pygame.transform.scale(bg_image, (full_width, full_height))
        
        self.image = pygame.Surface((full_width * 2, full_height))
        self.image.blit(full_sized_image, (0,0))
        self.image.blit(full_sized_image, (full_width, 0))

        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def update(self, dt):
        self.pos.x -= 250 * dt

        if self.rect.centerx <= 0:
            self.pos.x = 0

        self.rect.x = round(self.pos.x)

class Bird(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        # image
        self.import_frames()
        self.frame_index = 1
        self.image = self.frames[self.frame_index]

        # rect
        self.rect = self.image.get_rect(center = (WIDTH/6, HEIGHT/2))
        self.pos = pygame.math.Vector2(self.rect.topleft)

        # movement
        self.gravity = 600
        self.direction = 0

    def import_frames(self):
        self.frames = []

        for i in range(1, 4):
            img = pygame.image.load(f'graphics/bird/bird{i}.png').convert_alpha()
            self.frames.append(img)

    def apply_gravity(self, dt):
        self.direction += self.gravity * dt
        self.pos.y += self.direction * dt
        self.rect.y = round(self.pos.y)

    def jump(self):
        self.direction = -400

    def animate(self, dt):
        self.frame_index += 5 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 1

        self.image = self.frames[int(self.frame_index)]

    def rotate(self):
        rotated_bird = pygame.transform.rotozoom(self.image, -self.direction * 0.05, 1)
        self.image = rotated_bird

    def update(self, dt):
        self.apply_gravity(dt)
        self.animate(dt)
        self.rotate()