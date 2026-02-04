import pygame

from consts.colors import WHITE


def draw_outlined_rect(screen, color, rect, outline_color=WHITE, outline_width=1):
    pygame.draw.rect(
        screen,
        color,
        rect
    )

    pygame.draw.rect(
        screen,
        outline_color,
        rect,
        width=outline_width
    )
