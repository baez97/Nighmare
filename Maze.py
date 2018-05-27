import sys, pygame
from pygame.locals import *
from Tile import *

class Maze:
    def __init__(self, game, factory):
        self.game = game
        line = []
        self.objects = []
        for i in range(0,20):
            for j in range(0,20):
                if j in (0, 19) or i in (0,19) or (j%5 == 0 and i%2 != 0):
                    line.append(factory.makeObstacleTile(i,j))
                else:
                    line.append(factory.makeGroundTile(i,j))
            self.objects.append(line)
            line = []

        self.ground_img   = pygame.image.load('images/GroundTile.png')
        self.obstacle_img = pygame.image.load('images/GrassTile.png')

    def paintTiles(self):
        for line in self.objects:
            for object in line:
                object.paint(self)

    def paintCharacter(self):
        self.game.paintCharacter() 

    def paintAll(self):
        self.paintTiles()
        self.paintCharacter()
        self.paintFront()
    
    def paintGroundTile(self, x, y):
        real_pos = self.getRealGround(x,y)
        self.game.paint(self.ground_img, real_pos)
    
    def paintObstacleTile(self, x, y):
        real_pos = self.getRealObstacle(x, y)
        self.game.paint(self.obstacle_img, real_pos)

    def paintFront(self):
        self.game.paintFront()

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
        
    




