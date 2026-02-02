import pygame


class ScreensManager:
    def __init__(self, game):
        self.game = game
        
        self.current_screen = None
        # Set the first screen here:
        # self.set_screen(screen object)

    def set_screen(self, screen):
        if self.current_screen:
            self.current_screen.on_exit()

        self.current_screen = screen(self.game)
        self.current_screen.on_enter()

    def screen_not_none(func):
        def wrapper(self, *args, **kwargs):
            if self.current_screen:
                func(self, *args, **kwargs)
        return wrapper

    @screen_not_none
    def event_handler(self, event):      
        self.current_screen.event_handler(event)

    @screen_not_none
    def redraw(self):
        self.current_screen.draw()
        pygame.display.update()
