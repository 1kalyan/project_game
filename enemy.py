import pygame


class Enemy:
    def __init__(self, x, y):
        self.position = [x, y]
        self.size = (50, 50)
        self.color = (0, 0, 255)
        self.velocity = [-2, 0]

    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        if self.position[0] < 0 or self.position[0] > 750:
            self.velocity[0] = -self.velocity[0]

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (*self.position, *self.size))