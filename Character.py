import pygame
from pygame.locals import *
from State import *
from StateFlyweight import *

class Character:
    def __init__(self, game, dic, dic_images_ss, factory):
        self.game = game
        self.stateFly = factory.makeStateFlyweight(self)
        self.pos = (500, 500)
        self.state = self.stateFly.getStopped()
        self.dic_images = dic
        self.dic_images_ss = dic_images_ss
        self.currentImage  = self.dic_images['stopped']
        self.rect = self.currentImage.get_rect()
        self.right_images = (self.dic_images['a_right_1'], self.dic_images['a_right_2'], self.dic_images['a_right_3'])
        self.left_images  = (self.dic_images['a_left_1'],  self.dic_images['a_left_2'],  self.dic_images['a_left_3'] )

    def move(self):
        self.state.move()

    def paint(self):
        self.game.paint(self.currentImage, self.pos)

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
            
    def attackRight(self):
        if self.counter < 3:
            self.currentImage = self.right_images[self.counter]
            self.counter+=1
        elif self.counter < 7:
            self.currentImage = self.right_images[2]
            self.counter+=1
        else:
            self.changeStopped()
        
    def attackLeft(self):
        if self.counter == 0:
            self.pos = (self.pos[0] - 15, self.pos[1])
        if self.counter < 3:
            self.currentImage = self.left_images[self.counter]
            self.counter+=1
        elif self.counter < 7:
            self.currentImage = self.left_images[2]
            self.counter +=1
        else:
            self.pos = (self.pos[0] + 15, self.pos[1])
            self.original_pos = self.pos
            self.changeStopped()

    def changeDown(self):
        self.state = self.stateFly.getMovingDown()
        self.currentImage = self.dic_images['down']
        self.rect = self.currentImage.get_rect()
        self.rect.move(self.pos)

    def changeUp(self):
        self.state = self.stateFly.getMovingUp()
        self.currentImage = self.dic_images['up']
        self.rect = self.currentImage.get_rect()
        self.rect.move(self.pos)

    def changeRight(self):
        self.state = self.stateFly.getMovingRight()
        self.currentImage = self.dic_images['right']
        self.rect = self.currentImage.get_rect()
        self.rect.move(self.pos)

    def changeLeft(self):
        self.state = self.stateFly.getMovingLeft()
        self.currentImage = self.dic_images['left']
        self.rect = self.currentImage.get_rect()
        self.rect.move(self.pos)

    def changeStopped(self):
        self.state = self.stateFly.getStopped()
        self.currentImage = self.dic_images['stopped']
        self.rect = self.currentImage.get_rect()
        self.rect.move(self.pos)

    def changeAttackRight(self):
        if(self.state.isAttackingLeft()):
            self.pos = (self.pos[0] + 15, self.pos[1])
        self.counter = 0
        self.state = self.stateFly.getAttackingRight()
        self.currentImage = self.dic_images['a_right_1']
        self.rect = self.currentImage.get_rect()
        self.rect.move(self.pos)

    def changeAttackLeft(self):
        if(self.state.isAttackingLeft()):
            self.pos = (self.pos[0] + 15, self.pos[1])

        self.counter = 0
        self.state = self.stateFly.getAttackingLeft()
        self.rect = self.currentImage.get_rect()
        self.rect.move(self.pos)

    def getPos(self):
        return self.pos

        
