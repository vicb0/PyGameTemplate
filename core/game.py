import os
import pygame

from consts import GAME_ICON
from consts import SCREEN_TITLE
from managers.ScreensManager import ScreensManager
from managers.InputsManager import InputsManager
from managers.SettingsManager import SettingsManager


class Game:
    def __init__(self):
        self.dt = 0
        self.running = True
        self.clock = pygame.time.Clock()

        self.screen = None
        self.screens_manager = None
        self.inputs_manager = None
        self.settings_manager = None

    def init(self):
        pygame.init()

        pygame.display.set_caption(SCREEN_TITLE)
        if os.path.exists(GAME_ICON):
            pygame.display.set_icon(pygame.image.load(GAME_ICON))

        self.settings_manager = SettingsManager()
        self.settings_manager.readIfExistsElseCreate()

        self.screen = pygame.display.set_mode(
            size=(
                self.settings_manager.getSetting("width"),
                self.settings_manager.getSetting("height")
            ),
            flags=pygame.FULLSCREEN if self.settings_manager.getSetting("fullscreen") else 0
        )

        self.screens_manager = ScreensManager(self)
        self.inputs_manager = InputsManager(self)
        # Set the first screen here:
        # self.screens_manager.set_screen(MainMenu)

    def run(self):
        self.init()

        while self.running:
            self.dt = self.clock.tick(self.settings_manager.getSetting("max_fps")) / 1000
        
            self.inputs_manager.inputsListener()
            
            self.screens_manager.redraw()

        pygame.quit()
