from io import StringIO

class EOFReached(Exception):
	def __init__ (self, message):
		super(EOFReached, self).__init__(message)

def get_current_information(file):

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