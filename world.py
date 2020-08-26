from player import Player
from tiles import tiles

def get_player_location(player, tiles):
    for tile in tiles:
        if player.location == tile.location:
            return tile