from pygame import SRCALPHA
from pygame import draw
from pygame import mask
from pygame import mouse
from pygame.rect import Rect
from pygame.surface import Surface


class Mouse:
    def __init__(self, color, width=10, height=10):
        self.color = color
        self.rect = Rect(0, 0, width, height)

        surface = Surface((width, height), SRCALPHA)
        surface.fill((255, 255, 255))

        self.mask = mask.from_surface(surface)

    def set_color(self, color):
        self.color = color

    def update(self, dt):
        self.rect.center = mouse.get_pos()

    def draw(self, screen):
        draw.rect(screen, self.color, self.rect)

    def get_rect(self):
        return self.rect

    def get_mask(self):
        return self.mask
