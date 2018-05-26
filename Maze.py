import sys, pygame
from pygame.locals import *
from Tile import *

class Maze:
    def __init__(self, game):
        self.game = game
        line = []
        self.objects = []
        for i in range(0,20):
            for j in range(0,20):
                if j in (0, 19) or i in (0,19):
                    line.append(ObstacleTile(i,j))
                else:
                    line.append(GroundTile(i,j))
            self.objects.append(line)
            line = []

        

        self.ground_img   = pygame.image.load('images/GroundTile.png')
        self.obstacle_img = pygame.image.load('images/GrassTile.png')

    def paint(self):
        for line in self.objects:
            for object in line:
                object.paint(self)
    
    def paintGroundTile(self, x, y):
        real_pos = self.getRealGround(x,y)
        self.game.paint(self.ground_img, real_pos)
    
    def paintObstacleTile(self, x, y):
        real_pos = self.getRealObstacle(x, y)
        self.game.paint(self.obstacle_img, real_pos)
    
    def getRealGround(self, x, y):
        real_x = x*50
        real_y = y*40 + 20
        return (real_x, real_y)

    def getRealObstacle(self, x, y):
        real_x = x*50
        real_y = y*40
        return (real_x, real_y)

    def canMove(self, new_pos):
        x, y = new_pos
        return objects[x][y].isObstacle()




