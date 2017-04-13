#from enemy import Enemy
#from tower import Tower
from setup import Setup
from gui import GUI


def main():
	# File names, which specify where the game information and high scores are stored
	game_data = "Game_data_1.0.txt"
	high_scores_data = "Highscores.txt"

	game = Setup().load_all(game_data)			# Load game information from text file
	#high_scores = Load_high_scores(high_scores_data)			# Load high scores from text file
	gui = GUI()								# Initialize GUI

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

	for j in range(game.board.get_height()):
		print("")
		for i in range(game.board.get_width()):
			if game.board.squares[i][j].contains() == 0:
				print(".", end="")
			elif game.board.squares[i][j].contains() == 1:
				print(" ", end="")
	
	game.get_board().get_enemies().append(game.get_board().waves[0][0])
	#game.get_board().get_enemies().append(game.get_board().waves[0][1])

	game.get_board().get_enemies()[0].set_location(list(game.get_board().get_route_points()[0]))

	while 0 < game.get_lives():
		list_of_enemies_to_be_killed = []
		if game.get_board().get_enemies() == []:
			break
		for enemy in game.get_board().get_enemies():
			print(enemy.location)
			if enemy.move(enemy.get_speed()):
				list_of_enemies_to_be_killed.append(enemy)
			print("Player's lives: {}".format(game.get_lives()))

		for enemy in list_of_enemies_to_be_killed:
			game.get_board().kill_enemy(enemy)


	print(game.get_board().get_enemies())

	
	


main()