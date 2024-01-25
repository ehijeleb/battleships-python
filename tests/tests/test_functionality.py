
from components import initialise_board, place_battleships, create_battleships
import game_engine

def test_initialise_board_return_size():
    """
    Test if the initialise_board function returns a list of the correct size.
    """
    size = 10
    # Run the function
    board = initialise_board(size)
    # Check that the return is a list
    assert isinstance(board, list), "initialise_board function does not return a list"
    # check that the length of the list is the same as board
    assert len(board) == size, "initialise_board function does not return a list of the correct size"
    for row in board:
        # Check that each sub element is a list
        assert isinstance(row, list), "initialise_board function does not return a list of lists"
        # Check that each sub list is the same size as board
        assert len(row) == size, "initialise_board function does not return lists of the correct size"

#test if the board is the correct size, with the correct dimensions
def test_initialise_board():
    board = initialise_board(10)
    assert len(board) == 10 and len(board[0]) == 10, "Board should be 10x10"

#test if the battleships are created correctly from the text file
def test_create_battleships():
    battleships = create_battleships("battleships.txt")
    assert isinstance(battleships, dict), "Battleships should be a dictionary"
    assert "SHIP1" in battleships, "SHIP1 should be in battleships"

#checks if the simple placement algorithm works
def test_place_battleships_simple():
    board = initialise_board()
    battleships = create_battleships("battleships.txt")
    board = place_battleships(board, battleships, algorithm='simple')
    assert board[0][0] == "SHIP1", "SHIP1 should be placed at the start of the board"

#checks if the random placement algorithm works
def test_place_battleships_random():
    board = initialise_board()
    battleships = create_battleships("battleships.txt")
    board = place_battleships(board, battleships, algorithm='random')
    # Verifying if any ship is placed
    assert any(any(row) for row in board), "Ships should be placed on the board"



#ensure that the ships do not overlap
def test_no_ship_overlap():
    board = initialise_board()
    battleships = create_battleships("battleships.txt")
    board = place_battleships(board, battleships, algorithm='random')
    # Check for overlaps
    ship_positions = []
    for row in board:
        for cell in row:
            if cell and cell not in ship_positions:
                ship_positions.append(cell)
    assert len(ship_positions) == len(battleships), "Ships should not overlap"


#verify the attack function works
def test_attack():
    board = initialise_board()
    battleships = create_battleships("battleships.txt")
    board = place_battleships(board, battleships, algorithm='random')
    #check that attack returns true or false
    assert game_engine.attack((0, 0), board, battleships) in [True, False], "Attack should return True or False"


#check how the game handles invalid input
def test_invalid_input():
    board = initialise_board()
    battleships = create_battleships("battleships.txt")
    board = place_battleships(board, battleships, algorithm='random')
    # Check for invalid input
    assert game_engine.attack((100, 100), board, battleships) == False, "Attack should return False for invalid input"


def test_game_end():
    board = initialise_board()
    battleships = create_battleships("battleships.txt")
    board = place_battleships(board, battleships, algorithm='random')

    #attack all the ships
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col]:
                game_engine.attack((row, col), board, battleships)

    assert all(size == 0 for size in battleships.values()), "Game should end when all ships are sunk"

#test if the cli_coordinates_input function works
def test_cli_coordinates_input():
    #mock the input function
    game_engine.input = lambda _: "1,1"
    x, y = game_engine.cli_coordinates_input()
    assert x == 1 and y == 1, "Coordinates should be 1,1"


