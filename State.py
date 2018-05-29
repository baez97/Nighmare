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
    def isAttackingRight(self):
        return False

class MovingUp(State):
    def __init__(self, guy):
        self.velocity = 10
        self.guy = guy

    def move(self):
        self.guy.moveUp()

    def getNextPos(self, velocity):
        return (self.guy.pos[0], self.guy.pos[1] - velocity)

    def getNextLimit(self, velocity):
        return (self.guy.pos[0], self.guy.pos[1] - velocity)

    def isUp(self):
        return True

class MovingDown(State):
    def __init__(self, guy):
        self.velocity = 10
        self.guy = guy

    def move(self):
        self.guy.moveDown()

    def getNextPos(self, velocity):
        return (self.guy.pos[0], self.guy.pos[1] + velocity)

    def getNextLimit(self, velocity):
        return (self.guy.pos[0], self.guy.pos[1] + velocity + 34)

    def isDown(self):
        return True

class MovingLeft(State):
    def __init__(self, guy):
        self.velocity = 10
        self.guy = guy

    def move(self):
        self.guy.moveLeft()

    def getNextPos(self, velocity):
        return (self.guy.pos[0] - velocity, self.guy.pos[1])

    def getNextLimit(self, velocity):
        return (self.guy.pos[0] - velocity, self.guy.pos[1])

    def isLeft(self):
        return True

class MovingRight(State):
    def __init__(self, guy):
        self.velocity = 10
        self.guy = guy

    def move(self):
        self.guy.moveRight()

    def getNextPos(self, velocity):
        return (self.guy.pos[0] + velocity, self.guy.pos[1])

    def getNextLimit(self, velocity):
        return (self.guy.pos[0] + velocity + 50, self.guy.pos[1])

    def isRight(self):
        return True

class Stopped(State):
    def __init__(self, guy):
        self.velocity = 10
        self.guy = guy
    
    def move(self):
        pass

    def getNextPos(self, velocity):
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
    
    

class SuperState(object):
    def __init__(self, guy, dic, factory):
        self.stateFly = factory.makeStateFlyweight(guy)
        self.factory = factory
        self.state = self.stateFly.getStopped()
        self.dic = dic
        self.guy = guy
        self.currentImg = self.dic['stopped']
        self.left_images  = (dic['a_left_1'],  dic['a_left_2'],  dic['a_left_3'] )
        self.right_images = (dic['a_right_1'], dic['a_right_2'], dic['a_right_3'])
        self.velocity = 10

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
    def isPoweringUp(self):
        return False

    def getNextPos(self):
        return self.state.getNextPos(self.velocity)
    def getNextLimit(self):
        return self.state.getNextLimit(self.velocity)

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
    def __init__(self, guy, dic, factory):
        super(SuperSaiyan, self).__init__(guy, dic, factory)
        self.velocity = 15

    def attackRight(self, counter):
        if counter < 3:
            self.currentImg = self.right_images[counter]
        elif counter == 3:
            self.guy.addBall('right', (26,5))
        elif counter < 7:
            self.currentImg = self.right_images[2]
        else:
            self.changeStopped()

    def attackLeft(self, counter):
        if counter == 0:
            self.guy.pos = (self.guy.pos[0] - 15, self.guy.pos[1])
        if counter < 3:
            self.currentImg = self.left_images[counter]
        elif counter == 3:
            self.guy.addBall('left', (-10,5))
        elif counter < 7:
            self.currentImg = self.left_images[2]
        else:
            self.guy.pos = (self.guy.pos[0] + 15, self.guy.pos[1])
            self.changeStopped()

class Normal(SuperState):
    def attackRight(self, counter):
        if counter < 3:
            self.currentImg = self.right_images[counter]
        elif counter < 7:
            self.currentImg = self.right_images[2]
        else:
            self.changeStopped()

class PoweringUp(SuperState):
    def __init__(self, guy, dic, factory):
        self.stateFly = factory.makeStateFlyweight(guy)
        self.state = self.stateFly.getStopped()
        self.dic = dic
        self.guy = guy
        self.currentImg = self.dic[0]

    def move(self):
        self.guy.powerUp()

    def powerUp(self, counter):
        if counter < 23:
            self.currentImg = self.dic[counter]
        else:
            self.guy.unlock()
            self.guy.pos = (self.guy.pos[0] + 40, self.guy.pos[1] + 40)
            self.guy.changeSuperSaiyan()

    def isPoweringUp(self):
        return True


class BallMovingRight():
    def move(self, ball):
        ball.moveRight()

class BallMovingLeft():
    def move(self, ball):
        ball.moveLeft()

class BallFading():
    def move(self, ball):
        ball.fade()
