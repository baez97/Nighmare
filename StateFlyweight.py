from State import *

class StateFlyweight:
    def __init__(self, guy):
        self.movingUp = MovingUp(guy)
        self.movingDown = MovingDown(guy)
        self.movingLeft = MovingLeft(guy)
        self.movingRight = MovingRight(guy)
        self.stopped = Stopped(guy)

    def getMovingUp(self):
        return self.movingUp

    def getMovingDown(self):
        return self.movingDown
        
    def getMovingLeft(self):
        return self.movingLeft

    def getMovingRight(self):
        return self.movingRight

    def getStopped(self):
        return self.stopped

    