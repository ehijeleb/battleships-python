# main.py 
import json

from flask import Flask, render_template, request, jsonify
from components import initialise_board, create_battleships, place_battleships
from game_engine import attack
from mp_game_engine import generate_attack

app = Flask(__name__)

def user_board():
    board = initialise_board()
    battleships = create_battleships()
    place_battleships(board, battleships, algorithm = "custom")
    return board

def bot_board():
    board = initialise_board()
    battleships = create_battleships()
    place_battleships(board, battleships, algorithm = "random")
    return board

ai_board = bot_board()
players_board = user_board()

def ai_won():
    #loop through ai board and check if all values are None
    for row in players_board:
        for cell in row:
            if cell != None:
                return False
    else:
        return True
    
def player_won():
    #loop through player board and check if all values are None
    for row in ai_board:
        for cell in row:
            if cell != None:
                return False
    else:
         return True


@app.route("/placement", methods=["GET", "POST"])
def placement_interface():
    if request.method == "GET":
        return render_template("placement.html" , board_size = 10, ships = create_battleships())   
    if request.method == "POST":
        data = request.get_json()
        
        #replace conntents of placement.json with data
        with open("placement.json", "r+") as f:
            json.dump(data, f)
        return jsonify({'message': 'Received'}), 200


@app.route("/", methods=["GET"])
def root():
    if request.method == "GET":
        return render_template("main.html" , player_board = user_board())

@app.route("/attack", methods = ["GET"])
def process_attack():
    x = request.args.get('x')
    y = request.args.get('y')

    coordinates = (int(x), int(y))

    hit = attack(coordinates, ai_board, create_battleships())
    user_won = player_won()
    bot_won = ai_won()

    if hit == True:
        if bot_won == True:
            return jsonify({'hit': True,
            'AI_Turn': generate_attack(),
            'finished': "Game Over AI wins",
            })
        if user_won == True:
            return jsonify({'hit': True,
            'AI_Turn': generate_attack(),
            'finished': "Game Over Player wins",
            })
        else:
            return jsonify({'hit': True,
            'AI_Turn': generate_attack(),
            })
    else:
        return jsonify({'hit': False,
        'AI_Turn': generate_attack(),
        })


if __name__ == "__main__":
    app.run()
