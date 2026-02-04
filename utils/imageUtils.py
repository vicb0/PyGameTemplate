import pygame


def load_scaled_image(path, size=None):
    image = pygame.image.load(path).convert_alpha()
    if size is None:
        return image
    return pygame.transform.smoothscale(image, size)
