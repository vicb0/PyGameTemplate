import pkgutil
import importlib
import inspect

import pygame

from consts import metadata
from core.ScreenInterface import ScreenInterface


SCREENS_FOLDER = getattr(metadata, "SCREENS_FOLDER", "screens")


class ScreensManager:
    def __init__(self, game):
        self.game = game
        self.screens = self.load_screens()
        self.current_screen = None

    def set_screen(self, screen):
        new_screen = self.screens.get(screen.lower())
        if not new_screen:
            raise Exception(f"Screen {screen} not found")

        if self.current_screen:
            self.current_screen.on_exit()

        self.current_screen = new_screen(self.game)
        self.current_screen.on_enter()

    def load_screens(self):
        screens = {}

        package = importlib.import_module(SCREENS_FOLDER)

        for _, module_name, is_pkg in pkgutil.iter_modules(package.__path__):
            if is_pkg:
                continue

            module = importlib.import_module(
                f"{SCREENS_FOLDER}.{module_name}"
            )

            for name, obj in inspect.getmembers(module, inspect.isclass):
                if name != module_name:
                    continue

                if obj.__module__ != module.__name__:
                    continue

                if not issubclass(obj, ScreenInterface):
                    raise Exception(
                        f"{module_name} does not inherit from ScreenInterface"
                    )

                screens[module_name.lower()] = obj
                break
            else:
                raise Exception(
                    f"Could not locate valid class {module_name} "
                    f"in {module_name}.py"
                )

        return screens


    def screen_not_none(func):
        def wrapper(self, *args, **kwargs):
            if self.current_screen:
                func(self, *args, **kwargs)
        return wrapper

    @screen_not_none
    def event_handler(self, event):      
        self.current_screen.event_handler(event)

    @screen_not_none
    def update(self, dt):
        self.current_screen.update(dt)

    @screen_not_none
    def redraw(self):
        self.current_screen.draw()
        pygame.display.update()

    @screen_not_none
    def close(self):
        self.current_screen.on_exit()
