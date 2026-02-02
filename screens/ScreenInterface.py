from abc import ABC, abstractmethod


class ScreenInterface(ABC):
    def __init__(self, game):
        self.game = game
        self.drawables = []

    @abstractmethod
    def event_handler(self, event):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def on_enter(self):
        pass

    @abstractmethod
    def on_exit(self):
        pass

