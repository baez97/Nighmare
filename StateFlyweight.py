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

class SuperStateFlyweight:
    def __init__(self, guy, dic, factory):
        self.superSaiyan = factory.makeSuperSaiyan(guy, dic['supersaiyan'])
        self.normal = factory.makeNormal(guy, dic['normal'])
        self.poweringUp = factory.makePoweringUp(guy, dic['powerup'])

    def getSuperSaiyan(self):
        return self.superSaiyan

    def getNormal(self):
        return self.normal

    def getPoweringUp(self):
        return self.poweringUp