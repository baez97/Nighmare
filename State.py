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
        self.guy.attack()

    def isAttackingRight(self):
        return True

    def attack(self, counter, superstate):
        superstate.attackRight(counter)

class AttackingLeft(State):
    def __init__(self, guy):
        self.guy = guy
        
    def move(self):
        self.guy.attack()

    def isAttackingLeft(self):
        return True

    def attack(self, counter, superstate):
        superstate.attackLeft(counter)
    
    

class SuperState:
    def __init__(self, guy, dic, factory):
        self.stateFly = factory.makeStateFlyweight(guy)
        self.state = self.stateFly.getStopped()
        self.dic = dic
        self.guy = guy
        self.currentImg = self.dic['stopped']
        self.left_images  = (dic['a_left_1'],  dic['a_left_2'],  dic['a_left_3'] )
        self.right_images = (dic['a_right_1'], dic['a_right_2'], dic['a_right_3'])
    def changeUp(self):
        self.state = self.stateFly.getMovingUp()
        self.currentImg = self.dic['up']
    def changeDown(self):
        self.state = self.stateFly.getMovingDown()
        self.currentImg = self.dic['down']
    def changeRight(self):
        self.state = self.stateFly.getMovingRight()
        self.currentImg = self.dic['right']
    def changeLeft(self):
        self.state = self.stateFly.getMovingLeft()
        self.currentImg = self.dic['left']
    def changeStopped(self):
        self.state = self.stateFly.getStopped()
        self.currentImg = self.dic['stopped']
    def changeAttackingRight(self):
        self.state = self.stateFly.getAttackingRight()
        self.currentImg = self.dic['a_right_1']
    def changeAttackingLeft(self):
        self.state = self.stateFly.getAttackingLeft()
        self.currentImg = self.dic['a_left_1']

    def getImg(self):
        return self.currentImg

    def isUp(self):
        return self.state.isUp()
    def isDown(self):
        return self.state.isDown()
    def isRight(self):
        return self.state.isRight()
    def isLeft(self):
        return self.state.isLeft()
    def isStopped(self):
        return self.state.isStopped()
    def isAttackingLeft(self):
        return self.state.isAttackingLeft()
    def isAttackingRight(self):
        return self.state.isAttackingRight()

    def getNextPos(self):
        return self.state.getNextPos()
    def getNextLimit(self):
        return self.state.getNextLimit()

    def move(self):
        self.state.move()

    def attack(self, counter):
        self.state.attack(counter, self)
        
    def attackLeft(self, counter):
        if counter == 0:
            self.guy.pos = (self.guy.pos[0] - 15, self.guy.pos[1])
        if counter < 3:
            self.currentImg = self.left_images[counter]
        elif counter < 7:
            self.currentImg = self.left_images[2]
        else:
            self.guy.pos = (self.guy.pos[0] + 15, self.guy.pos[1])
            self.changeStopped()

    def attackRight(self, counter):
        if counter < 3:
            self.currentImg = self.right_images[counter]
        elif counter < 7:
            self.currentImg = self.right_images[2]
        else:
            self.changeStopped()

class SuperSaiyan(SuperState):
    def attackRight(self, counter):
        if counter < 3:
            self.currentImg = self.right_images[counter]
        elif counter < 7:
            self.currentImg = self.right_images[2]
        else:
            self.changeStopped()

class Normal(SuperState):
    def attackRight(self, counter):
        if counter < 3:
            self.currentImg = self.right_images[counter]
        elif counter < 7:
            self.currentImg = self.right_images[2]
        else:
            self.changeStopped()



    
