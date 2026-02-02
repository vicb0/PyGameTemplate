import pygame

from components.Text import Text


class Button:
    def __init__(
        self,
        rect,
        text,
        font,
        on_click,
        bg,
        hover_bg,
        text_color
    ):
        self.rect = pygame.Rect(rect)
        self.text = Text(
            text,
            font,
            (self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2),
            text_color,
            center=True
        )
        self.on_click = on_click

        self.bg = bg
        self.hover_bg = hover_bg

        self.hovered = False

    def handle_hover(self, event):
        self.hovered = self.rect.collidepoint(event.pos)

    def handle_click(self, event):
        if self.hovered and event.button == 1:
            self.on_click()

    def draw(self, screen):
        color = self.hover_bg if self.hovered else self.bg
        pygame.draw.rect(screen, color, self.rect, border_radius=6)
        self.text.draw(screen)
