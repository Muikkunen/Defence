#from enemy import Enemy
#from tower import Tower
from setup import Setup


def main():
	file_name = "Game_data_1.0.txt"

	game = Setup().load_all(file_name)

	
	for j in range(game.board.get_height()):
		print("")
		for i in range(game.board.get_width()):
			if game.board.squares[i][j].contains() == 0:
				print("#", end="")
			elif game.board.squares[i][j].contains() == 1:
				print(" ", end="")

	#game.board.current_wave(game.board.waves[0])

	for i in range(5):
		print(game.board.waves[0][1].name)
	


main()