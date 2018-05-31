class Component(object):
    def __init__(self, pos):
        self.pos = pos
        
    def getPos(self):
        return self.pos
    def isKey(self):
        return False
    def isMedal(self):
        return False
    def isItem(self):
        return False
    def isBag(self):
        return False
    def isMedalBox(self):
        return False
    def addBlueMedal(self):
        pass
    def addRedMedal(self):
        pass
    def addGoldMedal(self):
        pass
    def hasKey(self):
        return False
    def useKey(self):
        pass
    def obtainKey(self):
        pass
    def paintMedalImages(self, game):
        pass

class Item(Component):
    def __init__(self, pos, dic_img):
        super(Item, self).__init__(pos)
        self.pos = pos
        self.dic_img = dic_img
        self.img = dic_img['empty']
        self.obtained = False

    def isItem(self):
        return True

    def obtain(self):
        self.obtained = True

class Key(Item):
    def useKey(self):
        if self.obtained:
            self.img = self.dic_img['empty']
            self.obtained = False
            return True
        else:
            return False

    def hasKey(self):
        return self.obtained

    def obtainKey(self):
        self.img = self.dic_img['obtained']
        self.obtained = True

class Composite(Component):
    def __init__(self, pos, factory):
        super(Composite, self).__init__(pos)
        self.sons = []
        self.factory = factory

    def addSon(self, son):
        self.sons.append(son)

    def removeSon(self, son):
        self.sons.remove(son)
    
class Bag(Composite):
    def __init__(self, pos, factory, character, image):
        super(Bag, self).__init__(pos, factory)
        self.character = character
        self.image = image
        self.addSon(self.factory.makeMedalBox(self))
        self.addSon(self.factory.makeKey())

    def addRedMedal(self):
        for son in self.sons:
            son.addRedMedal()
    
    def addBlueMedal(self):
        for son in self.sons:
            son.addBlueMedal()

    def addGoldMedal(self):
        for son in self.sons:
            son.addGoldMedal()

    def useKey(self):
        for son in self.sons:
            if son.useKey():
                return True
        return False

    def hasKey(self):
        for son in self.sons:
            if son.hasKey():
                return True
        return False

    def addKey(self):
        for son in self.sons:
            son.obtainKey()

    def notifyCharacter(self):
        self.character.changePoweringUp()

    def paintMedalImages(self, game):
        for son in self.sons:
            son.paintMedalImages(game)

        
class MedalBox(Composite):
    def __init__(self, pos, factory, bag, image):
        super(MedalBox, self).__init__(pos, factory)
        self.bag = bag
        self.image = image
        self.addSon(self.factory.makeRedMedal())
        self.addSon(self.factory.makeBlueMedal())
        self.addSon(self.factory.makeGoldMedal())
        self.counterMedals = 0

    def addRedMedal(self):
        for son in self.sons:
            if son.obtainRedMedal():
                self.checkMedals()
    
    def addBlueMedal(self):
        for son in self.sons:
            if son.obtainBlueMedal():
                self.checkMedals()

    def addGoldMedal(self):
        for son in self.sons:
            if son.obtainGoldMedal():
                self.checkMedals()

    def checkMedals(self):
        self.counterMedals += 1
        print 'checking medals -> ', self.counterMedals
        if self.counterMedals == 3:
            self.bag.notifyCharacter()

    def paintMedalImages(self, game):
        for son in self.sons:
            son.paintMedalImages(game)

class Medal(Item):
    def obtainRedMedal(self):
        pass
    def obtainBlueMedal(self):
        pass
    def obtainGoldMedal(self):
        pass

class BlueMedal(Medal):
    def obtainBlueMedal(self):
        self.img = self.dic_img['obtained']
        self.obtained = True
        return True

    def paintMedalImages(self, game):
        if self.obtained:
            game.paintBlueMedal()

class RedMedal(Medal):
    def obtainRedMedal(self):
        self.img = self.dic_img['obtained']
        self.obtained = True
        return True

    def paintMedalImages(self, game):
        if self.obtained:
            game.paintRedMedal()

class GoldMedal(Medal):
    def obtainGoldMedal(self):
        self.img = self.dic_img['obtained']
        self.obtained = True
        return True

    def paintMedalImages(self, game):
        if self.obtained:
            game.paintGoldMedal()
        