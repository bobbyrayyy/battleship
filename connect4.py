# Created by Bob Lin

# connect 4 game with infinite edges
DEFAULT_SIZE = 6
grid = [[]]


def create_grid(size):
    global grid

    grid = [[0 for _ in range(size)] for _ in range(size)]

#def expand_grid(expand_by, direction):

def show_grid():
    for i in range(DEFAULT_SIZE-1, -1, -1):
        print("\n")
        print(grid[i])


def place_chip(player, column):
    # return -1 means fail to place chip, 0 means placed but no win, 1 means placed and win
    global grid

    if player == 'RED':
        player  = 'R'
    else:
        player = 'B'

    if grid[DEFAULT_SIZE-1][column] == 0:
        for i in range(DEFAULT_SIZE):
            if grid[i][column] == 0:
                if player == 'R':
                    grid[i][column] = 'R'
                else:
                    grid[i][column] = 'B'
                
                row = i
                break

    else:
        print("Column full! Try again.")

    # check if win
    count = 0
    # check vertical
    if row >= 3:
        for i in range(row-1, -1, -1):
            if grid[i][column] == player:
                count += 1
            else:
                return 0
            if count == 3:
                return 1

    # check horizontal
    if column <= DEFAULT_SIZE-4:
        if grid[row][column+1] == player and grid[row][column+2] == player and grid[row][column+3] == player:
            return 1
    if column <= DEFAULT_SIZE-3 and column >= 1:
        if grid[row][column-1] == player and grid[row][column+1] == player and grid[row][column+2] == player:
            return 1
    if column <= DEFAULT_SIZE-2 and column >= 2:
        if grid[row][column-2] == player and grid[row][column-1] == player and grid[row][column+1] == player:
            return 1
    if column <= DEFAULT_SIZE-1 and column >= 3:
        if grid[row][column-3] == player and grid[row][column-2] == player and grid[row][column-1] == player:
            return 1

    # check diagonal
    if column <= DEFAULT_SIZE-4 and row <= DEFAULT_SIZE-4:
        if grid[row+1][column+1] == player and grid[row+2][column+2] == player and grid[row+3][column+3] == player:
            return 1
    if column <= DEFAULT_SIZE-4 and row >= 3:
        if grid[row-1][column+1] == player and grid[row-2][column+2] == player and grid[row-3][column+3] == player:
            return 1

    if column <= DEFAULT_SIZE-3 and row <= DEFAULT_SIZE-3 and column >= 1 and row >= 1:
        if grid[row-1][column-1] == player and grid[row+1][column+1] == player and grid[row+2][column+2] == player:
            return 1
    if column <= DEFAULT_SIZE-3 and row >= 2 and column >= 1 and row <= DEFAULT_SIZE-3:
        if grid[row+1][column-1] == player and grid[row-1][column+1] == player and grid[row-2][column+2] == player:
            return 1

    if column <= DEFAULT_SIZE-2 and row <= DEFAULT_SIZE-2 and column >= 2 and row >= 2:
        if grid[row-2][column-2] == player and grid[row-1][column-1] == player and grid[row+1][column+1] == player:
            return 1
    if column <= DEFAULT_SIZE-2 and row >= 1 and column >= 2 and row <= DEFAULT_SIZE-2:
        if grid[row+2][column-2] == player and grid[row+1][column-1] == player and grid[row-1][column+1] == player:
            return 1

    if column <= DEFAULT_SIZE-1 and row <= DEFAULT_SIZE-1 and column >= 3 and row >= 3:
        if grid[row-3][column-3] == player and grid[row-2][column-2] == player and grid[row-1][column-1] == player:
            return 1
    if column <= DEFAULT_SIZE-1 and row >= 3 and column >= 3 and row <= DEFAULT_SIZE-1:
        if grid[row+3][column-3] == player and grid[row+2][column-2] == player and grid[row+1][column-1] == player:
            return 1
    
    return 0



def main():


    print("----------------------------------------------------------------------------------------------")
    print("                         Welcome to Bob's Infinite Connect 4 Game!                            ")
    print("----------------------------------------------------------------------------------------------")
    print("")
    create_grid(DEFAULT_SIZE)
    turn = 'RED'

    while 1:
        show_grid()
        print("It is now " + turn + "'s turn.")
        print("Please enter column number to place chip:")
        user_input = int(input())

        if user_input < 0 or user_input >= DEFAULT_SIZE:
            print("Column out of range! Try again...")
            continue

        res = place_chip(turn, user_input)
        if res == 1:
            print("Congratulations! " + turn + " player won!")
            show_grid()
            break
        else:
            if turn == 'RED':
                turn = 'BLUE'
            else:
                turn = 'RED'

if __name__ == "__main__":
    main()