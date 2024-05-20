import pygame
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Platformer Game")
        self.clock = pygame.time.Clock()
        self.levels = [Level(1), Level(2), Level(3)]
        self.current_level_index = 0
        self.running = True

    def run(self):
        while self.running:
            self.levels[self.current_level_index].play(self.screen, self.clock)
            if self.levels[self.current_level_index].completed:
                self.current_level_index += 1
                if self.current_level_index >= len(self.levels):
                    self.running = False
        print("Game Over!")
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()