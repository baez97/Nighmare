from Character import *

class Ball(MovableObject):
    def __init__(self, game, dic, stateDic, direction, pos):
        super(Ball, self).__init__(game, dic, pos)
        self.img_dic = dic
        self.state_dic = stateDic
        self.image = dic[direction]
        self.state = stateDic[direction]
        self.img_fading = (dic['f_1'], dic['f_2'], dic['f_3'])
        self.wide = self.image.get_rect().right
        self.height = self.image.get_rect().bottom
        

    def move(self):
        self.state.move(self)

    def moveRight(self):
        if self.pos[0] + self.wide >= 950:
            self.state = self.state_dic['fading']
        else:
            self.pos = (self.pos[0] + 10, self.pos[1])
        
    def moveLeft(self):
        if self.pos[0] <= 50:
            self.state = self.state_dic['fading']
        else:
            self.pos = (self.pos[0] - 10, self.pos[1])

    def fade(self):
        if self.counter > 2:
            self.deleteMe()
        else:
            self.image = self.img_fading[self.counter]
            self.counter += 1

    def paint(self):
        self.game.paint(self.image, self.pos)

    def deleteMe(self):
        self.game.deleteBall(self)
