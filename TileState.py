from State import *

class TileState:
    def __init__(self, image):
        self.image = image

    def getImage(self):
        return self.image

class HoleClosed(TileState):
    def interact(self, tile, character):
        if character.hasKey():
            tile.open()
        else:
            print "The hole is locked! you need a key"

class HoleOpened(TileState):
    def interact(self, tile, character):
        print "The hole is opened"


class KeyObtained(TileState):
    def interact(self, tile, character):
        pass

class KeyUnobtained(TileState):
    def interact(self, tile, character):
        print "The character has obtained a Key!"
        tile.obtain()
        character.addKey()
    
class HeartObtained(TileState):
    def interact(self, tile, character):
        pass

class HeartUnobtained(TileState):
    def interact(self, tile, character):
        print "The character has obtained an Extra Life!"
        tile.obtain()
        character.addLife()