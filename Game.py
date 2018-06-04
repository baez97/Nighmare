from Character import *
import sys, pygame
from pygame.locals import *
from Maze import *
from Tile import *
from FactoryMethod import *

class Game:
    def __init__(self, factory):
        self.factory = factory
        self.mazes = {'top':factory.makeTopMaze(self),
                      'underground':factory.makeUndergroundMaze(self)}
        self.maze = self.mazes['top']
        self.character = factory.makeCharacter(self)
        self.display = pygame.display.set_mode((1000, 720))
        self.display.fill((255, 255, 255))
        pygame.display.set_caption('Vegeta\'s Nightmare')
        self.fpsClock = pygame.time.Clock()
        self.locked = False
        self.colissionManager = factory.makeColissionManager(self)
        self.banner = pygame.image.load('images/banner.png')
        self.won = False
        self.dead = False

    def run(self):
        pygame.init()
        while True:
            
            self.maze.paintAll()
            #self.display.blit(self.banner, (1000, 0))
            if (not self.locked):
                self.moveBalls()
                self.moveEnemies()

            elif self.dead:
                self.paintDead()

            elif self.won:
                self.paintWin()

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
                        self.character.interact()
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
        self.display.blit(image, (position[0], position[1] + 15))

    def paintKey(self):
        if self.character.hasKey():
            self.paint(self.factory.makeKeyImage(), (10, 630))

    def paintLife(self):
        num_lives = self.character.getLife()
        for i in range(0,num_lives):
            x = 50 + 30*i
            y = 670
            self.paint(self.factory.makeHeartImage(), (x,y))

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

    def addBall(self, ball_pos, direction):
        ball = self.factory.makeBall(self, direction, ball_pos)
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

    def isLocked(self):
        return self.locked

    def deleteBall(self, ball):
        self.maze.deleteBall(ball)

    def isAttackingLeft(self):
        return self.character.isAttackingLeft()

    def isPoweringUp(self):
        return self.character.isPoweringUp()

    def getCharacterPosition(self):
        return self.character.getPos()

    def getCharacterWidth(self):
        return self.character.getWidth()

    def getCharacterHeight(self):
        return self.character.getHeight()

    def hurtCharacter(self, damage):
        self.character.hurt(damage)

    def getColissionManager(self):
        return self.colissionManager

    def getEnemies(self):
        return self.maze.getEnemies()
        
    def getCell(self, pos):
        ground_x = pos[0] + self.getCharacterWidth()/2
        ground_y = pos[1] + self.getCharacterHeight() - 30
        return self.maze.getCell(ground_x, ground_y)

    def changeMazeTo(self, maze):
        self.maze = self.mazes[maze]

    def paintMedals(self):
        self.character.paintMedalImages()

    def paintBlueMedal(self):
        self.paint(self.factory.makeBlueImage(), (10, 500))

    def paintRedMedal(self):
        self.paint(self.factory.makeRedImage(), (10, 550))

    def paintGoldMedal(self):
        self.paint(self.factory.makeGoldImage(), (10, 450))

    def getCharacter(self):
        return self.character

    def die(self):
        self.lock()
        self.dead = True

    def win(self):
        self.lock()
        self.won = True

    def paintDead(self):
        self.paint(self.factory.getDeadImage(), (200,200))

    def paintWin(self):
        self.paint(self.factory.getWinImage(), (200,200))

    def killEnemy(self, enemy):
        self.maze.killEnemy(enemy)
        
fm = FactoryMethod()
game = Game(fm)
game.run()
