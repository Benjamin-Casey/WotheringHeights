class Player:
    def __init__(self):
        self.hp = 100
        self.location = [0, 0]  # [X, Y]

    def isAlive(self):
        return self.hp > 0

    def move_north(self):
        self.location[1] += 1
    def move_south(self):
        self.location[1] -= 1
    def move_east(self):
        self.location[0] -= 1
    def move_west(self):
        self.location[0] -= 1


player = Player()