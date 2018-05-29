from Character import *
import sys, pygame
from pygame.locals import *
from Maze import *
from Tile import *
from FactoryMethod import *

class Game:
    def __init__(self, factory):
        self.maze = factory.makeMaze(self)
        self.character = factory.makeCharacter(self)
        self.display = pygame.display.set_mode((1000, 840))
        self.fpsClock = pygame.time.Clock()
        self.locked = False

    def run(self):
        pygame.init()
        while True:
            self.maze.paintAll()

            if (not self.locked):
                self.moveBalls()
                self.moveEnemies()

            self.character.move()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                elif event.type == KEYDOWN and not self.locked:
                    if event.key == K_DOWN:
                        self.character.changeDown()
                    if event.key == K_LEFT:
                        self.character.changeLeft()
                    if event.key == K_RIGHT:
                        self.character.changeRight()
                    if event.key == K_UP:
                        self.character.changeUp()
                    if event.key == K_d:
                        self.character.changeAttackRight()
                    if event.key == K_a:
                        self.character.changeAttackLeft()
                    if event.key == K_e:
                        self.character.changePoweringUp()
                    if event.key == K_q:
                        self.character.changeNormal()

                elif event.type == KEYUP:
                    if self.character.state.isUp() and event.key ==K_UP:
                        self.character.changeStopped()
                    elif self.character.state.isDown() and event.key ==K_DOWN:
                        self.character.changeStopped()
                    elif self.character.state.isRight() and event.key ==K_RIGHT:
                        self.character.changeStopped()
                    elif self.character.state.isLeft() and event.key ==K_LEFT:
                        self.character.changeStopped()


            pygame.display.update()
            self.fpsClock.tick(30)

    def paint(self, image, position):
        self.display.blit(image, (position[0], position[1] + 10))

    def canMoveUp(self, new_pos):
        return self.maze.canMoveUp(new_pos)

    def canMoveDown(self, new_pos):
        return self.maze.canMoveDown(new_pos)

    def canMoveRight(self, new_pos):
        return self.maze.canMoveRight(new_pos)

    def canMoveLeft(self, new_pos):
        return self.maze.canMoveLeft(new_pos)

    def paintCharacter(self):
        self.character.paint()

    def paintFront(self):
        self.maze.rePaint(self.character.getPos())

    def addBall(self, ball):
        self.maze.addBall(ball)

    def addEnemy(self, enemy):
        self.maze.addEnemy(enemy)

    def moveBalls(self):
        self.maze.moveBalls()

    def moveEnemies(self):
        self.maze.moveEnemies()

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def deleteBall(self, ball):
        self.maze.deleteBall(ball)

    def isAttackingLeft(self):
        return self.character.isAttackingLeft()

    def isPoweringUp(self):
        return self.character.isPoweringUp()

fm = FactoryMethod()
game = Game(fm)
game.addEnemy(fm.makeRightEnemy(game, (150, 102), 0))
game.addEnemy(fm.makeRightEnemy(game, (150, 370), 10))
game.addEnemy(fm.makeRightEnemy(game, (150, 623), 0))
game.run()
