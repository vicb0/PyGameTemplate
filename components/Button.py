import pygame


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
        self.text = text
        self.font = font
        self.on_click = on_click

        self.bg = bg
        self.hover_bg = hover_bg
        self.text_color = text_color

        self.hovered = False

        self.text_surface = font.render(text, True, text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def handle_hover(self, event):
        self.hovered = self.rect.collidepoint(event.pos)

    def handle_click(self, event):
        if self.hovered and event.button == 1:
            self.on_click()

    def draw(self, screen):
        color = self.hover_bg if self.hovered else self.bg
        pygame.draw.rect(screen, color, self.rect, border_radius=6)
        screen.blit(self.text_surface, self.text_rect)
