# Tiles
class Tile:
    def __init__(self, name, location, description):
        self.name = name
        self.location = location
        self.description = description

    def __str__(self):
        return """{}\nLocation: {}\n""".format(self.description, self.location)

    def get_adjacent_tiles(self, tile_list):
        # Stores adjacent tiles and the direction they are in from the current tile.
        adjacent_tiles = []

        # Check each tile to see if it is 1 tile either side of this tile
        for tile in tile_list:
            if self.location[0] == tile.location[0] and self.location[1] == tile.location[1] + 1:
                adjacent_tiles.append(["north", tile])
            elif self.location[0] == tile.location[0] and self.location[1] == tile.location[1] - 1:
                adjacent_tiles.append(["south", tile])
            elif self.location[1] == tile.location[1] and self.location[0] == tile.location[0] + 1:
                adjacent_tiles.append(["east", tile])
            elif self.location[1] == tile.location[1] and self.location[0] == tile.location[0] - 1:
                adjacent_tiles.append(["west", tile])

        return adjacent_tiles