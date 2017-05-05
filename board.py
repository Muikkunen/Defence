from tower import Tower
from enemy import Enemy
#from missile import missile
from square import Square


class Board(object):

	def __init__ (self, width, height, square_size):

		self.squares = [None] * width
		for i in range(self.get_width()):
			self.squares[i] = [None] * height
			for j in range(self.get_height()):
				self.squares[i][j] = Square()

		self.square_size = square_size

		# Containers
		self.enemies = []
		self.towers = []
		self.missiles = []
		self.route_points = []		# Container for route points
		self.waves = []				# Container for different waves

		self.current_wave = 0
		self.adding_enemies = False
		self.difficulty = None

	def initialize(self):
		self.enemies = []
		self.towers = []
		self.missiles = []
		self.route_points = []
		self.current_wave = 0
		self.adding_enemies = False
		self.difficulty = None		


	def get_width(self):
		# Returns the board's width: int
		return len(self.squares)

	def get_height(self):
		# Returns the board's height: int
		return len(self.squares[0])

	def get_squares(self):
		# Returns the board's table of squares
		return self.squares

	def get_square_size(self):
		# Returns the board's square size: int
		return self.square_size

	def get_enemies(self):
		# Returns the container list of enemies
		return self.enemies

	def get_towers(self):
		# Returns the container list of towers
		return self.towers

	def get_missiles(self):
		# Returns the container list of missiles
		return self.missiles

	def get_route_points(self):
		return self.route_points

	def get_waves(self):
		return self.waves

	def get_current_wave(self):
		return self.current_wave

	def get_enemy_start_location(self):
		return self.enemy_start_location

	def amount_of_enemies_on_next_wave(self):
		return len(self.waves[self.current_wave])

	def get_difficulty(self):
		return self.difficulty

	"""def get_waves(self):
		return self.waves"""


	def set_route_points(self, route_points, difficulty):
		self.route_points = route_points
		self.difficulty = difficulty


	def add_wave(self, enemy, amount):
		wave = [enemy, amount]
		self.waves.append(wave)


	def add_tower(self, tower_information, position):

		# Adds tower to the board if the certain square is empty
		try:
			if self.squares[position[0]][position[1]].contains() == 0:

				# Calculate the tower's position so that the tower's location is in the middle of a square
				x_coordinate = position[0] * self.square_size + (self.square_size / 2)
				y_coordinate = position[1] * self.square_size + (self.square_size / 2)

				tower = Tower(tower_information)
				tower.set_location([x_coordinate, y_coordinate])

				# Add tower to the container list
				self.towers.append(tower)
				# Set Square's type to tower
				self.squares[position[0]][position[1]].set_tower()
				return tower
			else:
				print("Cannot add Tower to the Board")

		except IndexError:
			print("Tower cannot be added because the specified Square is outside of the board")


	def add_missile(self, missile):				# Adds missile to the board
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
						print("CANNOT ADD")

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
						print("CANNOT ADD")

		self.enemy_start_location = list(self.route_points[0])		# Define the point where enemies should start




	def kill_enemy(self, enemy):
		self.enemies.remove(enemy)


	def add_enemy(self, enemy, position):
		enemy.set_location(position)
		self.enemies.append(enemy)
		return enemy

	def is_adding_enemies(self):
		return self.adding_enemies

	def set_adding_enemies(self):
		self.adding_enemies = True

	def set_enemies_added(self):
		self.adding_enemies = False

	def advance_to_next_wave(self):
		self.current_wave += 1