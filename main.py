#from enemy import Enemy
#from tower import Tower
from setup import Setup


def main():
	file_name = "Game_data_1.0.txt"

	game = Setup().load_all(file_name)

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
	game.get_board().get_enemies().append(game.get_board().waves[0][1])

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