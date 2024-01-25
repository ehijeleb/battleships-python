import random
from components import initialise_board, create_battleships, place_battleships
from game_engine import attack, cli_coordinates_input
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


players = {}

def display_board(board):
    for row in board:
        print(" ".join(cell if cell is not None else '-' for cell in row))
    print()

def generate_attack(size = 10):
    #generate random coords for attack within the board size
    coord = random.randint(0, size -1), random.randint(0, size-1)
    logging.info("AI generated attack at {}".format(coord))
    return coord
    


def ai_opponent_game_loop():
    logging.info("𝑊𝑒𝑙𝑐𝑜𝑚𝑒 𝑡𝑜 𝐵𝑎𝑡𝑡𝑙𝑒𝑠ℎ𝑖𝑝𝑠")


    # #Initialise user controlled player
    username_user = "user"
    players[username_user] = {
        "board": initialise_board(),
        "battleships": create_battleships()
    }

    player_data_user = players[username_user]
    place_battleships(player_data_user["board"], player_data_user["battleships"], algorithm = "custom")
    logging.info(f"Placed user battleships using custom algorithm")

    #Initialise Ai opponent

    username_ai = "ai"
    players[username_ai] = {
        "board": initialise_board(),
        "battleships": create_battleships()
    }
    player_data_ai = players[username_ai]
    place_battleships(player_data_ai["board"], player_data_ai["battleships"], algorithm = "random")
    logging.info(f"Placed AI battleships using random algorithm")  


    #Game loop

    while any(size > 0 for size in player_data_user["battleships"].values()) and any(size > 0 for size in player_data_ai["battleships"].values()):
        logging.info("Starting a new round")
        #repeat util all battleships are sunken

        #user attack
        print(f"{username_user}'s turn")
        display_board(player_data_user["board"])
        user_coords = cli_coordinates_input()
        hit_user = attack(user_coords, player_data_ai["board"], player_data_ai["battleships"])
        if hit_user:
            print("HIT!")
            logging.info(f"User attack at {user_coords} was a hit")  
        else:
            print("MISS!")
            logging.info(f"User attack at {user_coords} was a miss")

        #ai attack
        print(f"{username_ai}'s turn")
        ai_coords = generate_attack()
        hit_ai = attack(ai_coords, player_data_user["board"], player_data_user["battleships"])
        if hit_ai:
            print("HIT!")
            logging.info(f"AI attack at {ai_coords} was a hit")
        else:
            print("MISS!")
            logging.info(f"AI attack at {ai_coords} was a miss")
        
    if all(size == 0 for size in player_data_user["battleships"].values()):
        print(f"{username_ai} WINS!")
        logging.info(f"{username_ai} WINS!")
    else:
        print(f"{username_user} WINS!")
        logging.info(f"{username_user} WINS!")

if __name__ == "__main__":
    ai_opponent_game_loop()