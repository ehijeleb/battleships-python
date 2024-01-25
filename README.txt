BATTLESHIPS

Welcome to my rendition of Battleships, a traditional board game. You will be able to interact with an AI or play 
by yourself. 


Packages/Libraries 
	-flask

Features
	-Multiplayer Battleships Game with GUI or CLI option
	-Singleplayer Battleships Game with CLI option
	

Main Game
	-To run the program, find your way to main.py, and open the domain that your IDE outputs
	-Before going through with the game, add /placement to the end of the domain
	-You can now place ships and continue with the game

Other Functionality 
	-Run mp_game_engine.py for the command line version
	-Run game_engine.py for the single player command line version

File Structure
	-The initial placement.json will have items within it, ignore this as your placement will replace it
	once you run the program, this file is used for the custom battleship placement
	-placement.json format : {ShipName: [startX_Coordinate, startY_Coordinate, orientation]}
	-You can add/remove ships within battleships.txt
	-battleships.txt is in the formate "shipname, shipsize"

License
	-This project is licensed under the MIT License

	