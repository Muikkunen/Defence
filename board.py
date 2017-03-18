from tower import Tower
#from enemy import Enemy
#from missile import missile
from square import Square


class Board(object):

	def __init__ (self, width, height):
		#self.enemys = []		# container
		#self.missiles = []		# container

		self.squares = [None] * width
		for i in range(self.get_width()):
			self.squares[i] = [None] * height
			for j in range(self.get_height()):
				self.squares[i][j] = Square()

		self.route_points = []


	def get_width(self):
		# Returns the board's width: int
		return len(self.squares)


	def get_height(self):
		# Returns the board's height: int
		return len(self.squares[0])


	def add_tower(self, tower, place):
		# Adds tower to the board
		if self.squares[placement[0]][placement[1]].is_empty():
			self.squares[placement[0]][placement[1]].set_tower(tower)
		else:
			print("CANNOT ADD")													#----------------------- NOT IMPLEMENTED


	def add_route_point(self):
		self.squares[0][0] = "test"


	"""def remove_tower(self, tower):
		self.towers.remove(tower)


	def add_enemy(self, enemy):
		self.enemys.append(enemy)


	def add_missile(self, missile):
		self.missiles.append(missile)"""