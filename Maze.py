import sys, pygame
from pygame.locals import *
from Tile import *

class Maze:
    def paintTiles(self):
        for line in self.objects:
            for object in line:
                object.paint(self)

    def moveBalls(self):
        for ball in self.balls:
            ball.move()

    def moveEnemies(self):
        for enemy in self.enemies:
            enemy.move()

    def paintCharacter(self):
        if self.game.locked:
            self.game.paint(self.black, (0,-10))
        self.game.paintCharacter() 

    def paintAll(self):
        #if not (self.game.isAttackingLeft() or self.game.isPoweringUp()): 
        
        self.paintTiles()
        self.paintEnemies()
        self.repaintEnemiesFort()
        self.paintCharacter()
        if not self.game.isLocked():
            self.paintFront()
        self.paintBalls()
        self.paintLife()
        self.paintKey()
        self.paintMedals()
    
    def paintGroundTile(self, x, y):
        real_pos = self.getRealGround(x,y)
        self.game.paint(self.ground_img, real_pos)
    
    def paintObstacleTile(self, x, y):
        real_pos = self.getRealObstacle(x, y)
        self.game.paint(self.obstacle_img, real_pos)
    
    def paintWallTile(self, x, y):
        real_pos = self.getRealWall(x, y)
        self.game.paint(self.wall_img, real_pos)

    def paintTileDecorator(self, image, x, y):
        real_pos = self.getRealGround(x, y)
        self.game.paint(image, real_pos)

    def paintKeyDecorator(self, image, x, y):
        real_pos = self.getRealObstacle(x, y)
        self.game.paint(image, (real_pos[0] + 10,real_pos[1]))

    def paintHeartDecorator(self, image, x, y):
        real_pos = self.getRealGround(x, y)
        self.game.paint(image, (real_pos[0] + 10,real_pos[1]))

    def paintMedalDecorator(self, image, x, y):
        real_pos = self.getRealGround(x, y)
        self.game.paint(image, (real_pos[0] + 10, real_pos[1]))

    def paintFront(self):
        self.game.paintFront()

    def paintBalls(self):
        for ball in self.balls:
            ball.paint()

    def paintEnemies(self):
        for enemy in self.enemies:
            enemy.paint()
    
    def paintLife(self):
        self.game.paintLife()

    def paintKey(self):
        self.game.paintKey()

    def paintMedals(self):
        self.game.paintMedals()

    def repaintEnemiesFort(self):
        for tile in self.enemiesFort:
            tile.paint(self)

    def addBall(self, ball):
        self.balls.append(ball)

    def addEnemy(self, enemy):
        self.enemies.append(enemy)

    def rePaint(self, pos):
        obj = self.objects[pos[0]/50][((pos[1]+30)/40) + 1]
        obj_r = self.objects[(pos[0]+23)/50][((pos[1]+30)/40) + 1]
        if obj.isObstacle()[1] > 0:
            obj.paint(self)
        if obj_r.isObstacle()[1] > 0:
            obj_r.paint(self)

    def getRealGround(self, x, y):
        real_x = x*50
        real_y = y*40 + 20
        return (real_x, real_y)

    def getRealObstacle(self, x, y):
        real_x = x*50
        real_y = y*40
        return (real_x, real_y)

    def getRealWall(self, x, y):
        real_x = x*50
        real_y = y*40 - 20
        return (real_x, real_y)

    def canMoveUp(self, new_pos):
        x, y = new_pos
        
        cell_a = self.objects[x/50][y/40].isObstacle()
        if cell_a[0] > 0:
            return self.getRealGround(cell_a[0], cell_a[1])[1]

        cell_b = self.objects[(x + 24)/50][y/40].isObstacle()
        if cell_b[0] > 0:
            return self.getRealGround(cell_b[0], cell_b[1])[1]

        return -1

    def canMoveRight(self, new_pos):
        x, y = new_pos
        
        cell_a = self.objects[x/50][(y+30)/40].isObstacle()
        if cell_a[0] > 0:
            return self.getRealGround(cell_a[0], cell_a[1])[0]

        cell_b = self.objects[x/50][(y+50)/40].isObstacle()
        
        if cell_b[0] > 0:
            return self.getRealGround(cell_b[0], cell_b[1])[0]

        return -1

    def canMoveDown(self, new_pos):
        x, y = new_pos

        cell_a = self.objects[x/50][y/40].isObstacle()
        if cell_a[0] > 0:
            return self.getRealGround(cell_a[0], cell_a[1])[1]

        cell_b = self.objects[(x+24)/50][y/40].isObstacle()
        if cell_b[0] > 0:
            return self.getRealGround(cell_b[0], cell_b[1])[1]

        return -1

    def canMoveLeft(self, new_pos):
        x, y = new_pos
        
        cell_a = self.objects[x/50][(y+30)/40].isObstacle()
        if cell_a[0] >= 0:
            return self.getRealGround(cell_a[0], cell_a[1])[0]

        cell_b = self.objects[x/50][(y+50)/40].isObstacle()
        
        if cell_b[0] >= 0:
            return self.getRealGround(cell_b[0], cell_b[1])[0]

        return -1
        
    def deleteBall(self, ball):
        self.balls.remove(ball)

    def getEnemies(self):
        return self.enemies

    def getCell(self, x, y):
        return self.objects[x/50][y/40]

    def goTo(self, maze):
        self.game.changeMazeTo(maze)


