from Character import *
from StateFlyweight import *
from Tile import *
from FactoryMethod import *
from Maze import *
from Ball import *
from Enemy import *
from ColissionManager import *
from TileDecorator import *
from TileState import *
from Composite import *
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

        self.dic_right_enemy = (pygame.image.load('images/cell/r_1.png'),
                                pygame.image.load('images/cell/r_2.png'),
                                pygame.image.load('images/cell/r_3.png'))

        self.dic_left_enemy =  (pygame.image.load('images/cell/l_1.png'),
                                pygame.image.load('images/cell/l_2.png'),
                                pygame.image.load('images/cell/l_3.png'))

        self.dic_tiles_img = {'closed': pygame.image.load('images/HoleTile_locked.png'),
                              'opened': pygame.image.load('images/HoleTile.png'),
                              'key_obtained': pygame.image.load('images/null.png'),
                              'key_unobtained': pygame.image.load('images/items/key.png'),
                              'heart_obtained': pygame.image.load('images/null.png'),
                              'heart_unobtained': pygame.image.load('images/heart/h_1.png')}

        self.dic_tiles_status = {'closed': self.makeHoleClosed(),
                                 'opened': self.makeHoleOpened(),
                                 'key_obtained': self.makeKeyObtained(),
                                 'key_unobtained': self.makeKeyUnobtained(),
                                 'heart_obtained': self.makeHeartObtained(),
                                 'heart_unobtained': self.makeHeartUnobtained()}

        self.dic_images_key = {'empty': pygame.image.load('images/items/key.png'),
                               'obtained': pygame.image.load('images/items/key.png')}

        self.dic_images_red_medal = {'empty': pygame.image.load('images/items/RedMedal_empty.png'),
                                     'obtained': pygame.image.load('images/items/RedMedal.png')}

        self.dic_images_blue_medal = {'empty': pygame.image.load('images/items/BlueMedal_empty.png'),
                                     'obtained': pygame.image.load('images/items/BlueMedal.png')}

        self.dic_images_gold_medal = {'empty': pygame.image.load('images/items/GoldMedal_empty.png'),
                                     'obtained': pygame.image.load('images/items/GoldMedal.png')}

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

    def makeClosedHoleTile(self, x, y):
        component = self.makeGroundTile(x, y)
        return HoleDecorator(x, y, component, 'closed', self.dic_tiles_status)

    def makeOpenedHoleTile(self, x, y):
        component = self.makeGroundTile(x, y)
        return HoleDecorator(x, y, component, 'closed', self.dic_tiles_status)

    def makeKeyTile(self, x, y):
        component = self.makeGroundTile(x, y)
        return KeyDecorator(x, y, component, 'key_unobtained', self.dic_tiles_status)

    def makeHeartTile(self, x, y):
        component = self.makeGroundTile(x, y)
        return HeartDecorator(x, y, component, 'heart_unobtained', self.dic_tiles_status)

    def makeBall(self, game, direction, pos):
        return Ball(game, self.ball_dic, self.state_dic, direction, pos, game.getColissionManager())

    def makeBallMovingRight(self):
        return BallMovingRight()

    def makeBallMovingLeft(self):
        return BallMovingLeft()

    def makeBallFading(self):
        return BallFading()
    
    def makeRightEnemy(self, game, pos, counter):
        return RightEnemy(game, self.dic_right_enemy, pos, counter, self)

    def makeLeftEnemy(self, game, pos, counter):
        return LeftEnemy(game, self.dic_left_enemy, pos, counter, self)

    def makeColissionManager(self, game):
        return ColissionManager(game)

    def makeHoleClosed(self):
        return HoleClosed(self.dic_tiles_img['closed'])

    def makeHoleOpened(self):
        return HoleOpened(self.dic_tiles_img['opened'])

    def makeKey(self):
        return Key((100,100), self.dic_images_key)

    def makeRedMedal(self):
        return RedMedal((200,200), self.dic_images_red_medal)

    def makeBlueMedal(self):
        return BlueMedal((300, 300), self.dic_images_blue_medal)

    def makeGoldMedal(self):
        return GoldMedal((400, 400), self.dic_images_gold_medal)

    def makeKeyObtained(self):
        return KeyObtained(self.dic_tiles_img['key_obtained'])
    
    def makeKeyUnobtained(self):
        return KeyUnobtained(self.dic_tiles_img['key_unobtained'])

    def makeHeartObtained(self):
        return HeartObtained(self.dic_tiles_img['heart_obtained'])

    def makeHeartUnobtained(self):
        return HeartUnobtained(self.dic_tiles_img['heart_unobtained'])
    
    def makeBag(self, character):
        return Bag((50,50), self, character, self.dic_tiles_img['key_unobtained'])
    
    def makeMedalBox(self, bag):
        return MedalBox((100,100), self, bag, self.dic_tiles_img['key_unobtained'])

    
        