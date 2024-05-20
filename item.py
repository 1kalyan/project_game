import pygame


class Item:
    def __init__(self, x, y):
        self.position = (x, y)
        self.size = (20, 20)
        self.color = (255, 255, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (*self.position, *self.size))
        