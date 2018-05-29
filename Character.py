import pygame
from pygame.locals import *
from State import *
from StateFlyweight import *

class MovableObject(object):
    def __init__(self, game, dic, pos):
        self.game = game
        self.pos = pos
        self.dic_images = dic
        self.counter = 0

    def move(self):
        self.state.move()

    def paint(self):
        self.game.paint(self.state.getImg(), self.pos)
        
class Character(MovableObject):
    def __init__(self, game, dic, dic_images_ss, dic_powerUp, factory):
        super(Character, self).__init__(game, dic, (500,500))
        self.dics = {'normal':dic, 'supersaiyan':dic_images_ss, 'powerup': dic_powerUp}
        self.superStateFly = factory.makeSuperStateFlyweight(self, self.dics)
        self.state = self.superStateFly.getNormal()
        self.rect = self.state.getImg().get_rect()
        self.factory = factory

    def moveUp(self):
        new_pos = self.state.getNextPos()
        new_limit = self.state.getNextLimit()
        top_limit = self.game.canMoveUp(new_limit)

        if top_limit < 0:
            self.rect.move((0, new_pos[1] - self.pos[1]))
            self.pos = new_pos
        
        else:
            self.changeStopped()
            self.rect.top = top_limit
            self.pos = (self.pos[0], self.rect.top)

    def moveDown(self):
        new_pos = self.state.getNextPos()
        new_limit = self.state.getNextLimit()
        bottom_limit = self.game.canMoveDown(new_limit)

        if bottom_limit < 0:
            self.rect.move((0, new_pos[1] - self.pos[1]))
            self.pos = new_pos
        
        else:
            self.changeStopped()
            self.rect.bottom = bottom_limit
            self.pos = (self.pos[0], self.rect.top)

    def moveLeft(self):
        new_pos = self.state.getNextPos()
        new_limit = self.state.getNextLimit()
        left_limit = self.game.canMoveLeft((new_limit[0], new_limit[1]))

        if left_limit < 0:
            self.rect.move((new_pos[0] - self.pos[0], 0))
            self.pos = new_pos
        
        else:
            self.changeStopped()
            self.rect.left = left_limit + 50
            self.pos = (self.rect.left, self.pos[1])

    def moveRight(self):
        new_pos = self.state.getNextPos()
        new_limit = self.state.getNextLimit()
        right_limit = self.game.canMoveRight((new_limit[0], new_limit[1]))

        if right_limit < 0:
            self.rect.move((self.pos[0] - new_pos[0], 0))
            self.pos = new_pos
        
        else:
            self.changeStopped()
            self.rect.right = right_limit - 26
            self.pos = (self.rect.right, self.pos[1])

    def attack(self):
        self.state.attack(self.counter)
        self.counter += 1

    def powerUp(self):
        self.state.powerUp(self.counter)
        self.counter += 1

    def changeDown(self):
        self.state.changeDown()
        self.rect = self.state.getImg().get_rect()
        self.rect.move(self.pos)

    def changeUp(self):
        self.state.changeUp()
        self.rect = self.state.getImg().get_rect()
        self.rect.move(self.pos)

    def changeRight(self):
        self.state.changeRight()
        self.rect = self.state.getImg().get_rect()
        self.rect.move(self.pos)

    def changeLeft(self):
        self.state.changeLeft()
        self.rect = self.state.getImg().get_rect()
        self.rect.move(self.pos)

    def changeStopped(self):
        self.state.changeStopped()
        self.rect = self.state.getImg().get_rect()
        self.rect.move(self.pos)

    def changePoweringUp(self):
        if(self.state.isAttackingLeft()):
            self.pos = (self.pos[0] + 15, self.pos[1])
        self.pos = (self.pos[0] - 40, self.pos[1] - 40)
        self.counter = 0
        self.lock()
        #self.state.changeStopped()
        self.state = self.superStateFly.getPoweringUp()
        

    def changeSuperSaiyan(self):
        self.state = self.superStateFly.getSuperSaiyan()
        self.state.changeStopped()
    
    def changeNormal(self):
        self.state = self.superStateFly.getNormal()
        self.unlock()
        self.state.changeStopped()

    def changeAttackRight(self):
        if(self.state.isAttackingLeft()):
            self.pos = (self.pos[0] + 15, self.pos[1])
        self.counter = 0
        self.state.changeAttackingRight()
        self.rect = self.state.getImg().get_rect()
        self.rect.move(self.pos)

    def changeAttackLeft(self):
        if(self.state.isAttackingLeft()):
            self.pos = (self.pos[0] + 15, self.pos[1])

        self.counter = 0
        self.state.changeAttackingLeft()
        self.rect = self.state.getImg().get_rect()
        self.rect.move(self.pos)

    def isAttackingLeft(self):
        return self.state.isAttackingLeft()

    def isPoweringUp(self):
        return self.state.isPoweringUp()

    def getPos(self):
        return self.pos

    def addBall(self, direction, displacement):
        ball_pos = (self.pos[0] + displacement[0], self.pos[1] + displacement[1])
        ball = self.factory.makeBall(self.game, direction, ball_pos)
        self.game.addBall(ball)

    def lock(self):
        self.game.lock()
    
    def unlock(self):
        self.game.unlock()
