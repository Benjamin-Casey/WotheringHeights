# Tiles
class Tile:
    def __init__(self, name, location, description):
        self.name = name
        self.location = location
        self.description = description

    def __str__(self):
        return """{}\nLocation: {}\n""".format(self.description, self.location)