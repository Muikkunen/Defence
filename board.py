from tower import Tower
#from enemy import Enemy
#from missile import missile
from square import Square


class Board(object):


	def __init__ (self, width, height):

		self.squares = [None] * width
		for i in range(self.get_width()):
			self.squares[i] = [None] * height
			for j in range(self.get_height()):
				self.squares[i][j] = Square()

		# Containers
		self.enemys = []
		self.missiles = []
		self.route_points = []


	def get_width(self):
		# Returns the board's width: int
		return len(self.squares)


	def get_height(self):
		# Returns the board's height: int
		return len(self.squares[0])


	def add_tower(self, tower, position):
		# Adds tower to the board
		if self.squares[position[0]][position[1]].is_empty():
			self.squares[position[0]][position[1]].set_tower(tower)
		else:
			print("CANNOT ADD")													#----------------------- NOT IMPLEMENTED


	def add_destination(self, position):
		# Adds next destination for enemys to the board
		if self.squares[int(position[0])][int(position[1])].is_empty():
			self.route_points.append(position)

		else:
			print("CANNOT ADD")													#----------------------- NOT IMPLEMENTED


	"""def remove_tower(self, tower):
		self.towers.remove(tower)


	def add_enemy(self, enemy):
		self.enemys.append(enemy)


	def add_missile(self, missile):
		self.missiles.append(missile)"""