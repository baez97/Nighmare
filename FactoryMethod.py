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
                              'heart_unobtained': pygame.image.load('images/heart/h_1.png'),
                              'medal_obtained': pygame.image.load('images/null.png'),
                              'red_unobtained': pygame.image.load('images/items/RedMedal.png'),
                              'blue_unobtained': pygame.image.load('images/items/BlueMedal.png'),
                              'gold_unobtained': pygame.image.load('images/items/GoldMedal.png')}

        self.dic_medals_img = {'red': {'obtained': self.dic_tiles_img['red_unobtained'],  'empty': self.dic_tiles_img['medal_obtained']},
                               'blue':{'obtained': self.dic_tiles_img['blue_unobtained'], 'empty': self.dic_tiles_img['medal_obtained']},
                               'gold':{'obtained': self.dic_tiles_img['gold_unobtained'], 'empty': self.dic_tiles_img['medal_obtained']}}

        self.dic_tiles_status = {'closed': self.makeHoleClosed(),
                                 'opened': self.makeHoleOpened(),
                                 'key_obtained': self.makeKeyObtained(),
                                 'key_unobtained': self.makeKeyUnobtained(),
                                 'heart_obtained': self.makeHeartObtained(),
                                 'heart_unobtained': self.makeHeartUnobtained(),
                                 'red_unobtained': self.makeRedMedalUnobtained(),
                                 'blue_unobtained': self.makeBlueMedalUnobtained(),
                                 'gold_unobtained': self.makeGoldMedalUnobtained(),
                                 'obtained': self.makeMedalObtained()}

        self.dic_images_key = {'empty': pygame.image.load('images/items/key.png'),
                               'obtained': pygame.image.load('images/items/key.png')}

        self.dead_image = pygame.image.load('images/Dead.png')
        self.win_image = pygame.image.load('images/Win.png')

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

    def makeTopMaze(self, game):
        return TopMaze(game, self)

    def makeUndergroundMaze(self, game):
        return UndergroundMaze(game, self)

    def makeGroundTile(self, x, y):
        return GroundTile(x, y)

    def makeObstacleTile(self, x, y):
        return ObstacleTile(x, y)

    def makeWallTile(self, x, y):
        return WallTile(x, y)

    def makeClosedHoleTile(self, x, y, maze_1, maze_2):
        component = self.makeGroundTile(x, y)
        return HoleDecorator(x, y, component, 'closed', self.dic_tiles_status, maze_1, maze_2)

    def makeOpenedHoleTile(self, x, y, maze_1, maze_2):
        component = self.makeGroundTile(x, y)
        return HoleDecorator(x, y, component, 'opened', self.dic_tiles_status, maze_1, maze_2)

    def makeKeyTile(self, x, y):
        component = self.makeGroundTile(x, y)
        return KeyDecorator(x, y, component, 'key_unobtained', self.dic_tiles_status)

    def makeHeartTile(self, x, y):
        component = self.makeGroundTile(x, y)
        return HeartDecorator(x, y, component, 'heart_unobtained', self.dic_tiles_status)

    def makeRedMedalTile(self, x, y):
        component = self.makeGroundTile(x, y)
        return RedMedalDecorator(x, y, component, 'red_unobtained', self.dic_tiles_status)

    def makeBlueMedalTile(self, x, y):
        component = self.makeGroundTile(x, y)
        return BlueMedalDecorator(x, y, component, 'blue_unobtained', self.dic_tiles_status)

    def makeGoldMedalTile(self, x, y):
        component = self.makeGroundTile(x, y)
        return GoldMedalDecorator(x, y, component, 'gold_unobtained', self.dic_tiles_status)

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
        return RedMedal((200,200), self.dic_medals_img['red'])

    def makeBlueMedal(self):
        return BlueMedal((300, 300), self.dic_medals_img['blue'])

    def makeGoldMedal(self):
        return GoldMedal((400, 400), self.dic_medals_img['gold'])

    def makeKeyObtained(self):
        return KeyObtained(self.dic_tiles_img['key_obtained'])
    
    def makeKeyUnobtained(self):
        return KeyUnobtained(self.dic_tiles_img['key_unobtained'])

    def makeHeartObtained(self):
        return HeartObtained(self.dic_tiles_img['heart_obtained'])

    def makeHeartUnobtained(self):
        return HeartUnobtained(self.dic_tiles_img['heart_unobtained'])

    def makeMedalObtained(self):
        return MedalObtained(self.dic_tiles_img['medal_obtained'])
    
    def makeRedMedalUnobtained(self):
        return RedMedalUnobtained(self.dic_tiles_img['red_unobtained'])

    def makeBlueMedalUnobtained(self):
        return BlueMedalUnobtained(self.dic_tiles_img['blue_unobtained'])

    def makeGoldMedalUnobtained(self):
        return GoldMedalUnobtained(self.dic_tiles_img['gold_unobtained'])
    
    def makeBag(self, character):
        return Bag((50,50), self, character, self.dic_tiles_img['key_unobtained'])
    
    def makeMedalBox(self, bag):
        return MedalBox((100,100), self, bag, self.dic_tiles_img['key_unobtained'])

    def makeHeartImage(self):
        return self.dic_tiles_img['heart_unobtained']

    def makeRedMedalImage(self):
        return self.dic_images_red_medal

    def makeKeyImage(self):
        return self.dic_tiles_img['key_unobtained']

    def makeRedImage(self):
        return self.dic_tiles_img['red_unobtained']

    def makeBlueImage(self):
        return self.dic_tiles_img['blue_unobtained']

    def makeGoldImage(self):
        return self.dic_tiles_img['gold_unobtained']

    def getDeadImage(self):
        return self.dead_image

    def getWinImage(self):
        return self.win_image
    

    
        