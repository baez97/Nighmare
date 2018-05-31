from Tile import *

class TileDecorator(Tile):
    def __init__(self, x, y, component, state_string, state_dic):
        super(TileDecorator, self).__init__(x, y)
        self.component = component
        self.state_dic = state_dic
        self.state = state_dic[state_string]

    def interact(self, character):
        self.state.interact(self, character)


class HoleDecorator(TileDecorator):
    def __init__(self, x, y, component, state_string, state_dic, maze_1, maze_2):
        super(HoleDecorator, self).__init__(x, y, component, state_string, state_dic)
        self.maze_1 = maze_1
        self.maze_2 = maze_2

    def paint(self, maze):
        self.component.paint(maze)
        image = self.state.getImage()
        maze.paintTileDecorator(image, self.cel_x, self.cel_y)

    def open(self):
        self.state = self.state_dic['opened']

    def enter(self):
        self.maze_1.goTo(self.maze_2)

class KeyDecorator(TileDecorator):
    def paint(self, maze):
        self.component.paint(maze)
        image = self.state.getImage()
        maze.paintKeyDecorator(image, self.cel_x, self.cel_y)

    def obtain(self):
        self.state = self.state_dic['key_obtained']

class HeartDecorator(TileDecorator):
    def paint(self, maze):
        self.component.paint(maze)
        image = self.state.getImage()
        maze.paintHeartDecorator(image, self.cel_x, self.cel_y)

    def obtain(self):
        self.state = self.state_dic['heart_obtained']

class MedalDecorator(TileDecorator):
    def paint(self, maze):
        self.component.paint(maze)
        image = self.state.getImage()
        maze.paintMedalDecorator(image, self.cel_x, self.cel_y)

class RedMedalDecorator(MedalDecorator):
    def obtain(self):
        self.state = self.state_dic['obtained']

class BlueMedalDecorator(MedalDecorator):
    def obtain(self):
        self.state = self.state_dic['obtained']

class GoldMedalDecorator(MedalDecorator):
    def obtain(self):
        self.state = self.state_dic['obtained']



