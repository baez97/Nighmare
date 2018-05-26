class State:
    def __init__(self, character):
        self.velocity = 10
        self.character = character

    def isUp(self):
        return False
    def isDown(self):
        return False
    def isRight(self):
        return False
    def isLeft(self):
        return False

class MovingUp(State):
    def move(self):
        self.character.moveUp()

    def getNextPos(self):
        return (self.character.pos[0], self.character.pos[1] - self.velocity)

    def getNextLimit(self):
        return (self.character.pos[0], self.character.pos[1] - self.velocity)

    def isUp(self):
        return True

class MovingDown(State):
    def move(self):
        self.character.moveDown()

    def getNextPos(self):
        return (self.character.pos[0], self.character.pos[1] + self.velocity)

    def getNextLimit(self):
        return (self.character.pos[0], self.character.pos[1] + self.velocity + 34)

    def isDown(self):
        return True

class MovingLeft(State):
    def move(self):
        self.character.moveLeft()

    def getNextPos(self):
        return (self.character.pos[0] - self.velocity, self.character.pos[1])

    def getNextLimit(self):
        return (self.character.pos[0] - self.velocity, self.character.pos[1])

    def isLeft(self):
        return True

class MovingRight(State):
    def move(self):
        self.character.moveRight()

    def getNextPos(self):
        return (self.character.pos[0] + self.velocity, self.character.pos[1])

    def getNextLimit(self):
        return (self.character.pos[0] + self.velocity + 50, self.character.pos[1])

    def isRight(self):
        return True

class Stopped(State):
    def move(self):
        pass

    def getNextPos(self):
        return self.character.pos