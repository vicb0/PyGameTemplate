import pygame

from consts.colors import *
from components.Button import Button
from components.Text import Text
from consts import metadata
from core.ScreenInterface import ScreenInterface
from utils.imageUtils import load_scaled_image


# This is an example of how to use this framework.
SCREEN_TITLE = getattr(metadata, "SCREEN_TITLE", "Pygame")

class MainMenu(ScreenInterface):
    def __init__(self, game):
        super().__init__(game)
        
        self.drawables = []
        self.background = None
        self.input_linker = {
            pygame.MOUSEMOTION: self.on_mouse_motion,
            pygame.MOUSEBUTTONDOWN: self.on_click
        }

    def on_mouse_motion(self, event):
        for obj in self.drawables:
            if getattr(obj, "handle_hover", None):
                obj.handle_hover(event)

    def on_click(self, event):        
        for obj in self.drawables:
            if getattr(obj, "handle_click", None):
                obj.handle_click(event)

    def event_handler(self, event):
        func = self.input_linker.get(event.type)
        if func:
            func(event)

    def update(self, dt):
        for obj in self.drawables:
            if getattr(obj, "update", None):
                obj.update(dt)

    def draw(self):
        self.game.screen.blit(self.background, (0, 0))

        for obj in self.drawables:
            if getattr(obj, "draw", None):
                obj.draw(self.game.screen)

    def on_enter(self):
        screen_width, screen_height = self.game.screen.get_size()
        button_width, button_height = screen_width * 0.4, screen_height * 0.2
        
        title_font = pygame.font.SysFont(None, screen_width // 9)
        button_font = pygame.font.SysFont(None, screen_width // 12)

        self.background = load_scaled_image(
            "assets/MainMenu/bg.png",
            (screen_width, screen_height)
        )

        self.drawables.append(
            Text(
                SCREEN_TITLE,
                title_font,
                (screen_width // 2, screen_height // 4),
                YELLOW,
                center=True
            )
        )

        self.drawables.append(
            Button(
                rect=(
                    screen_width // 2,
                    screen_height // 2,
                    button_width,
                    button_height
                ),
                text="Play",
                font=button_font,
                on_click=lambda: self.game.screens_manager.set_screen("gamescreen"),
                image="assets/MainMenu/button.png",
                hover_darkened=50,
                text_color=WHITE,
                center=True
            )
        )

        self.drawables.append(
            Button(
                rect=(
                    screen_width // 2,
                    screen_height * 3 // 4,
                    button_width,
                    button_height
                ),
                text="Leave",
                font=button_font,
                on_click=self.game.close,
                bg=RED,
                hover_bg=DARK_RED,
                text_color=WHITE,
                center=True
            )
        )

    def on_exit(self):
        print("Exiting Main Menu Screen")
