from Character import *
from StateFlyweight import *
from Tile import *
from FactoryMethod import *
from Maze import *
import pygame
from pygame import *

class FactoryMethod:
    def makeCharacter(self, game):
        dic_images = {'stopped':pygame.image.load('images/vegeta/stopped.png'),
                           'left':pygame.image.load('images/vegeta/left.png'), 'right':pygame.image.load('images/vegeta/right.png'),
                           'up':pygame.image.load('images/vegeta/up.png'), 'down':pygame.image.load('images/vegeta/down.png')}
        dic_images_ss = {'stopped':pygame.image.load('images/vegetaSS/stopped.gif'),
                           'left':pygame.image.load('images/vegetaSS/left.png'), 'right':pygame.image.load('images/vegetaSS/right.png'),
                           'up':pygame.image.load('images/vegetaSS/up.png'), 'down':pygame.image.load('images/vegetaSS/down.png')}

        return Character(game, dic_images, dic_images_ss, self)
        
    def makeStateFlyweight(self, guy):
        return StateFlyweight(guy, self)

    def makeMovingUp(self, guy):
        return MovingUp(guy)

    def makeMovingDown(self, guy):
        return MovingDown(guy)

    def makeMovingRight(self, guy):
        return MovingRight(guy)

    def makeMovingLeft(self, guy):
        return MovingLeft(guy)

    def makeStopped(self, guy):
        return Stopped(guy)

    def makeMaze(self, game):
        return Maze(game, self)

    def makeGroundTile(self, x, y):
        return GroundTile(x, y)

    def makeObstacleTile(self, x, y):
        return ObstacleTile(x, y)

    
