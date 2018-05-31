from Tile import *

class TileDecorator(Tile):
    def __init__(self, x, y, component):
        super(TileDecorator, self).__init__(x, y)
        self.component = component

    def interact(self, character):
        self.state.interact(self, character)


class HoleDecorator(TileDecorator):
    def __init__(self, x, y, component, state_string, state_dic):
        super(HoleDecorator, self).__init__(x, y, component)
        self.state_dic = state_dic
        self.state = state_dic[state_string]

    def paint(self, maze):
        self.component.paint(maze)
        image = self.state.getImage()
        maze.paintTileDecorator(image, self.cel_x, self.cel_y)