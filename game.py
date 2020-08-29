from player import player as p
from world import get_player_location
from tiles import tiles

while True:
    # Get player location
    p_loc = get_player_location(p, tiles)
    print(p_loc)

    # Ask for user input
    u_in = input("What would you like to do?\n")

    # Check if that input is legal
    #parse_input(u_in)
    if u_in.lower() == 'stop':
        break

