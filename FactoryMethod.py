from Character import *
from StateFlyweight import *
from Tile import *
from FactoryMethod import *
from Maze import *
from Ball import *
import pygame
from pygame import *

class FactoryMethod:
    def makeCharacter(self, game):
        dic_images = {'stopped':pygame.image.load('images/vegeta/stopped.png'),
                           'left':pygame.image.load('images/vegeta/left.png'), 'right':pygame.image.load('images/vegeta/right.png'),
                           'up':pygame.image.load('images/vegeta/up.png'), 'down':pygame.image.load('images/vegeta/down.png'),
                           'a_right_1':pygame.image.load('images/vegeta/a_right_1.png'), 'a_left_1':pygame.image.load('images/vegeta/a_left_1.png'),
                           'a_right_2':pygame.image.load('images/vegeta/a_right_2.png'), 'a_left_2':pygame.image.load('images/vegeta/a_left_2.png'),
                           'a_right_3':pygame.image.load('images/vegeta/a_right_3.png'), 'a_left_3':pygame.image.load('images/vegeta/a_left_3.png')}
                           
        dic_images_ss = {'stopped':pygame.image.load('images/vegetaSS/stopped.gif'),
                           'left':pygame.image.load('images/vegetaSS/left.png'), 'right':pygame.image.load('images/vegetaSS/right.png'),
                           'up':pygame.image.load('images/vegetaSS/up.png'), 'down':pygame.image.load('images/vegetaSS/down.png'),
                           'a_right_1':pygame.image.load('images/vegetaSS/a_right_1.png'), 'a_left_1':pygame.image.load('images/vegetaSS/a_left_1.png'),
                           'a_right_2':pygame.image.load('images/vegetaSS/a_right_2.png'), 'a_left_2':pygame.image.load('images/vegetaSS/a_left_2.png'),
                           'a_right_3':pygame.image.load('images/vegetaSS/a_right_3.png'), 'a_left_3':pygame.image.load('images/vegetaSS/a_left_3.png')}

        return Character(game, dic_images, dic_images_ss, self)
        
    def makeStateFlyweight(self, guy):
        return StateFlyweight(guy, self)

    def makeSuperStateFlyweight(self, guy, dic):
        return SuperStateFlyweight(guy, dic, self)

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
    
    def makeAttackingRight(self, guy):
        return AttackingRight(guy)

    def makeAttackingLeft(self, guy):
        return AttackingLeft(guy)

    def makeSuperSaiyan(self, guy, dic):
        return SuperSaiyan(guy, dic, self)

    def makeNormal(self, guy, dic):
        return Normal(guy, dic, self)

    def makeMaze(self, game):
        return Maze(game, self)

    def makeGroundTile(self, x, y):
        return GroundTile(x, y)

    def makeObstacleTile(self, x, y):
        return ObstacleTile(x, y)

    def makeBall(self, game, direction, pos):
        dir_dic = {'right':(10,0), 'left':(-10,0)}
        dic = {'right':pygame.image.load('images/ball_right.png'), 'left':pygame.image.load('images/ball_left.png')}
        return Ball(game, dic, direction, dir_dic, pos)
    
