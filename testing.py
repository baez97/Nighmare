from Game import *
from FactoryMethod import *
import pygame

class Nightmare_test:
    def __init__(self):
        self.fm = FactoryMethod()
        self.game = Game(self.fm)
        self.character = self.game.getCharacter()
        self.counter = 0
        self.total = 13

    def run(self):
        self.counter += self.test_locked()
        self.counter += self.test_character_initial_pos()
        self.counter += self.test_character_initial_basicstate()
        self.counter += self.test_character_initial_superstate()
        self.counter += self.test_character_changing_superState()
        self.counter += self.test_character_changing_basicState()
        self.counter += self.test_character_movement()
        self.counter += self.test_top_maze_objects()
        self.counter += self.test_underground_maze_objects()
        self.counter += self.test_game_dead()
        self.counter += self.test_game_win()
        self.counter += self.test_key_closed()

        if self.counter == self.total:
            #print "All test passed!"
            print('\x1b[6;30;42m' + 'Success!                     ' + '\x1b[0m')
        else:
            print('\x1b[6;30;41m' + 'Failure!                     ' + '\x1b[0m')
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

    def test_top_maze_objects(self):
        maze = self.game.getMaze()
        objects = maze.getObjects()
        for i in range(0, 20):
            for j in range(0, 18):
                if (j in (0, 17) or i in (0, 19)):
                    if not objects[i][j].isWallTile():
                        print 'cell', (i,j), 'of the top maze should be a wall'
                        return 0
                    #line.append(factory.makeWallTile(i, j))
                elif i in (6, 13) or ((j in (6, 11)) and i not in range(6,13)):
                    if not objects[i][j].isObstacleTile():
                        print 'cell', (i,j), 'of the top maze should be an obstacle'
                        return 0
                    #line.append(factory.makeObstacleTile(i,j))
                elif i==17 and (j in (4,5,12,13)) or (i,j) ==(18,4):
                    if not objects[i][j].isObstacleTile():
                        print 'cell', (i,j), 'of the top maze should be an obstacle'
                        return 0
                    #line.append(factory.makeObstacleTile(i,j))
                elif (i,j) == (18,13):
                    if not objects[i][j].isObstacleTile():
                        print 'cell', (i,j), 'of the top maze should be an obstacle'
                        return 0
                    #fortObstacle = factory.makeObstacleTile(i,j)
                    #line.append(fortObstacle)
                    #self.enemiesFort.append(fortObstacle)
                elif (i,j) in ((2,2), (9,2)):
                    if not objects[i][j].isKeyTile():
                        print 'cell', (i,j), 'of the top maze should be a key'
                        return 0
                    #line.append(factory.makeKeyTile(i,j))
                elif (i,j) in ((4,4), (18,3), (18,1), (2,13), (16, 13), (16, 15), (11,11)):
                    if not objects[i][j].isHoleTile():
                        print 'cell', (i,j), 'of the top maze should be a hole'
                        return 0
                    if not objects[i][j].isOpened():
                        print 'hole at cell', (i,j), 'of the top maze should be opened'
                        return 0
                    #line.append(factory.makeOpenedHoleTile(i, j, self, 'underground'))
                elif (i,j) in ((4,15), (8,11), (18,15)):
                    if not objects[i][j].isHoleTile():
                        print 'cell', (i,j), 'of the top maze should be a hole'
                        return 0
                    if not objects[i][j].isClosed():
                        print 'hole at cell', (i,j), 'of the top maze should be closed'
                        return 0
                    #line.append(factory.makeClosedHoleTile(i, j, self, 'underground'))
                elif (i,j) == (15,15):
                    if not objects[i][j].isRedMedalTile():
                        print 'cell', (i,j), 'should be a Red Medal'
                        return 0
                    #line.append(factory.makeRedMedalTile(i,j))
                elif j == 2 and i in (3,8):
                    if not objects[i][j].isHeartTile():
                        print 'cell', (i,j), 'of the top maze should be a heart'
                        return 0
                    #line.append(factory.makeHeartTile(i,j))
                else:
                    if not objects[i][j].isGroundTile():
                        print 'cell', (i,j), 'of the top maze should be ground'
                        return 0
                    #line.append(factory.makeGroundTile(i,j))
        
        return 1

    def test_underground_maze_objects(self):
        self.game.changeMazeTo('underground')
        maze = self.game.getMaze()
        objects = maze.getObjects()
        
        for i in range(0,20):
            for j in range(0,18):
                if (j in (0, 17) or i in (0, 19)):
                    if not objects[i][j].isWallTile():
                        print 'cell', (i,j), 'of the underground maze should be a wall'
                        return 0
                    #line.append(factory.makeWallTile(i, j))
                elif (i==5 and j <11) or (i==17 and j not in (1,15,17)) or (j == 14 and i not in (1,2,3,18)):
                    if not objects[i][j].isObstacleTile():
                        print 'cell', (i,j), 'of the underground maze should be an obstacle'
                        return 0
                    #line.append(factory.makeObstacleTile(i,j))
                elif (j==10 and i in range(6,11)) or (j==12 and i in range(7,17)):
                    if not objects[i][j].isObstacleTile():
                        print 'cell', (i,j), 'of the underground maze should be an obstacle'
                        return 0
                    #line.append(factory.makeObstacleTile(i,j))
                elif (i==3 and j in range(12,17)) or (j==12 and i in (1,2,3)):
                    if not objects[i][j].isObstacleTile():
                        print 'cell', (i,j), 'of the underground maze should be an obstacle'
                        return 0
                    #line.append(factory.makeObstacleTile(i,j))
                elif (j == 11 and i in (7,10) or (i,j) in ((18,2), (17,15), (17,16))):
                    if not objects[i][j].isObstacleTile():
                        print 'cell', (i,j), 'of the underground maze should be an obstacle'
                        return 0
                    #line.append(factory.makeObstacleTile(i,j))
                elif (i,j) in ((4,4), (18,3), (18,1), (2,13), (16, 13), (16, 15), (11,11), (4,15), (8,11), (18,15)):
                    if not objects[i][j].isHoleTile():
                        print 'cell', (i,j), 'of the underground maze should be a hole'
                        return 0
                    if not objects[i][j].isOpened():
                        print 'hole at cell', (i,j), 'of the underground maze should be opened'
                        return 0
                    #line.append(factory.makeOpenedHoleTile(i, j, self, 'top'))
                elif (i,j) == (9,11):
                    if not objects[i][j].isGoldMedalTile():
                        print 'cell', (i,j), 'should be a Gold Medal'
                        return 0
                    #line.append(factory.makeGoldMedalTile(i,j))
                elif (i,j) == (17,1):
                    if not objects[i][j].isBlueMedalTile():
                        print 'cell', (i,j), 'should be a Blue Medal'
                        return 0
                    #line.append(factory.makeBlueMedalTile(i,j))
                elif (i,j) == (1,15):
                    if not objects[i][j].isKeyTile():
                        print 'cell', (i,j), 'of the underground maze should be a key'
                        return 0
                    #line.append(factory.makeKeyTile(i,j))
                else:
                    if not objects[i][j].isGroundTile():
                        print 'cell', (i,j), 'of the underground maze should be ground'
                        return 0
                    #line.append(factory.makeGroundTile(i,j))

        self.game.changeMazeTo('top')
        return 1    

    
    def test_game_dead(self):
        self.game.hurtCharacter(6)
        if not self.game.dead:
            print 'The game is not ending when character dies'
            return 0
        self.game.character.life = 6
        return 1

    def test_game_win(self):
        enemies = self.game.getEnemies()
        for i in range(0, 4):
            self.game.killEnemy(enemies[0])
        if not self.game.won:
            print 'The game is not ending when all enemies are killed'
            return 0
        self.game.maze.enemies = enemies
        return 1

    def test_key_closed(self):
        maze = self.game.getMaze()
        objects = maze.getObjects()
        hole = objects[4][15]
        hole.interact(self.character)
        if not hole.isClosed():
            print 'The holes are getting opened without key'
            return 0
        self.character.addKey()
        hole.interact(self.character)
        self.character.useKey()
        if not hole.isOpened():
            print 'The holes are not getting opened with key'
            return 0
        if self.character.hasKey():
            print 'The character is not loosing the key when opening a hole'
            return 0
        return 1


test = Nightmare_test()
test.run()
