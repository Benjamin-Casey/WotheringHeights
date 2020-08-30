from player import player as p

class Action:
    def __init__(self, name, function, description):
        self.name = name
        self.function = function
        self.description = description

    def __str__(self):
        return """{}\n=============\n{}\n""".format(self.name, self.description) 


action_list = []

move_north = Action('Move North', p.move_north, 'Move the player North')
move_south = Action('Move South', p.move_south, 'Move the player South')
move_east = Action('Move East', p.move_east, 'Move the player East')
move_west = Action('Move West', p.move_west, 'Move the player West')


def get_available_movement(player, tiles, player_location):
    for adjacent_tile in player_location.get_adjacent_tiles(tiles):
        if adjacent_tile[0] == 'north':
            action_list.append(move_north)
        elif adjacent_tile[0] == 'south':
            action_list.append(move_south)
        elif adjacent_tile[0] == 'east':
            action_list.append(move_east)
        elif adjacent_tile[0] =='west':
            action_list.append(move_west)


def get_actions(player, tiles, player_location):
    get_available_movement(player, tiles, player_location)
    return action_list
    
