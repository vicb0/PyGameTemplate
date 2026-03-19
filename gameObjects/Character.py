import pygame

from components.Sprite import SpritesGroupManager, Sprite
from utils.imageUtils import load_scaled_image


class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = None
        self.vx = 0
        self.vy = 0
        self.speed = 200

        self.animations = SpritesGroupManager()

        self.animations.add("front", [
            Sprite(load_scaled_image("assets/Sprites/Char/Front/CharTopDown1.png"), 1/6),
            Sprite(load_scaled_image("assets/Sprites/Char/Front/CharTopDown2.png"), 1/6),
            Sprite(load_scaled_image("assets/Sprites/Char/Front/CharTopDown3.png"), 1/6),
            Sprite(load_scaled_image("assets/Sprites/Char/Front/CharTopDown4.png"), 1/6),
            Sprite(load_scaled_image("assets/Sprites/Char/Front/CharTopDown5.png"), 1/6),
            Sprite(load_scaled_image("assets/Sprites/Char/Front/CharTopDown6.png"), 1/6),
        ])

        self.animations.add("back", [
            Sprite(load_scaled_image("assets/Sprites/Char/Back/CharTopDown1.png"), 1/6),
            Sprite(load_scaled_image("assets/Sprites/Char/Back/CharTopDown2.png"), 1/6),
            Sprite(load_scaled_image("assets/Sprites/Char/Back/CharTopDown3.png"), 1/6),
            Sprite(load_scaled_image("assets/Sprites/Char/Back/CharTopDown4.png"), 1/6),
            Sprite(load_scaled_image("assets/Sprites/Char/Back/CharTopDown5.png"), 1/6),
            Sprite(load_scaled_image("assets/Sprites/Char/Back/CharTopDown6.png"), 1/6),
        ])

        self.animations.add("side", [
            Sprite(load_scaled_image("assets/Sprites/Char/Side/CharTopDown1.png"), 1/6),
            Sprite(load_scaled_image("assets/Sprites/Char/Side/CharTopDown2.png"), 1/6),
            Sprite(load_scaled_image("assets/Sprites/Char/Side/CharTopDown3.png"), 1/6),
            Sprite(load_scaled_image("assets/Sprites/Char/Side/CharTopDown4.png"), 1/6),
            Sprite(load_scaled_image("assets/Sprites/Char/Side/CharTopDown5.png"), 1/6),
            Sprite(load_scaled_image("assets/Sprites/Char/Side/CharTopDown6.png"), 1/6),
        ], store_flipped_x=True)

        self.change_state("front")

    def update_rect(self):
        self.rect = self.animations.get_curr_sprite().get_rect()
        self.rect.center = (self.x, self.y)

    def change_direction(self):  
        flip_x = False
        if self.vx != 0:
            state = "side"
            flip_x = self.vx > 0
        elif self.vy >= 0:
            state = "front"
        else:
            state = "back"

        self.change_state(state, flip_x, False)

    def change_state(self, state, flip_x=False, flip_y=False):
        self.animations.set_state(state, flip_x, flip_y)
        self.update_rect()

    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.vx = 0
        self.vy = 0

        if keys[pygame.K_LEFT]:
            self.vx = -1
        elif keys[pygame.K_RIGHT]:
            self.vx = 1

        if keys[pygame.K_UP]:
            self.vy = -1
        elif keys[pygame.K_DOWN]:
            self.vy = 1

        if self.vx != 0 and self.vy != 0:
            length = (self.vx**2 + self.vy**2)**(1/2)
            self.vx /= length
            self.vy /= length

        self.x += self.vx * self.speed * dt
        self.y += self.vy * self.speed * dt
        self.rect.center = (self.x, self.y)
        self.change_direction()
        self.animations.update(dt)

    def draw(self, screen):
        screen.blit(self.animations.get_curr_sprite(), self.rect)