import os
import json

from consts import default_settings


DEFAULT_SETTINGS = getattr(default_settings, "DEFAULT_SETTINGS", {
    "width": 800,
    "height": 600,
    "max_fps": 24,
    "fullscreen": False,
    "sfx_volume": 0.5,
    "music_volume": 0.5
})


class SettingsManager:
    def __init__(self, game):
        self.game = game
        self.settings = DEFAULT_SETTINGS

    def readSettingsFile(self, file_name="settings.json"):
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                self.settings |= json.load(f)
        except json.decoder.JSONDecodeError:
            pass

    def writeSettingsFile(self, file_name="settings.json"):
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(self.settings, f, indent=4)
    
    def readIfExistsElseCreate(self, file_name="settings.json"):
        if os.path.exists(file_name):
            self.readSettingsFile()
        else:
            self.writeSettingsFile()

    def setSetting(self, key, value):
        self.settings[key] = value
        self.writeSettingsFile()

    def getSetting(self, key):
        return self.settings.get(key, None)
