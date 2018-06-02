from Game import *
from FactoryMethod import *

class Nightmare_test:
    def __init__(self):
        self.fm = FactoryMethod()
        self.game = Game(self.fm)
        self.character = self.game.getCharacter()
        self.counter = 0
        self.total = 7

    def run(self):
        self.counter += self.test_locked()
        self.counter += self.test_character_initial_pos()
        self.counter += self.test_character_initial_basicstate()
        self.counter += self.test_character_initial_superstate()
        self.counter += self.test_character_changing_superState()
        self.counter += self.test_character_changing_basicState()
        self.counter += self.test_character_movement()

        if self.counter == self.total:
            print "All test passed!"
        else:
            print "Only ", self.counter, "/", self.total, "have passed"

    def test_locked(self):
        if self.game.isLocked():
            print "The Game is initially locked, it shouldn't be"
            return 0
        
        self.game.lock()

        if self.game.isLocked():
            self.game.unlock()
            
            if self.game.isLocked():
                print "The unlock method is not working properly"
                return 0

            return 1

    def test_character_initial_pos(self):
        pos = self.game.getCharacterPosition()
        if (pos != (170,620)):
            print "The initial position of Vegeta should be (80, 600)"
            return 0
        return 1

    def test_character_initial_superstate(self):
        state = self.character.getState()
        if not state.isNormal():
            print "The initial superstate should be Normal"
            return 0
        return 1

    def test_character_initial_basicstate(self):
        state = self.character.getState()
        if not state.isStopped():
            print "The initial state should be stopped"
            return 0
        return 1

    def test_character_changing_superState(self):
        self.character.changePoweringUp()
        state = self.character.getState()
        if not state.isPoweringUp():
            print "The character is not changing to PoweringUp state"
            return 0
        
        self.character.changeSuperSaiyan()
        state = self.character.getState()
        if not state.isSuperSaiyan():
            print "The character is not changing to SuperSaiyan state"
            return 0

        self.character.changeNormal()
        state = self.character.getState()
        if not state.isNormal():
            print "The character is not changing to Normal state"
            return 0

        return 1

    def test_character_changing_basicState(self):
        self.character.changeUp()
        state = self.character.getState()
        if not state.isUp():
            print "The character is not changing to MovingUp state"
            return 0
        
        self.character.changeDown()
        state = self.character.getState()
        if not state.isDown():
            print "The character is not changing to MovingDown state"
            return 0

        self.character.changeLeft()
        state = self.character.getState()
        if not state.isLeft():
            print "The character is not changing to MovingLeft state"
            return 0

        self.character.changeRight()
        state = self.character.getState()
        if not state.isRight():
            print "The character is not changing to MovingRight state"
            return 0
        
        self.character.changeStopped()
        state = self.character.getState()
        if not state.isStopped():
            print "The character is not changing to MovingLeft state"
            return 0

        return 1

    def test_character_movement(self):
        v = self.character.getVelocity()
        ini_pos = (self.character.getPos())
        self.character.changeUp()
        self.character.move()
        expected_pos = (ini_pos[0], ini_pos[1] - v)
        if not expected_pos == self.character.getPos():
            print "The character is not moving up correctly", expected_pos, self.character.getPos()            
            return 0

        self.character.changeDown()
        self.character.move()
        self.character.changeStopped()
        expected_pos = (expected_pos[0], expected_pos[1] + v)
        if not expected_pos == self.character.getPos():
            print "The character is not moving down correctly", expected_pos, self.character.getPos()
            return 0
        
        self.character.changeRight()
        self.character.move()
        expected_pos = (expected_pos[0] + v, expected_pos[1])
        if not expected_pos == self.character.getPos():
            print "The character is not moving right correctly, the position should be", expected_pos, "but it's", self.character.getPos()
            return 0

        self.character.changeLeft()
        self.character.move()
        expected_pos = (expected_pos[0] - v, expected_pos[1])
        if not expected_pos == self.character.getPos():
            print "The character is not moving left correctly", expected_pos, self.character.getPos()
            return 0

        self.character.changeStopped()
        self.character.move()
        if not expected_pos == self.character.getPos():
            print "The character is not stopping correctly", self.character.getPos()
            return 0

        return 1


test = Nightmare_test()
test.run()
