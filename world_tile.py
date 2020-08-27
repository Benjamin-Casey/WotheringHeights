# Tiles
class Tile:
    def __init__(self, name, location, description):
        self.name = name
        self.location = location
        self.description = description

    def __str__(self):
        return """{}\nLocation: {}\n""".format(self.description, self.location)

    def adjacent_tiles(self, tile_list):
        adjacent_tiles = []
        for tile in tile_list:
            if self.location[0] == tile.location[0] and self.location[1] == tile.location[1] + 1\
            or self.location[0] == tile.location[0] and self.location[1] == tile.location[1] - 1\
            or self.location[1] == tile.location[1] and self.location[0] == tile.location[0] + 1\
            or self.location[1] == tile.location[1] and self.location[0] == tile.location[0] - 1:
                adjacent_tiles.append(tile)

        return adjacent_tiles