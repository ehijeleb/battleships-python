
import random
import json


def initialise_board(size=10):
    board = [[None for i in range(size)] for i in range(size)]
    #create board, with dimensions size x size
    return board


def create_battleships(filename = "battleships.txt"):

    battleships = {}

    with open(filename, 'r') as f:
        for line in f:
            ship, size = line.strip().split(',')
            battleships[ship] = int(size)

    #dictionary containing the battlships : key = name of ship, value = size of ship
    return battleships



def place_battleships(board, ships, algorithm='simple'):
    
    ships = [[key, value] for key, value in ships.items()]
    #convert battleships dictionary to list, where each item in the list is as follows
    #  : [battleship name, sizre]

    def simple_placement(board, ships):

        for x in range(len(ships)):
            size = int(ships[x][1])
            for i in range(int(size)):
                board[x][i] = ships[x][0]
        #places each ship on a new row starting from (0,0), 
        #the size determines how much space the ship takes up

    def random_placement(board, ships):

        for ship in ships:
            size = int(ship[1])
            orientation = random.choice(['horizontal', 'vertical'])
            placed = False

            while not placed:
                if orientation == 'horizontal':
                    start_row = random.randint(0, len(board) - 1)
                    start_col = random.randint(0, len(board[0]) - size)

                    # Check if the positions are empty
                    if all(board[start_row][start_col + i] is None for i in range(size)):
                        # Place the ship
                        for i in range(size):
                            board[start_row][start_col + i] = ship[0]
                        placed = True
                else:
                    start_row = random.randint(0, len(board) - size)
                    start_col = random.randint(0, len(board[0]) - 1)

                    # Check if the positions are empty
                    if all(board[start_row + i][start_col] is None for i in range(size)):
                        # Place the ship
                        for i in range(size):
                            board[start_row + i][start_col] = ship[0]
                        placed = True

    def custom_placement(board, ships):
        with open("placement.json", "r") as config_file:
            placement_config = json.load(config_file)
            #read in placement.json and add it to variable placement_config

        for ship in ships:
            ship_name = ship[0]
            size = int(ship[1])
            if ship_name in placement_config:
                
                start_y, start_x, orientation = placement_config[ship_name]

                start_x = int(start_x)
                start_y = int(start_y)

                if orientation.lower() == 'h':
                    for i in range(size):
                        board[start_x][start_y + i] = ship_name
                elif orientation.lower() == 'v':
                    for i in range(size):
                        board[start_x + i][start_y] = ship_name


    if algorithm == "simple":
        simple_placement(board, ships)
    if algorithm =="random":
        random_placement(board, ships)
    if algorithm =="custom":
        custom_placement(board, ships)
    return board

