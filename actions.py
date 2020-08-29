action_list = []

#Note: May need to create an Anction class later for all these
def get_available_movement(player, tiles, player_location):
    #Todo: add the move_* functions.
    for adjacent_tile in player_location.get_adjacent_tiles:
        if adjacent_tile[0] == 'north':
            action_list.append(move_north)
        elif adjacent_tile[0] == 'south':
            action_list.append(move_south)
        elif adjacent_tile[0] == 'east':
            action_list.append(move_east)
        elif adjacent_tile[0] =='west':
            action_list.append(move_west)