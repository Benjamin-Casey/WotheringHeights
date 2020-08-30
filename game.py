from player import player as p
from world import get_player_location
from tiles import tiles
from actions import action_list, get_actions

while True:
    # Get player location
    p_loc = get_player_location(p, tiles)
    print(p_loc)

    # Get available actions and print them to the player
    actions = get_actions(p, tiles, p_loc)
    for action in actions:
        print(action)

    # Ask for user input
    u_in = input("What would you like to do?\n")

    if u_in.lower() == 'stop':
        break


