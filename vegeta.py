import sys, pygame
from pygame.locals import *

class Maze:
    def __init__(self):
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
        DISPLAYSURF.blit(self.ground_img, real_pos)
    
    def paintObstacleTile(self, x, y):
        real_pos = self.getRealObstacle(x, y)
        DISPLAYSURF.blit(self.obstacle_img, real_pos)
    
    def getRealGround(self, x, y):
        real_x = x*50
        real_y = y*40 + 20
        return (real_x, real_y)

    def getRealObstacle(self, x, y):
        real_x = x*50
        real_y = y*40
        return (real_x, real_y)

class Tile:
    def __init__(self, x, y):
        self.cel_x = x
        self.cel_y = y

    def occuped(self):
        return False

class GroundTile(Tile):
    def paint(self, maze):
        maze.paintGroundTile(self.cel_x, self.cel_y)

class ObstacleTile(Tile):
    def paint(self, maze):
        maze.paintObstacleTile(self.cel_x, self.cel_y)
    
    def occuped(self):
        return True


pygame.init()
DISPLAYSURF = pygame.display.set_mode((1000, 820))
maze = Maze()
WHITE = (255, 255, 255)

while True:
    maze.paint()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()