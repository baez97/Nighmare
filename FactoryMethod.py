from Character import *
from StateFlyweight import *
from Tile import *
from FactoryMethod import *
from Maze import *
from Ball import *
import pygame
from pygame import *

class FactoryMethod:
    def __init__(self):
        self.ballStateFlyweight = BallStateFlyweight(self)

        self.state_dic = {'right': self.ballStateFlyweight.getMovingRight(),
                        'left' : self.ballStateFlyweight.getMovingLeft(),
                        'fading': self.ballStateFlyweight.getFading()}

        self.ball_dic = {'right':pygame.image.load('images/ball/ball_right.png'), 
               'left' :pygame.image.load('images/ball/ball_left.png'),
               'f_1'  :pygame.image.load('images/ball/f_1.png'),
               'f_2'  :pygame.image.load('images/ball/f_2.png'),
               'f_3'  :pygame.image.load('images/ball/f_3.png')}

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

        dic_images_powerup = (pygame.image.load('images/vegetaPU/n_1.png' ), pygame.image.load('images/vegetaPU/n_2.png' ),
                              pygame.image.load('images/vegetaPU/n_3.png' ), pygame.image.load('images/vegetaPU/n_4.png' ),
                              pygame.image.load('images/vegetaPU/n_5.png' ), pygame.image.load('images/vegetaPU/n_6.png' ),
                              pygame.image.load('images/vegetaPU/n_7.png' ), pygame.image.load('images/vegetaPU/n_8.png' ),
                              pygame.image.load('images/vegetaPU/n_9.png' ), pygame.image.load('images/vegetaPU/n_10.png'),
                              pygame.image.load('images/vegetaPU/s_1.png' ), pygame.image.load('images/vegetaPU/s_2.png' ), 
                              pygame.image.load('images/vegetaPU/s_3.png' ), pygame.image.load('images/vegetaPU/s_4.png' ), 
                              pygame.image.load('images/vegetaPU/s_5.png' ), pygame.image.load('images/vegetaPU/s_6.png' ), 
                              pygame.image.load('images/vegetaPU/s_7.png' ), pygame.image.load('images/vegetaPU/s_8.png' ), 
                              pygame.image.load('images/vegetaPU/s_9.png' ), pygame.image.load('images/vegetaPU/s_10.png'), 
                              pygame.image.load('images/vegetaPU/s_11.png'), pygame.image.load('images/vegetaPU/s_12.png'), 
                              pygame.image.load('images/vegetaPU/s_13.png'), pygame.image.load('images/vegetaPU/s_14.png'))
        
        


        return Character(game, dic_images, dic_images_ss, dic_images_powerup, self)
        
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

    def makePoweringUp(self, guy, dic):
        return PoweringUp(guy, dic, self)

    def makeMaze(self, game):
        return Maze(game, self)

    def makeGroundTile(self, x, y):
        return GroundTile(x, y)

    def makeObstacleTile(self, x, y):
        return ObstacleTile(x, y)

    def makeWallTile(self, x, y):
        return WallTile(x, y)

    def makeBall(self, game, direction, pos):
        return Ball(game, self.ball_dic, self.state_dic, direction, pos)

    def makeBallMovingRight(self):
        return BallMovingRight()

    def makeBallMovingLeft(self):
        return BallMovingLeft()

    def makeBallFading(self):
        return BallFading()
    

        