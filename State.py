class MovingUp:
    def __init__(self, character):
        self.image = 'up'
        self.velocity = 5
        self.character = character

    def move(self):
        self.character.moveUp()

    def getNextPos(self):
        return (self.character.pos[0], self.character.pos[1] + self.velocity)

class MovingDown:
    def __init__(self, character):
        self.image = 'down'
        self.velocity = 5
        self.character = character

    def move(self):
        self.character.moveDown()

    def getNextPos(self):
        return (self.character.pos[0], self.character.pos[1] + self.velocity)

    def getNextLimit(self):
        return (self.character.pos[0], self.character.pos[1] + self.velocity + 34)

class Stopped:
    def __init__(self, character):
        self.image = 'stopped'
        self.character = character

    def move(self):
        pass

    def getNextPos(self):
        return self.character.pos