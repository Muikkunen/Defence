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
		self.towers = []
		self.enemies = []
		self.missiles = []
		self.route_points = []		# Container for route points
		self.waves = []				# Container for different waves


	def set_route_points(self, route_points):
		self.route_points = route_points


	def get_width(self):
		# Returns the board's width: int
		return len(self.squares)

	def get_height(self):
		# Returns the board's height: int
		return len(self.squares[0])

	def get_enemies(self):
		# Returns the container list of enemies
		return self.enemies

	def get_route_points(self):
		return self.route_points


	def add_wave(self, enemy, amount):
		sub_list_of_enemies = []
		for i in range(amount):
			sub_list_of_enemies.append(enemy)
		self.waves.append(sub_list_of_enemies)

	"""
	def current_wave(self, wave): #---------------------------NOT READY-----------------------------------
		for enemy in range(wave):
			self.enemies.append(enemy)"""


	def add_tower(self, position, tower):
		# Adds tower to the board if the certain square is empty
		if self.squares[position[0]][position[1]].contains() == 0:
			# Add tower to the container list
			self.towers.append(tower)
			# Set Square's type to tower
			self.squares[position[0]][position[1]].set_tower()
		else:
			print("CANNOT ADD")													#----------------------- NOT IMPLEMENTED


	def add_missile_type(self, missile):
		self.missiles.append(missile)


	def add_route(self):
		amount_of_route_points = len(self.route_points)

		# Set first route point to route here because the following loop will not set the first square to route
		#	to prevent setting square that has already been set to square
		self.squares[self.route_points[0][0]][self.route_points[0][1]].set_route()

		# Iterate through route points until second last to prevent checking last value with one that doesn't exist
		for i in range(amount_of_route_points - 1):
			self.squares[self.route_points[i + 1][0]][self.route_points[i + 1][1]].set_route()

			# If consecutive route points have the same x-coordinate set the vertical squares between first and second point to route
			if self.route_points[i][0] == self.route_points[i + 1][0]:

				# Check which route point's y value is greater
				if self.route_points[i][1] < self.route_points[i + 1][1]:
					loop_direction = 1
				else:
					loop_direction = -1

				for j in range(self.route_points[i][1] + loop_direction, self.route_points[i + 1][1], loop_direction):
					if self.squares[self.route_points[i][0]][j].contains() == 0:
						self.squares[self.route_points[i][0]][j].set_route()
					else:
						print("CANNOT ADD")										#----------------------- NOT IMPLEMENTED

			# If consecutive route points have the same y-coordinate set the horizontal squares between first and second point to route
			elif self.route_points[i][1] == self.route_points[i + 1][1]:

				# Check which route point's x value is greater
				if self.route_points[i][0] < self.route_points[i + 1][0]:
					loop_direction = 1
				else:
					loop_direction = -1

				for j in range(self.route_points[i][0] + loop_direction, self.route_points[i + 1][0], loop_direction):
					if self.squares[j][self.route_points[i][1]].contains() == 0:
						self.squares[j][self.route_points[i][1]].set_route()
					else:
						print("CANNOT ADD")										#----------------------- NOT IMPLEMENTED


	def kill_enemy(self, enemy):
		self.enemies.remove(enemy)



	"""def remove_tower(self, tower):
		self.towers.remove(tower)


	def add_enemy(self, enemy):
		self.enemies.append(enemy)


	def add_missile(self, missile):
		self.missiles.append(missile)"""