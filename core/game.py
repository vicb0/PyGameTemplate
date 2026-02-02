import os
import pygame

from consts import GAME_ICON
from consts import SCREEN_TITLE
from managers.ScreensManager import ScreensManager
from managers.InputsManager import InputsManager
from managers.SettingsManager import SettingsManager


class Game:
    def __init__(self):
        pygame.display.set_caption(SCREEN_TITLE)
        if os.path.exists(GAME_ICON):
            pygame.display.set_icon(pygame.image.load(GAME_ICON))
        
        self.settings_manager = SettingsManager()
        self.screens_manager = ScreensManager(self)
        self.inputs_manager = InputsManager(self)

        self.screen = pygame.display.set_mode(
            size=(
                self.settings_manager.getSetting("width"),
                self.settings_manager.getSetting("height")
            ),
            flags=pygame.FULLSCREEN if self.settings_manager.getSetting("fullscreen") else 0
        )

        self.dt = 0
        self.running = True
        self.clock = pygame.time.Clock()

    def init(self):
        pygame.init()
        self.settings_manager.readIfExistsElseCreate()

    def run(self):
        self.init()

        while self.running:
            self.dt = self.clock.tick(self.settings_manager.getSetting("max_fps")) / 1000
        
            self.inputs_manager.inputsListener()
            
            self.screens_manager.redraw()

        pygame.quit()
