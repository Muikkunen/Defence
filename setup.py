from io import StringIO
from board import Board

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


	def load_board(self, file):

		# Set up variables for board measurements
		width, height = None, None

		while True:
			current_line = self.get_current_information(file)

			if current_line[0] == "Width":
				width = int(current_line[1])
			elif current_line[0] == "Height":
				height = int(current_line[1])

			# Examine whether width and height has been found
			if width != None and height != None:
				print("toimii")
				return Board(width, height)


	def load_game(self, input):
		try:
			file = open(input, "r")

			while True:
				current_information = self.get_current_information(file)

				# Find certain information block
				if current_information[0] == "#Board":
					board = self.load_board(file)
					board.add_route_point()
					print(board.squares[0][0])


		except OSError:
			raise CorruptedGameData("File missing or corrupted")

		except EOFReached:
			return