class TopMaze(Maze):
    def __init__(self, game, factory):
        self.game = game
        line = []
        self.objects = []
        self.balls = []
        self.enemies = []
        self.enemiesFort = []
        for i in range(0,20):
            for j in range(0,20):
                if (j in (0, 19) or i in (0, 19)):
                    line.append(factory.makeWallTile(i, j))
                elif i%7==6 or j%7==6 and i not in range(6,13):
                    line.append(factory.makeObstacleTile(i,j))
                elif i==3 and j==16:
                    line.append(factory.makeGoldMedalTile(i,j))
                    #line.append(factory.makeKeyTile(i,j))
                elif i==4 and j==16:
                    line.append(factory.makeRedMedalTile(i,j))
                elif i==5 and j==16:
                    line.append(factory.makeBlueMedalTile(i,j))
                elif i==2 and j==16:
                    line.append(factory.makeOpenedHoleTile(i,j, self, 'underground'))
                elif i==17 and (j in (4,5,14,15)) or (i,j) ==(18,4):
                    line.append(factory.makeObstacleTile(i,j))
                elif (i,j) == (18,15):
                    fortObstacle = factory.makeObstacleTile(i,j)
                    line.append(fortObstacle)
                    self.enemiesFort.append(fortObstacle)
                else:
                    line.append(factory.makeGroundTile(i,j))
            self.objects.append(line)
            line = []
        self.enemiesFort.append(self.objects[18][6])
        self.addEnemy(factory.makeLeftEnemy(game, (895, 170), 0))
        self.addEnemy(factory.makeRightEnemy(game, (50, 350), 10))
        self.addEnemy(factory.makeRightEnemy(game, (70, 390), 15))
        self.addEnemy(factory.makeLeftEnemy(game, (895, 530), 0))

        self.ground_img   = pygame.image.load('images/GroundTile.png')
        self.obstacle_img = pygame.image.load('images/GrassTile.png')
        self.wall_img = pygame.image.load('images/WallTile.png')
        self.black = pygame.image.load('images/Black.png')

class UndergroundMaze(Maze):
    def __init__(self, game, factory):
        self.game = game
        line = []
        self.objects = []
        self.balls = []
        self.enemies = []
        self.enemiesFort = []
        for i in range(0,20):
            for j in range(0,20):
                if (j in (0, 19) or i in (0, 19)):
                    line.append(factory.makeWallTile(i, j))
                elif i%7==6 or j%7==6 and i not in range(6,13):
                    line.append(factory.makeObstacleTile(i,j))
                elif i==3 and j==16:
                    line.append(factory.makeKeyTile(i,j))
                elif i==2 and j==16:
                    line.append(factory.makeHeartTile(i,j))
                elif i==5 and j==16:
                    line.append(factory.makeOpenedHoleTile(i,j, self, 'top'))
                elif i==17 and (j in (4,5,14,15)) or (i,j) ==(18,4):
                    line.append(factory.makeObstacleTile(i,j))
                elif (i,j) == (18,15):
                    fortObstacle = factory.makeObstacleTile(i,j)
                    line.append(fortObstacle)
                    self.enemiesFort.append(fortObstacle)
                else:
                    line.append(factory.makeGroundTile(i,j))
            self.objects.append(line)
            line = []
        self.enemiesFort.append(self.objects[18][6])
        self.addEnemy(factory.makeLeftEnemy(game, (895, 170), 0))
        self.addEnemy(factory.makeRightEnemy(game, (50, 350), 10))
        self.addEnemy(factory.makeRightEnemy(game, (70, 390), 15))
        self.addEnemy(factory.makeLeftEnemy(game, (895, 530), 0))

        self.ground_img   = pygame.image.load('images/WallTile.png')
        self.obstacle_img = pygame.image.load('images/RockTile.png')
        self.wall_img = pygame.image.load('images/WallStone.png')
        self.black = pygame.image.load('images/Black.png')

    def getRealObstacle(self, x, y):
        real_x = x*50
        real_y = y*40 + 20
        return (real_x, real_y)

    def paintKeyDecorator(self, image, x, y):
        real_pos = self.getRealObstacle(x, y)
        self.game.paint(image, (real_pos[0] + 10, real_pos[1] - 20))
