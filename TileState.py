from State import *

class TileState:
    def __init__(self, image):
        self.image = image

    def getImage(self):
        return self.image

class HoleClosed(TileState):
    def interact(self, tile, character):
        print "The hole is locked! you need a key"

class HoleOpened(TileState):
    def interact(self, tile, character):
        print "The hole is opened"