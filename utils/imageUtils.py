import pygame

from utils.resourceUtils import resource_path


def load_scaled_image(path, size=None):
    image = pygame.image.load(resource_path(path)).convert_alpha()
    if size is None:
        return image
    return pygame.transform.smoothscale(image, size)
