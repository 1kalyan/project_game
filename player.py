import pygame


class Player:
    def __init__(self):
        self.position = [100, 100]
        self.size = (50, 50)
        self.color = (0, 255, 0)
        self.velocity = [0, 0]

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.position[0] -= 5
        if keys[pygame.K_RIGHT]:
            self.position[0] += 5
        if keys[pygame.K_UP]:
            self.position[1] -= 5
        if keys[pygame.K_DOWN]:
            self.position[1] += 5

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (*self.position, *self.size))