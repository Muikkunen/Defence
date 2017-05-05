import sys

from missile import Missile
from enemy import Enemy
#from tower import Tower
from setup import Setup
from load_high_scores import LoadHighScores
from gui import GUI

from PyQt5.QtWidgets import QApplication


def main():
	# File names, which specify where the game information and high scores are stored
	game_data = "Game_data.txt"
	high_scores_data = "High_scores.txt"

	game = Setup().load_all(game_data)							# Load game information from text file
	high_scores = LoadHighScores().load(high_scores_data)		# Load information for high scores from text file

	#game.get_board().set_route_points(game.routes[1][1])
	#game.get_board().add_route()

	# Every Qt application must have one instance of QApplication
	global app # This prevents crash on exit
	app = QApplication(sys.argv)
	gui = GUI(game, high_scores, high_scores_data)

	# Make interaction with the gui possible and start the actual Qt event loop
	sys.exit(app.exec_())

main()