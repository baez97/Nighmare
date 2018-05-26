import sys, pygame
from pygame.locals import *
from Maze import *
from Tile import *

class Game:
    def __init__(self):
        self.maze = Maze(self)
        self.display = pygame.display.set_mode((1000, 820))

    def run(self):
        pygame.init()
        while True:
            self.maze.paint()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

    def paint(self, image, position):
        self.display.blit(image, position)

    def canMove(self, new_pos):
        return self.maze.canMove(new_pos)


game = Game()
game.run()