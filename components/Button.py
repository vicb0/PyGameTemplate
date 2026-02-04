import pygame

from components.Text import Text
from consts.colors import WHITE, BLACK
from utils.imageUtils import load_scaled_image


class Button:
    def __init__(
        self,
        text,
        font,
        rect,
        on_click,
        bg=None,
        hover_bg=None,
        image=None,
        hover_darkened=60,
        text_color=WHITE,
        center=False,
        border_radius=5
    ):
        self.center = center
        self.rect = pygame.Rect(rect)
        if self.center:
            self.rect.center = self.rect.topleft

        self.on_click = on_click
        self.border_radius = border_radius
        self.hovered = False

        self.text = None
        if text:
            self.text = Text(
                text,
                font,
                self.rect.center,
                text_color,
                center=True
            )

        self.bg = bg
        self.hover_bg = hover_bg or bg

        self.image = None
        self.hover_image = None
        if image:
            self.set_image(image, hover_darkened)

    def set_image(self, image, hover_darken=60):
        self.image = load_scaled_image(image, self.rect.size)
        self.hover_image = self.create_darkened_image(self.image, hover_darken)

    def create_darkened_image(self, surface, hover_darkened):
        dark = surface.copy()
        
        overlay = pygame.Surface(
            dark.get_size(),
            pygame.SRCALPHA
        )

        overlay.fill((*BLACK, hover_darkened))

        dark.blit(overlay, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

        return dark

    def set_position(self, pos):
        if self.center:
            self.rect.center = pos
        else:
            self.rect.topleft = pos

        if self.text:
            self.text.set_position(pos)

    def handle_hover(self, event):
        if hasattr(event, "pos"):
            self.hovered = self.rect.collidepoint(event.pos)

    def handle_click(self, event):
        if self.hovered and event.button == 1:
            self.on_click()

    def draw(self, screen):
        if self.image:
            img = self.hover_image if self.hovered else self.image
            screen.blit(img, self.rect)
        elif self.bg:
            color = self.hover_bg if self.hovered else self.bg
            pygame.draw.rect(screen, color, self.rect, border_radius=self.border_radius)
        else:
            raise Exception("Button must have an image or a background color")
        if self.text:
            self.text.draw(screen)
