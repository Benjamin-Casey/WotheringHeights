from player import player as p
from world import get_player_location
from tiles import tiles

while True:
    # Get player location
    p_loc = get_player_location(p, tiles)
    # If the game can find a location, print it
    if p_loc in locals():
        print(p_loc)

    # Ask for user input
    u_in = input("What would you like to do?")
    # Do something with the input
    if u_in.lower() == 'stop':
        break