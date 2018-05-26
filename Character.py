import pygame
from pygame.locals import *
from State import *

class Character:
    def __init__(self, game):
        self.game = game
        self.pos = (500, 500)
        self.state = Stopped(self)
        self.dic_images = {'stopped':pygame.image.load('images/vegeta/stopped.png'),
                           'left':pygame.image.load('images/vegeta/left.png'), 'right':pygame.image.load('images/vegeta/right.png'),
                           'up':pygame.image.load('images/vegeta/up.png'), 'down':pygame.image.load('images/vegeta/down.png')}
        self.dic_images_ss = {'stopped':pygame.image.load('images/vegetaSS/stopped.gif'),
                           'left':pygame.image.load('images/vegetaSS/left.png'), 'right':pygame.image.load('images/vegetaSS/right.png'),
                           'up':pygame.image.load('images/vegetaSS/up.png'), 'down':pygame.image.load('images/vegetaSS/down.png')}

        self.currentImage = self.dic_images['stopped']
        self.rect = self.currentImage.get_rect()

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
            self.rect.right = right_limit - 24
            self.pos = (self.rect.right, self.pos[1])
            
        
    def changeDown(self):
        self.state = MovingDown(self)
        self.currentImage = self.dic_images['down']
        self.rect = self.currentImage.get_rect()
        self.rect.move(self.pos)

    def changeUp(self):
        self.state = MovingUp(self)
        self.currentImage = self.dic_images['up']
        self.rect = self.currentImage.get_rect()
        self.rect.move(self.pos)

    def changeRight(self):
        self.state = MovingRight(self)
        self.currentImage = self.dic_images['right']
        self.rect = self.currentImage.get_rect()
        self.rect.move(self.pos)

    def changeLeft(self):
        self.state = MovingLeft(self)
        self.currentImage = self.dic_images['left']
        self.rect = self.currentImage.get_rect()
        self.rect.move(self.pos)

    def changeStopped(self):
        self.state = Stopped(self)
        self.currentImage = self.dic_images['stopped']
        self.rect = self.currentImage.get_rect()
        self.rect.move(self.pos)

    def getPos(self):
        return self.pos

        
