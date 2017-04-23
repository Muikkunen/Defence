import sys

from missile import Missile
from enemy import Enemy
#from tower import Tower
from setup import Setup
from gui import GUI

from PyQt5.QtWidgets import QApplication


def main():
	# File names, which specify where the game information and high scores are stored
	game_data = "Game_data_1.0.txt"
	high_scores_data = "High_scores.txt"

	game = Setup().load_all(game_data)			# Load game information from text file
	#high_scores = Load_high_scores(high_scores_data)			# Load high scores from text file
	#gui = GUI()								# Initialize GUI

	"""
	# Loop that allows player to navigate between main menu, highscores and playing
	while True:
		if main_menu():							# If Main menu returns true, move on to choose difficulty
			route = select_route(gui)			# Call for select_route() to select the difficulty
			score = play(gui, game, route)		# Start playing on selected difficulty. Function returns players points and reached level as list
			add_new_high_score(high_scores_data, route, score)	# Add new high score to certain level if it is greater than the lowest on certain level
		else:
			high_scores(gui, high_scores)		# View the high scores of all levels
	"""


	#game.board.current_wave(game.board.waves[0])

	game.get_board().set_route_points(game.routes[1][1])
	game.get_board().add_route()

	"""for j in range(game.board.get_height()):
		print("")
		for i in range(game.board.get_width()):
			if game.board.squares[i][j].contains() == 0:
				print(".", end="")
			elif game.board.squares[i][j].contains() == 1:
				print(" ", end="")"""
	

	#location = [50, 60]
	#print(game.get_enemy_types()["KILLER1"])
	#print(list(game.get_board().get_route_points()[0]))

	"""game.get_board().add_enemy(game.get_enemy_types()["KILLER1"],\
		[game.get_board().get_route_points()[0][0] * game.get_board().get_square_size(), game.get_board().get_route_points()[0][1]\
		* game.get_board().get_square_size()])"""

	#print(game.get_board().get_enemies()[0].get_location())

	#game.get_board().get_enemies().append(game.get_board().waves[0][1])

	#game.get_board().get_enemies()[0].set_location(list(game.get_board().get_route_points()[0]))

	"""while 0 < game.get_lives():
		list_of_enemies_to_be_killed = []
		if game.get_board().get_enemies() == []:
			break
		for enemy in game.get_board().get_enemies():
			print(enemy.location)
			if enemy.move(enemy.get_speed()):
				list_of_enemies_to_be_killed.append(enemy)
			print("Player's lives: {}".format(game.get_lives()))

		for enemy in list_of_enemies_to_be_killed:
			game.get_board().kill_enemy(enemy)"""


	#print(game.get_board().get_enemies())

	#global app # Prevent crash on exit
	#app = QApplication(sys.argv)

	#print(game.get_tower_types())

	cannon = game.get_tower_types()["Cannon"]
	#enemy = game.get_enemy_types()["KILLER1"]

	position = [10, 10]
	game.get_board().add_tower(cannon, position)

	
	#print(game.get_board().get_towers()[0].get_location())
	#print("Enemy[0] location: {}".format(game.get_board().get_enemies()[0].get_location()))
	#game.get_board().get_towers()[0].shoot()


	board = game.get_board()

	#print(game.get_enemy_types()["KILLER2"])

	board.add_enemy(Enemy(game.get_enemy_types()["KILLER1"]), list(game.get_board().get_route_points()[0]))
	board.add_enemy(Enemy(game.get_enemy_types()["KILLER2"]), list(game.get_board().get_route_points()[0]))

	game.get_board().get_towers()[0].shoot()

	#print("Missiles: {}".format(game.get_board().get_missiles()))

	"""
	for enemy in board.get_enemies():
		print("Enemy location: ", end="")
		print(enemy.get_location())
		print(enemy.get_speed())"""

	#sys.exit(app.exec_())

	# Every Qt application must have one instance of QApplication.--------------------------------------------REMOVE
	global app # Prevent crash on exit
	app = QApplication(sys.argv)
	gui = GUI(game)

	# Start the Qt event loop. (i.e. make it possible to interact with the gui)--------------------------------------------REMOVE
	sys.exit(app.exec_())


	"""
	for tower_type in game.get_tower_types():
		tower = game.get_tower_types()[tower_type]
		tower.shoot(game.get_board().get_enemies[0])
		print(game.tower_types[tower].get_damage())
		print(game.tower_types[tower].get_shoot_range())"""


	#missile = Missile("Cannon", 50)
	#missile.Initialize(game.get_tower_types()[CANNON], game.get_enemy_types()[KILLER1])


main()