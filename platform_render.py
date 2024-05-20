import pygame


class Platform:
    def __init__(self, x, y, width, height):
        self.position = (x, y)
        self.size = (width, height)
        self.color = (255, 255, 255)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (*self.position, *self.size))