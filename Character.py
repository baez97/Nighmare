import pygame
from pygame.locals import *
from State import *

class Character:
    def __init__(self, game):
        self.game = game
        self.pos = (30, 30)
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
        up_limit = self.game.canMoveUp(new_pos)
        if up_limit < 0:
            self.pos = new_pos
        
        else:
            self.rect.up = up_limit

    def moveDown(self):
        new_pos = self.state.getNextPos()
        self.rect.move((self.pos[0], new_pos[1] - self.pos[1]))
        self.pos = new_pos
        

    def changeDown(self):
        self.state = MovingDown(self)
        self.currentImage = self.dic_images['down']

        
