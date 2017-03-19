from board import Board

class Game():

	def __init__ (self):
		self.money = 0
		self.points = 0
		self.lives = 0
		self.routes = []		# Container for route names


	def lose_life(self):
		lives -= 1


	def set_money(self, money):
		self.money = money


	def set_lives(self, lives):
		self.lives = lives


	def set_board(self, board):
		self.board = board


	def set_waves(self, waves):
		# Set types and amount of enemies on a certain wave
		self.waves = waves


	def add_route_name(self, route_name):
		self.routes.append(route_name)


	def get_money(self):
		return self.money

	def get_points(self):
		return self.points

	def get_lives(self):
		return self.lives

	def get_board(self):
		return self.board


	"""money = property(set_money, get_money)
	points = property(get_points)
	lives = property(get_lives)"""