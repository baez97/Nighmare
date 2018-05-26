from Character import *
import sys, pygame
from pygame.locals import *
from Maze import *
from Tile import *


class Game:
    def __init__(self):
        self.maze = Maze(self)
        self.character = Character(self)
        self.display = pygame.display.set_mode((1000, 820))
        self.fpsClock = pygame.time.Clock()

    def run(self):
        pygame.init()
        while True:
            self.maze.paintAll()
            self.character.move()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                elif event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        self.character.changeDown()

            pygame.display.update()
            self.fpsClock.tick(30)

    def paint(self, image, position):
        self.display.blit(image, position)

    def canMoveUp(self, new_pos):
        return self.maze.canMoveUp(new_pos)

    def canMoveDown(self, new_pos):
        return self.maze.canMoveDown(new_pos)

    def canMoveRight(self, new_pos):
        return self.maze.canMoveRight(new_pos)

    def canMoveLeft(self, new_pos):
        return self.maze.canMoveLeft(new_pos)

    def paintCharacter(self):
        self.character.paint()


game = Game()
game.run()