from io import StringIO

from game import Game
from board import Board
from enemy import Enemy
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
			current_line = self.get_current_information(file)

			# Return if the first character of the line is '-' thus meaning that all waves have been read
			if current_line[0][0] == "-":
				return

			# In case information block's highlighting is missing, examine if next block has been reached
			current_line_last_position = file.tell()
			current_line = self.get_current_information(file)

			if current_line[0] == "#":
				# Move back to earlier line if new information block has been reached because
				# 	'load_all()' expects that this point has not been reached
				file.seek(current_line_last_position)
				return

			# Add certain wave to the Game
			game.add_wave(current_line[0], int(current_line[1]))


	def load_missile(self, file, game):
		missile_type, speed = (None,) * 2

		while True:
			current_line = self.get_current_information(file)	

			if current_line[0] == "Type":
				missile_type = current_line[1]
			elif current_line[0] == "Speed":
				speed = int(current_line[1])

			if None not in (missile_type, speed):
				missile = Missile(missile_type, speed)
				game.add_missile_type(missile_type, missile)
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

			if None not in (enemy_type, name, hitpoints, armour, speed, worth):
				enemy = Enemy(enemy_type, name, hitpoints, armour, speed, worth)
				game.add_enemy_type(enemy_type, enemy)	
				return


	def load_route(self, file, game):
		while True:
			current_line = self.get_current_information(file)

			# When name has been read, the function expects that the route has also been read
			if current_line[0] == "Name":
				game.add_route_name(current_line[1])

				# According to the position points, add the whole route to the board
				game.get_board().add_route()
				return

			if current_line[0][0] == "#":
				raise CorruptedGameData("Route's name is missing")

			# Convert information from list to tuple and strings inside the list to integers
			position = tuple(map(int, current_line))

			game.get_board().add_destination(position)


	def load_board(self, file):
		# Set up variables for board measurements
		width, height = None, None

		while True:
			current_line = self.get_current_information(file)

			# Set board measurements to the variables
			if current_line[0] == "Width":
				width = int(current_line[1])
			elif current_line[0] == "Height":
				height = int(current_line[1])

			# Examine whether width and height have been found
			if width != None and height != None:
				return Board(width, height)


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

				elif current_information[0] == "#Missile":
					self.load_missile(file, game)

				elif current_information[0] == "#Waves":
					self.load_waves(file, game)


		except OSError:
			raise CorruptedGameData("File missing or corrupted")

		except EOFReached:
			return game