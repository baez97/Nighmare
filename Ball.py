from Character import *

class Ball(MovableObject):
    def __init__(self, game, dic, direction, dir_dic, pos):
        super(Ball, self).__init__(game, dic)
        self.image = dic[direction]
        self.direction = dir_dic[direction]
        self.pos = pos
        

    def move(self):
        self.pos = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])

    def paint(self):
        self.game.paint(self.image, self.pos)
