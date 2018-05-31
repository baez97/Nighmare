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
    def paint(self, maze):
        self.component.paint(maze)
        image = self.state.getImage()
        maze.paintTileDecorator(image, self.cel_x, self.cel_y)

    def open(self):
        self.state = self.state_dic['opened']

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


