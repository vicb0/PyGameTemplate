import pygame


class Text:
    def __init__(
        self,
        text,
        font,
        pos,
        color,
        center=False,
        antialias=True
    ):
        self.text = text
        self.font = font
        self.pos = pos
        self.color = color
        self.center = center
        self.antialias = antialias

        self.image = None
        self.rect = None

        self._render()

    def _render(self):
        self.image = self.font.render(
            self.text,
            self.antialias,
            self.color
        ).convert_alpha()

        self.rect = self.image.get_rect()
        self.set_position(self.pos)

    def set_text(self, new_text):
        if new_text != self.text:
            self.text = new_text
            self._render()

    def set_color(self, color):
        self.color = color
        self._render()

    def set_position(self, pos):
        self.pos = pos

        if self.center:
            self.rect.center = pos
        else:
            self.rect.topleft = pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)
