from Maze import *

class Tile(object):
    def __init__(self, x, y):
        self.cel_x = x
        self.cel_y = y

    def isObstacle(self):
        return (-1, -1)

    def interact(self, character):
        print "Hi! I am the cell", (self.cel_x, self.cel_y), ', may I help you in something?'

    def isGroundTile(self):
        return False
    def isObstacleTile(self):
        return False
    def isWallTile(self):
        return False
    def isHeartTile(self):
        return False
    def isKeyTile(self):
        return False
    def isHoleTile(self):
        return False
    def isRedMedalTile(self):
        return False
    def isBlueMedalTile(self):
        return False
    def isGoldMedalTile(self):
        return False

class GroundTile(Tile):
    def paint(self, maze):
        maze.paintGroundTile(self.cel_x, self.cel_y)

    def isGroundTile(self):
        return True

class ObstacleTile(Tile):
    def paint(self, maze):
        maze.paintObstacleTile(self.cel_x, self.cel_y)
    
    def isObstacle(self):
        return ((self.cel_x, self.cel_y))

    def isObstacleTile(self):
        return True

class WallTile(Tile):
    def paint(self, maze):
        maze.paintWallTile(self.cel_x, self.cel_y)

    def isObstacle(self):
        return ((self.cel_x, self.cel_y))

    def isWallTile(self):
        return True



    