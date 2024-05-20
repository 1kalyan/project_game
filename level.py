import pygame
from enemy import Enemy
from item import Item
from obstacle import Obstacle
from platform_render import Platform
from player import Player


class Level:
    def __init__(self, number):
        self.number = number
        self.completed = False
        self.player = Player()
        self.platforms = [Platform(100, 500, 600, 20)]
        self.items = [Item(350, 450)]
        self.obstacles = [Obstacle(400, 300)]
        self.enemies = [Enemy(200, 400)]

    def play(self, screen, clock):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.completed = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                running = False
                self.completed = True

            screen.fill((0, 0, 0))  # Fill the screen with black
            self.player.update()
            self.player.draw(screen)
            for platform in self.platforms:
                platform.draw(screen)
            for item in self.items:
                item.draw(screen)
            for obstacle in self.obstacles:
                obstacle.draw(screen)
            for enemy in self.enemies:
                enemy.update()
                enemy.draw(screen)

            pygame.display.flip()
            clock.tick(60)