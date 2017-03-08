from enemy import *
from tower import *

def main():
	print("asdf")
	vihu1 = Enemy(80, 10, 80, Enemy.steel)
	vihu1.reduce_hitpoints(50)
	print(vihu1.type)

main()