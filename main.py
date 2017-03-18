#from enemy import Enemy
#from tower import Tower
from setup import Setup


def main():
	file_name = "Game_data_1.0.txt"

	Setup().load_game(file_name)
	

main()