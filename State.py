class State(object):
    def __init__(self, guy):
        self.velocity = 10
        self.guy = guy

    def isUp(self):
        return False
    def isDown(self):
        return False
    def isRight(self):
        return False
    def isLeft(self):
        return False
    def isAttackingLeft(self):
        return False

class MovingUp(State):
    def __init__(self, guy):
        self.velocity = 10
        self.guy = guy

    def move(self):
        self.guy.moveUp()

    def getNextPos(self):
        return (self.guy.pos[0], self.guy.pos[1] - self.velocity)

    def getNextLimit(self):
        return (self.guy.pos[0], self.guy.pos[1] - self.velocity)

    def isUp(self):
        return True

class MovingDown(State):
    def __init__(self, guy):
        self.velocity = 10
        self.guy = guy

    def move(self):
        self.guy.moveDown()

    def getNextPos(self):
        return (self.guy.pos[0], self.guy.pos[1] + self.velocity)

    def getNextLimit(self):
        return (self.guy.pos[0], self.guy.pos[1] + self.velocity + 34)

    def isDown(self):
        return True

class MovingLeft(State):
    def __init__(self, guy):
        self.velocity = 10
        self.guy = guy

    def move(self):
        self.guy.moveLeft()

    def getNextPos(self):
        return (self.guy.pos[0] - self.velocity, self.guy.pos[1])

    def getNextLimit(self):
        return (self.guy.pos[0] - self.velocity, self.guy.pos[1])

    def isLeft(self):
        return True

class MovingRight(State):
    def __init__(self, guy):
        self.velocity = 10
        self.guy = guy

    def move(self):
        self.guy.moveRight()

    def getNextPos(self):
        return (self.guy.pos[0] + self.velocity, self.guy.pos[1])

    def getNextLimit(self):
        return (self.guy.pos[0] + self.velocity + 50, self.guy.pos[1])

    def isRight(self):
        return True

class Stopped(State):
    def __init__(self, guy):
        self.velocity = 10
        self.guy = guy
    
    def move(self):
        pass

    def getNextPos(self):
        return self.guy.pos

class AttackingRight(State):
    def __init__(self, guy):
        self.guy = guy
        
    def move(self):
        self.guy.attackRight()

class AttackingLeft(State):
    def __init__(self, guy):
        self.guy = guy
        
    def move(self):
        self.guy.attackLeft()

    def isAttackingLeft(self):
        return True

    
