from Maze import *

class Tile:
    def __init__(self, x, y):
        self.cel_x = x
        self.cel_y = y

    def isObstacle(self):
        return False

class GroundTile(Tile):
    def paint(self, maze):
        maze.paintGroundTile(self.cel_x, self.cel_y)

class ObstacleTile(Tile):
    def paint(self, maze):
        maze.paintObstacleTile(self.cel_x, self.cel_y)
    
    def isObstacle(self):
        return True