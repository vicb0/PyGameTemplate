import pygame

from consts.colors import *
from core.ScreenInterface import ScreenInterface
from gameObjects.Character import Character


class SpriteScreen(ScreenInterface):
    def __init__(self, game):
        super().__init__(game)
        self.character = None
        self.drawables = []

        self.input_linker = {
            pygame.KEYDOWN: self.on_key_down
        }

    def event_handler(self, event):
        func = self.input_linker.get(event.type)
        if func:
            func(event)

    def on_key_down(self, event):
        if event.key == pygame.K_ESCAPE:
            self.game.screens_manager.set_screen("gamescreen")
        elif event.key == pygame.K_LEFT:
            self.character.change_direction(dir_x=-1, dir_y=0)
        elif event.key == pygame.K_RIGHT:
            self.character.change_direction(dir_x=1, dir_y=0)
        elif event.key == pygame.K_UP:
            self.character.change_direction(dir_x=0, dir_y=-1)
        elif event.key == pygame.K_DOWN:
            self.character.change_direction(dir_x=0, dir_y=1)

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
        self.character = Character(self.game.screen.get_width() // 2, self.game.screen.get_height() // 2)
        self.drawables.append(self.character)

    def on_exit(self):
        print("Exiting Test Screen")
