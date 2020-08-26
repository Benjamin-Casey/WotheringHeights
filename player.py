# Player file

class Player:
    def __init__(self):
        self.hp = 100
        self.location = [0, 0]  # [X, Y]

    def isAlive(self):
        return self.hp > 0

    def moveNorth(self):
        self.location = self.location[1] += 1
    def moveSouth(self):
        self.location = self.location[1] -= 1
    def moveEast(self):
        self.location = self.location[0] += 1
    def moveWest(self):
        self.location = self.location[0] -= 1
