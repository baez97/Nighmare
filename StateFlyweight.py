from State import *

class StateFlyweight:
    def __init__(self, guy, factory):
        self.movingUp = factory.makeMovingUp(guy)
        self.movingDown = factory.makeMovingDown(guy)
        self.movingLeft = factory.makeMovingLeft(guy)
        self.movingRight = factory.makeMovingRight(guy)
        self.stopped = factory.makeStopped(guy)
        self.attackingRight = factory.makeAttackingRight(guy)
        self.attackingLeft = factory.makeAttackingLeft(guy)

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

    def getAttackingRight(self):
        return self.attackingRight
    
    def getAttackingLeft(self):
        return self.attackingLeft

    