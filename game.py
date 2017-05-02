from board import Board
from enemy import Enemy

class Game():

	def __init__ (self):
		self.money = 0					# Integer to store the information of the player's money
		self.points = 0					# Integer to store the information of the player's points
		self.lives = 0					# Integer to store the information of the player's lives
		self.time_between_waves = 0		# Integer to store the information of the time between waves
		self.enemy_spawn_interval = 0
		self.fps = 0					# Integer to store the frames per second value
		self.routes = []				# Container for different routes (E.g. Easy, Medium, Hard)

		self.enemy_types = {}			# Dictionary for different enemies
		self.tower_types = {}			# Dictionary for different towers
		self.missile_types = {}			# Dictionary for different missiles

	def setup(self, game_information):
		self.money = game_information[0]
		self.lives = game_information[1]
		self.time_between_waves = game_information[2]
		self.enemy_spawn_interval = game_information[3]
		self.fps = game_information[4]

	# Game's getters
	def get_money(self):
		return self.money

	def get_points(self):
		return self.points

	def get_lives(self):
		return self.lives

	def get_time_between_waves(self):
		return self.time_between_waves

	def get_enemy_spawn_interval(self):
		return self.enemy_spawn_interval

	def get_fps(self):
		return self.fps

	def get_board(self):
		return self.board

	def get_enemy_types(self):
		return self.enemy_types

	def get_tower_types(self):
		return self.tower_types

	def get_missile_types(self):
		return self.missile_types

	def get_route_points(self):
		return self.route_points


	def check_dead_enemies(self):
		for enemy in self.board.get_enemies():

			# Check if enemy's hitpoints are less than or equal to 0
			if enemy.get_hitpoins() <= 0:

				# Increase player's money according to the enemy's worth
				self.points += enemy.get_worth()

				# Remove enemy from board
				self.board.get_enemies().remove(enemy)



	# Adds enemy's type and the enemy itself to the enemy_types dictionary
	def add_enemy_type(self, type_name, enemy):
		self.enemy_types[type_name] = enemy

	# As add_enemy_type(), adds tower's type and the tower itself to the tower_types dictionary
	def add_tower_type(self, type_name, tower):
		self.tower_types[type_name] = tower

	# As add_tower_type(), adds missiles type and the missile itself to the missile_types dictionary
	def add_missile_type(self, type_name, missile):
		self.missile_types[type_name] = missile


	def add_route(self, route_name, route_points):
		new_route = [route_name, route_points]
		#new_route = [None] * 2
		#new_route[0] = route_name
		#new_route[1] = route_points

		self.routes.append(new_route)


	def lose_life(self):
		self.lives -= 1
		if self.lives <= 0:
			print("Game over")


	def increase_money(self, money):		# When enemy is killed, increase player's money
		self.money += money

	def increase_points(self, points):		# When enemy is killed, increase player's points
		self.points += points


	"""def set_money(self, money):
		self.money = money

	def set_lives(self, lives):
		self.lives = lives

	def set_time_between_waves(self, time):
		self.time_between_waves = time

	def set_enemy_spawn_interval(self, time):
		self.enemy_spawn_interval = time

	def set_fps(self, fps):
		self.fps = fps"""

	def set_board(self, board):
		self.board = board


	def next_wave(self):
		enemies_to_be_added = []
		try:
			current_wave = self.get_board().get_current_wave() - 1		# Get the current wave; minus 1, because lists in python start from 0
			waves = self.get_board().get_waves()
			for amount in range(waves[current_wave][1]):
				enemy_name = waves[current_wave][0]
				enemy = Enemy(self.enemy_types[enemy_name])	# Select the enemy's type from game's dictionary
				enemies_to_be_added.append(enemy)
		except IndexError:
			print("Trying to find too many enemies from a wave")
	
		self.get_board().advance_to_next_wave()
		#self.adding_enemies = False								# Indicate that new enemies are not currently being added
		return enemies_to_be_added