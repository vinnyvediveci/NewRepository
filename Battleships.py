class BattleShipGame:
    battleField = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def add(self, ship, x1, y1):
        assert isinstance(ship, Ship)
        BattleShipGame.battleField[x1][y1] = 6

        #if x1 == x2:
          #y1 = BattleShipGame.battleField[y1]
          #y2 = BattleShipGame.battleField[y2]
          #for x in range(y1, y2):
            # x = 1
       # elif y1 == y2:
          #x1 = BattleShipGame.battleField[x1]
          #x2 = BattleShipGame.battleField[x2]
          #for y in range(x1, x2):
            # y = 1









class Player:
    def __init__(self, name):
        self.name = name


class Ship(BattleShipGame):
    def __init__(self, size):

        self.size = size


class Battleship(Ship):
    def __init__(self):
        Ship.__init__(self, 3)

class PatrolBoat(Ship):
    def __init__(self):
        Ship.__init__(self, 2)

class Submarine(Ship):
    def __init__(self):
        Ship.__init__(self, 3)

class Destroyer(Ship):
    def __init__(self):
        Ship.__init__(self, 4)

class Carrier(Ship):
    def __init__(self):
        Ship.__init__(self,  5)

battleShipGame = BattleShipGame()
battleShipGame.add(Battleship(), 0, 2)

#

#BattleShipGame.add(Battleship(), 0, 1, 0, 5)
print(BattleShipGame.battleField)