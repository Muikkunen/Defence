class Square(object):

	EMPTY = 0
	ROUTE = 1
	TOWER = 2

	def __init__ (self):
		self._type = Square.EMPTY

	def set_empty(self):
		# Marks square as empty. This method is used for emptying the board and therefore does not care whether
		# 	square is marked as route or tower
		self._type = Square.EMPTY

	def set_route(self):
		# Marks square as route, if possible. Returns boolean value stating whether succesful or not
		if self._type == 0:
			self._type = Square.ROUTE
			return True
		else:
			return False

	def set_tower(self):
		# Marks square as tower, if possible. Returns boolean value stating whether succesfull or not
		if self._type == Square.EMPTY:
			self._type = Square.TOWER
			return True
		else:
			return False

	def contains(self):
		# Returns Square's type (EMPTY = 0, ROUTE = 1 or TOWER = 2) 
		return self._type