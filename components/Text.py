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
        lines = self.text.split("\n")

        rendered_lines = [
            self.font.render(line, self.antialias, self.color).convert_alpha()
            for line in lines
        ]

        line_height = self.font.get_linesize()

        width = max(line.get_width() for line in rendered_lines)
        height = line_height * len(rendered_lines)

        self.image = pygame.Surface((width, height), pygame.SRCALPHA)

        for i, line_surf in enumerate(rendered_lines):
            x = (width - line_surf.get_width()) // 2
            y = i * line_height
            self.image.blit(line_surf, (x, y))

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
