from Character import *

class Ball(MovableObject):
    def __init__(self, game, dic, stateDic, direction, pos, colissionManager):
        super(Ball, self).__init__(game, dic, pos)
        self.img_dic = dic
        self.state_dic = stateDic
        self.image = dic[direction]
        self.state = stateDic[direction]
        self.img_fading = (dic['f_1'], dic['f_2'], dic['f_3'])
        self.width = self.image.get_rect().right
        self.height = self.image.get_rect().bottom
        self.damage = 20
        self.colissionManager = colissionManager
        

    def move(self):
        self.state.move(self)

    def moveRight(self):
        if not self.colissionManager.checkRightColission(self):
            self.pos = (self.pos[0] + 10, self.pos[1])
        
    def moveLeft(self):
        if not self.colissionManager.checkLeftColission(self):
            self.pos = (self.pos[0] - 10, self.pos[1])

    def fade(self):
        if self.counter > 2:
            self.deleteMe()
        else:
            self.image = self.img_fading[self.counter]
            self.counter += 1

    def changeFading(self):
        self.state = self.state_dic['fading']

    def paint(self):
        self.game.paint(self.image, self.pos)

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def deleteMe(self):
        self.game.deleteBall(self)

    def getDamage(self):
        return self.damage

    def getVelocity(self):
        return 10
