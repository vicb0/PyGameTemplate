import os
import pygame

from consts import metadata
from managers.AudioManager import AudioManager
from managers.ScreensManager import ScreensManager
from managers.InputsManager import InputsManager
from managers.SettingsManager import SettingsManager
from utils.resourceUtils import resource_path


SCREEN_TITLE = getattr(metadata, "SCREEN_TITLE", "Pygame")
ASSETS_FOLDER = resource_path(getattr(metadata, "ASSETS_FOLDER", "assets"))
GAME_ICON_PATH = getattr(metadata, "GAME_ICON_PATH", f"{ASSETS_FOLDER}/icon.png")
DEFAULT_SCREEN = getattr(metadata, "DEFAULT_SCREEN", "mainmenu")


class Game:
    def __init__(self):
        self.dt = 0
        self.running = True
        self.clock = pygame.time.Clock()

        self.screen = None
        self.screens_manager = None
        self.inputs_manager = None
        self.settings_manager = None
        self.audio_manager = None

    def init(self):
        pygame.init()

        pygame.display.set_caption(SCREEN_TITLE)
        if os.path.exists(GAME_ICON_PATH):
            pygame.display.set_icon(pygame.image.load(GAME_ICON_PATH))

        self.audio_manager = AudioManager(self)
        self.inputs_manager = InputsManager(self)
        self.screens_manager = ScreensManager(self)
        self.settings_manager = SettingsManager(self)

        self.settings_manager.readIfExistsElseCreate()

        self.screen = pygame.display.set_mode(
            size=(
                self.settings_manager.getSetting("width"),
                self.settings_manager.getSetting("height")
            ),
            flags=pygame.FULLSCREEN if self.settings_manager.getSetting("fullscreen") else 0
        )

        self.screens_manager.set_screen(DEFAULT_SCREEN)

    def run(self):
        self.init()

        while self.running:
            self.dt = self.clock.tick(self.settings_manager.getSetting("max_fps")) / 1000

            self.inputs_manager.inputsListener()
            
            self.screens_manager.update(self.dt)
            self.screens_manager.redraw()

        pygame.quit()

    def close(self): 
        self.running = False
        self.screens_manager.close()
