class Square(object):

	def __init__ (self):
		self.route = None
		self.tower = None

	def set_route(self):
		# Marks square as route, if possible. Returns boolean value stating whether succesfull or not
		if self.tower == None:
			self.route == True
			return True
		else:
			return False

	def set_tower(self, tower):
		# Sets tower to the square, if possible. Returns boolean value stating whether succesfull or not
		if self.route == None:
			self.tower == tower
			return True
		else:
			return False

	def is_empty(self):
		# Returns boolean value whether square is empty or not
		if self.tower == None and self.route == None:
			return True
		else:
			return False