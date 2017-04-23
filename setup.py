from io import StringIO

from game import Game
from board import Board
#from enemy import Enemy
from tower import Tower
from missile import Missile


class CorruptedGameData(Exception):
	def __init__ (self, message):
		super(CorruptedGameData, self).__init__(message)

class EOFReached(Exception):
	def __init__ (self, message):
		super(EOFReached, self).__init__(message)

class Setup(object):

	def get_current_information(self, file):

		# Iterate through file until information has been found
		while True:
			current_line = file.readline()

			# If EOF has been reached, use exception to return to the code that called the 'load_game' function
			if current_line == "":
				raise EOFReached("File completely read")

			# Split line to parts using whitespace as text divider
			current_information = current_line.split()

			# Pass empty lines and lines containing only whitespace
			if current_information == []:
				continue

			# Return gathered information
			return current_information


	def load_waves(self, file, game):
		# In order to keep the game data file as simple as possible, this function contains additional
		# 	operation to check whether all waves have been read
		while True:
			current_line_last_position = file.tell()
			current_line = self.get_current_information(file)

			# Return if the first character of the line is '-' thus meaning that all waves have been read
			if current_line[0][0] == "-":
				return

			# In case information block's highlighting is missing, examine if next block has been reached
			#	by examining if the first character is '#'
			next_of_current_line = file.readline()

			# Examine that file has not been completely read
			if next_of_current_line != "":
				if next_of_current_line[0] == "#":
					# Move back to earlier line if new information block has been reached because
					# 	'load_all()' expects that this point has not been reached
					file.seek(current_line_last_position)
					return

			file.seek(current_line_last_position)
			current_line = self.get_current_information(file)

			# Examine that type is defined in game.enemy_types
			if current_line[0] in game.get_enemy_types():
				# Add current wave to the Board
				game.get_board().add_wave(game.get_enemy_types()[current_line[0]], int(current_line[1]))
			else:												#----------------------------------NOT IMPLEMENTED---------------
				print("Enemy not in game types")


	def load_missile(self, file, game):
		missile_type, speed = (None,) * 2

		while True:
			current_line = self.get_current_information(file)	

			if current_line[0] == "Type":
				missile_type = current_line[1]
			elif current_line[0] == "Speed":
				speed = int(current_line[1])

			if None not in (missile_type, speed):
				missile_information = [missile_type, speed]
				game.add_missile_type(missile_type, missile_information)
				return

	def load_tower(self, file, game):
		tower_type, damage, shoot_range, reload_time, build_time, sound_effect = (None,) * 6

		while True:
			current_line = self.get_current_information(file)

			if current_line[0] == "Type":
				tower_type = current_line[1]
			elif current_line[0] == "Damage":
				damage = int(current_line[1])
			elif current_line[0] == "Range":
				shoot_range = int(current_line[1])
			elif current_line[0] == "Reload_time":
				reload_time = int(current_line[1])
			elif current_line[0] == "Build_time":
				build_time = int(current_line[1])
			elif current_line[0] == "Sound_effect":
				sound_effect = current_line[1]


			if None not in (tower_type, damage, shoot_range, reload_time, build_time, sound_effect):
				tower_information = [tower_type, damage, shoot_range, reload_time, build_time, sound_effect, game]
				game.add_tower_type(tower_type, tower_information)
				return

	def load_enemy(self, file, game):
		enemy_type, name, hitpoints, armour, speed, worth = (None,) * 6

		while True:
			current_line = self.get_current_information(file)	

			if current_line[0] == "Type":
				enemy_type = current_line[1]
			elif current_line[0] == "Name":
				name = current_line[1]
			elif current_line[0] == "Hitpoints":
				hitpoints = int(current_line[1])
			elif current_line[0] == "Armour":
				armour = int(current_line[1])
			elif current_line[0] == "Speed":
				speed = int(current_line[1])
			elif current_line[0] == "Worth":
				worth = int(current_line[1])

			if None not in (enemy_type, name, hitpoints, armour, speed, worth, game):
				enemy_information = [enemy_type, name, hitpoints, armour, speed, worth, game]
				game.add_enemy_type(enemy_type, enemy_information)
				return


	def load_route(self, file, game):

		route_points = []		# Empty container for route points

		while True:
			current_line = self.get_current_information(file)

			# When name has been read, the function expects that the route has also been read
			if current_line[0] == "Name":

				# According to the position points, add the whole route to the board
				game.add_route(current_line[1], route_points)
				return

			if current_line[0][0] == "#":
				raise CorruptedGameData("Route's name is missing")

			# Convert information from list to tuple and strings inside the list to integers
			position = tuple(map(int, current_line))

			# Add certain position to the route list's second slot as two-dimensional list
			route_points.append(position)


	def load_board(self, file):
		# Set up variables for board measurements
		width, height, square_size = (None,) * 3

		while True:
			current_line = self.get_current_information(file)

			# Set board measurements to the variables
			if current_line[0] == "Width":
				width = int(current_line[1])
			elif current_line[0] == "Height":
				height = int(current_line[1])
			elif current_line[0] == "Square_size":
				square_size = int(current_line[1])

			# Examine whether width and height have been found
			if None not in (width, height, square_size):
				return Board(width, height, square_size)


	def load_game(self, file, game):
		while True:
			current_line = self.get_current_information(file)

			if current_line[0] == "Money":
				game.set_money(int(current_line[1]))
			elif current_line[0] == "Lives":
				game.set_lives(int(current_line[1]))

			# Examine whether money and lives have been found
			if game.get_money() != 0 and game.get_lives() != 0:
				return game


	def load_all(self, input):

		game = Game()

		try:
			file = open(input, "r")

			while True:
				current_information = self.get_current_information(file)

				# Find certain information block
				if current_information[0] == "#Game":
					game = self.load_game(file, game)

				elif current_information[0] == "#Board":
					game.set_board(self.load_board(file))

				elif current_information[0] == "#Route":
					self.load_route(file, game)

				elif current_information[0] == "#Enemy":
					self.load_enemy(file, game)

				elif current_information[0] == "#Tower":
					self.load_tower(file, game)

				elif current_information[0] == "#Missile":
					self.load_missile(file, game)

				elif current_information[0] == "#Waves":
					self.load_waves(file, game)


		except OSError:
			raise CorruptedGameData("File missing or corrupted")

		except EOFReached:
			return game