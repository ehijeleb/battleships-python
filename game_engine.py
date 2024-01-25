from components import initialise_board, create_battleships, place_battleships
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def attack(coordinates, board, battleships):

    row, col = coordinates
    #converts coordinates tuple into two varialbles which can be used later

    if not (0 <= row < len(board) and 0 <= col < len(board[0])):
        logging.warning("Attack coordinates out of bounds")
        return False  # Return false for out of bounds
    
    if board[row][col] is not None:
        #Check if therer is a ship at the coordinate
        ship_model = board[row][col]

        board[row][col] = None
        #update the board to None

        battleships[ship_model] -= 1
        #decrease size of the battleship

        if battleships[ship_model] == 0:
            print("SUNK ", ship_model, " !")
            logging.info(f"Sunk {ship_model}")
        logging.info(f"User attack at {coordinates} was a hit")
        return True # return true for hit

    else:
        logging.info(f"User attack at {coordinates} was a miss")
        return False # return false for miss
    


def cli_coordinates_input():

    while True:

        user_input = input("Enter coordinates for attack: ")

        try:
            x, y = map(int, user_input.split(','))
            return x,y       
        except ValueError:
            print("Invalid input, please try again")
            logging.warning("Invalid input, please try again")
            
def simple_game_loop():
    print("𝑊𝑒𝑙𝑐𝑜𝑚𝑒 𝑡𝑜 𝐵𝑎𝑡𝑡𝑙𝑒𝑠ℎ𝑖𝑝𝑠")
    logging.info("Game started")
    #1. Welcome Message

    board = initialise_board()
    battleships = create_battleships()
    place_battleships(board, battleships, algorithm = "random")
    logging.info(f"Placed battleships using random algorithm")

    #2. Initialise the board,the ships and place the ships

    while any(size > 0 for size in battleships.values()):
        #5.repeat util all battleships are sunken
        attack_coords = cli_coordinates_input()
        #3. prompt ser to input coords of their attack
        hit = attack(attack_coords, board, battleships)
        #4. Process attack

        if hit:
            print("HIT!")
            logging.info(f"User attack at {attack_coords} was a hit")
        else:
            print("MISS!")
            logging.info(f"User attack at {attack_coords} was a miss")
        #4. Print hit or miss message
        # 
        #     
    print("𝐴𝑙𝑙 𝑠ℎ𝑖𝑝𝑠 ℎ𝑎𝑣𝑒 𝑏𝑒𝑒𝑛 𝑠𝑢𝑛𝑘, 𝐺𝑎𝑚𝑒 𝑂𝑣𝑒𝑟 !")
    logging.info("Game over, all ships have been sunk")
    #6. print game over message

if __name__ == "__main__":
    simple_game_loop()