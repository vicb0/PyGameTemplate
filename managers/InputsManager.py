import pygame


class InputsManager:
    def __init__(self, game):
        self.game = game

    def inputsListener(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.close()
            
            self.game.screens_manager.event_handler(event)
