from Character import *

class Enemy(MovableObject):
    def __init__(self, game, dic, pos, counter, factory):
        super(Enemy, self).__init__(game, dic, pos)
        self.image = self.dic_images[0]
        self.factory = factory
        self.counter = counter

    def paint(self):
        self.game.paint(self.image, self.pos)

    def move(self):
        if self.counter < 18:
            self.image = self.dic_images[0]
            self.counter += 1
        elif self.counter < 20:
            self.image = self.dic_images[1]
            self.counter += 1
        elif self.counter == 20:
            self.addBall()
            self.counter += 1
        elif self.counter < 25:
            self.image = self.dic_images[2]
            self.counter += 1
        else:
            self.image = self.dic_images[0]
            self.counter = 0

    def addBall(self):
        ball_pos = self.getBallPosition()
        self.createBall(ball_pos)

    def getWidth(self):
        return self.image.get_rect().right
    
    def getHeight(self):
        return self.image.get_rect().bottom

class RightEnemy(Enemy):
    def getBallPosition(self):
        return (self.pos[0] + (self.image.get_rect().right - 20), self.pos[1])

    def createBall(self, ball_pos):
        self.game.addBall(ball_pos, 'right')

class LeftEnemy(Enemy):
    def getBallPosition(self):
        return (self.pos[0], self.pos[1])

    def createBall(self, ball_pos):
        self.game.addBall(ball_pos, 'left')