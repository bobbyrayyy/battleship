# Created by Bob Lin

# need a function to start game (create grid, place ships)
# function to shoot
# function to check if shot hit or not
# function to check if ship that was hit, has been sunked
# main function that calls other functions and iterates through the turns

#START
import random
from sre_constants import GROUPREF_EXISTS
from tracemalloc import start

# global data structures
grid = [[]]
ship_locations = []
possible_length_choices = [2,3,4,4,5]
possible_direction_choices = ['up', 'down', 'left', 'right']

NUM_OF_SHIPS = 5
GRID_SIZE = 10

# create grid and place ships randomly (minimum size is 10x10)
def create_grid(GRID_SIZE):
    global grid
    global ship_locations
    global possible_length_choices
    global possible_direction_choices

    # in grid, 0 means empty, 1 means unhit ship, 2 means hit ship, 3 means fired but missed
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # randomly place 5 ships of lengths 2, 3, 4, 5, 6
    ships_placed_count = 0
    while ships_placed_count < NUM_OF_SHIPS:
        try:
            # randomly choose attributes of a battleship and its position
            start_x = random.randint(0, 9)
            start_y = random.randint(0,9)
            length =random.choice(possible_length_choices)
            #length = possible_length_choices[-1]
            direction = random.choice(possible_direction_choices)
            proposed_coords = []
            #print("")
            #print(start_x, start_y)
            #print(length)
            #print(direction)


            # test if battleship position is valid, if yes then place, else continue and try again
            if direction == 'up' and start_x - length >= -1:    # -1 because the ending coord can be index 0
                proposed_coords = [[x, start_y] for x in range(start_x, start_x - length, -1)]
            
            elif direction == 'down' and start_x + length <= GRID_SIZE:
                proposed_coords = [[x, start_y] for x in range(start_x, start_x + length)]
            
            elif direction == 'left' and start_y - length >= -1:
                proposed_coords = [[start_x, y] for y in range(start_y, start_y - length, -1)]
            
            elif direction == 'right' and start_y - length <= GRID_SIZE:
                proposed_coords = [[start_x, y] for y in range(start_y, start_y + length)]

            else:
                continue

            for coord in proposed_coords:
                # if proposed coord already on the grid, means overlap of ships, which is not allowed. Try again!
                if grid[coord[0]][coord[1]] == 1:
                    continue
            if len(proposed_coords) == 0:
                continue
            
            for coord in proposed_coords:
                confirm_x = coord[0]
                confirm_y = coord[1]
                grid[confirm_x][confirm_y] = 1
            ship_locations.append(proposed_coords)
            
            possible_length_choices.remove(length)
            ships_placed_count += 1
        except:
            continue

def fire(x, y):
    global grid

    return grid[x][y]

def check_if_sunk(shot):
    global grid
    global ship_locations
    location_to_check = None

    for location_of_ship in ship_locations:
        if shot in location_of_ship:
            location_to_check = location_of_ship

    is_sunk = True
    if location_to_check != None:
        for coord in location_to_check:
            if grid[coord[0]][coord[1]] != 2:
                is_sunk = False
    else:
        print("ERROR")

    if is_sunk == True:
        ship_locations.remove(location_to_check)
    return is_sunk


def main():
    global ship_locations


    tries = 0

    create_grid(GRID_SIZE)
    print("----------------------------------------------------------------------------------------------")
    print("                              Welcome to Bob's Battleships!                                   ")
    print("----------------------------------------------------------------------------------------------")
    print("A fleet of enemy battleships have suddenly appeared in a grid of size %2dx%2d" % (GRID_SIZE, GRID_SIZE))
    print("There are a total of %2d ships" % len(ship_locations))
    print("Your goal is to use the minimum number of tries to destroy the fleet")
    print("You can only fire one shot at a time, at a specific coordinate (x, y)")
    print("")

    while True:
        print("----------------------------------------------------------------------------------------------")
        print("Please enter the coordinates of your shot (x, y separated by a comma): ")
        print("")

        user_input = input()
        if user_input == 'help':
            print(ship_locations)
            continue

        try:
            shot = [int(_) for _ in user_input.split(',')]
        except:
            print("Please enter coordinates in the correct format...")
            continue


        if shot[0] < 0 or shot[0] >= GRID_SIZE or shot[1] < 0 or shot[1] >= GRID_SIZE:
            print("ERROR: This shot is outside of the grid of play - please enter a valid coordinate: ")
            continue

        # fire shot on grid
        result = fire(shot[0], shot[1])
        if result == 2:
            print("This coordinate has already been a confirmed hit. Enter another coordinate.")
            continue

        elif result == 3:
            print("You've already fired at this coordinate and hit nothing. Enter another coordinate")

        tries += 1
        if result == 0:
            print("You missed!")

        elif result == 1:
            print("Its a hit!")
            grid[shot[0]][shot[1]] = 2
            if check_if_sunk(shot) == True:
                print('You have sunk an enemy ship!')
                print("Number of enemy ships left: %2d" % len(ship_locations))

        print("Number of tries so far: %2d" % tries)

        if len(ship_locations) == 0:
            print("Congrats! The entire enemy fleet has been eliminated.")
            break

if __name__ == "__main__":
    main()











