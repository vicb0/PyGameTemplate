import os
import json


class SettingsManager:
    def __init__(self):
        self.settings = {
            "width": 800,
            "height": 600,
            "max_fps": 60,
            "fullscreen": False
        }

    def readSettingsFile(self, file_name="settings.json"):
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                self.settings |= json.load(f)
        except json.decoder.JSONDecodeError:
            pass

    def writeSettingsFile(self, file_name="settings.json"):
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(self.settings, f, indent=4)
    
    def readIfExistsElseCreate(self):
        if os.path.exists("settings.json"):
            self.readSettingsFile()
        else:
            self.writeSettingsFile()

    def setSetting(self, key, value):
        self.settings[key] = value
        self.writeSettingsFile()

    def getSetting(self, key):
        return self.settings.get(key, None)
