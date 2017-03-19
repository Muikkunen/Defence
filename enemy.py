class Enemy(object):

	def __init__ (self, enemy_type, name, hitpoints, armour, speed, worth):
		# Pass these for subclass
		self.enemy_type = enemy_type
		self.name = name
		self.hitpoints = hitpoints
		self.armour = armour
		self.speed = speed
		self.worth = worth


	# Next four methods will return the Enemy class's data
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


	"""
	hitpoints = property(get_hitpoints)
	armour = property(get_armour)
	speed = property(get_speed)
	enemy_type = property(get_type)"""