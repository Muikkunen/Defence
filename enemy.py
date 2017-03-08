class Enemy():

	wood = 0
	steel = 1


	def __init__(self, hitpoints, armour, speed, type):
		# Pass these for subclass
		self._hitpoints = hitpoints
		self._armour = armour
		self._speed = speed
		self._type = type

	# Next four methods will return the class Enemy data
	def get_hitpoints(self):
		return self._hitpoints

	def get_armour(self):
		return self._armour

	def get_speed(self):
		return self._speed

	def get_type(self):
		return self._type


	def reduce_hitpoints(self, damage):				# In case enemy is hit, lower it's hitpoints
		self._hitpoints -= damage


	hitpoints = property(get_hitpoints)
	armour = property(get_armour)
	speed = property(get_speed)
	type = property(get_type)