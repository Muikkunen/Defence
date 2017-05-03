from io import StringIO

from loader_function import EOFReached, get_current_information

class CorruptedHighScoresData(Exception):
	def __init__ (self, message):
		super(CorruptedGameData, self).__init__(message)

class LoadHighScores(object):

	def load_scores(self, file, error_text):
		stage = []
		for i in range(10):
			current_information = get_current_information(file)

			# If next information block has been found, check that all 10 scores have been saved before proceeding
			if current_information[0][0] == "#":
				if i != 9:
					raise CorruptedHighScoresData("High Scores file does not have 10 saved scores on "+ +" difficulty")

			placing_information = [current_information[0], current_information[1], current_information[2]]
			stage.append(placing_information)
		return stage



	def load(self, input):
		high_scores = {}
		
		try:
			file = open(input, "r")

			while True:
				current_information = get_current_information(file)

				# Find certain information block
				if current_information[0] == "#Easy":
					high_scores["Easy"] = self.load_scores(file, "easy")

				elif current_information[0] == "#Medium":
					high_scores["Medium"] = self.load_scores(file, "medium")

				elif current_information[0] == "#Hard":
					high_scores["Hard"] = self.load_scores(file, "hard")



		except OSError:
			raise CorruptedHighScoresData("File missing or corrupted")

		except EOFReached:
			return high_scores