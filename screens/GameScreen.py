import random

import pygame

from consts.colors import *
from components.Text import Text
from core.ScreenInterface import ScreenInterface


class GameScreen(ScreenInterface):
    def __init__(self, game):
        super().__init__(game)

        self.drawables = []
        self.input_linker = {
            pygame.KEYDOWN: self.on_key_down
        }

    def on_key_down(self, event):
        if event.key == pygame.K_ESCAPE:
            self.game.screens_manager.set_screen("mainmenu")
        elif event.key == pygame.K_SPACE:
            self.game.screens_manager.set_screen("spritescreen")

    def event_handler(self, event):
        func = self.input_linker.get(event.type)
        if func:
            func(event)

    def update(self, dt):
        for obj in self.drawables:
            if getattr(obj, "update", None):
                obj.update(dt)

    def draw(self):
        self.game.screen.fill(BLACK)

        for obj in self.drawables:
            if getattr(obj, "draw", None):
                obj.draw(self.game.screen)

    def on_enter(self):
        w, h = self.game.screen.get_size()
        font_size = min(w, h) // 9

        title_font = pygame.font.SysFont(None, font_size)

        text_object = Text(
            "Press ESC to go back\nto the main menu\nPress SPACE to go to\nthe sprite screen",
            title_font,
            (w // 2, h // 2),
            WHITE,
            center=True
        )

        class TextUpdate:
            def __init__(self):
                self.dx = 1
                self.dy = 1
                self.elapsed_time = 0
                self.interval = 1
    
            def update(self, dt):
                self.elapsed_time += dt

                if self.elapsed_time >= self.interval:
                    self.elapsed_time %= self.interval
                    idx = random.randint(0, len(text_object.text) - 1)
                    while not text_object.text[idx].isalpha():
                        idx = random.randint(0, len(text_object.text) - 1)

                    curr_ascii = ord(text_object.text[idx])

                    new_char = chr(curr_ascii + 32 * (1 if curr_ascii < 97 else -1))
                    new_text = text_object.text[:idx] + new_char + text_object.text[idx+1:]
                    text_object.set_text(new_text)
                
                if text_object.rect.topleft[0] < 0:
                    self.dx = 1
                elif text_object.rect.topright[0] >= w:
                    self.dx = -1
                if text_object.rect.topleft[1] < 0:
                    self.dy = 1
                elif text_object.rect.bottomleft[1] >= h:
                    self.dy = -1

                text_object.set_position(
                    (
                        text_object.pos[0] + self.dx,
                        text_object.pos[1] + self.dy
                    )
                )
                

        text_object.update = TextUpdate().update
        self.drawables.append(text_object)

    def on_exit(self):
        print("Exiting Game Screen")
