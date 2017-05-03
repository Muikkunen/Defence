from coordinates import distance, new_location, direction


class Missile(object):

	#def __init__ (self, missile_type, speed):

	def __init__ (self, missile_information):
		if missile_information[0] in ["Cannon"]:			# If type is defined here, the missile moves to the point where the enemy was when it was shot
			self.static_target = True
		elif missile_information[0] in ["Rocket"]:			# If type is defined here, the missile moves towards the enemy
			self.static_target = False
		else:									# If neither case is true, the type of the missile is not defined here and should be added
			raise SystemExit(missile_type + " is a type of missile that is not "\
				"defined in class Missile and should be added before playing.")

		self.type = missile_information[0]
		self.speed = missile_information[1]
		self.radius = missile_information[2]
		self.explosion_time = missile_information[3]

		self.damage = None
		self.location = None
		self.target = None
		self.target_location = []

		self.degrees = None

	def get_type(self):
		return self.type

	def get_damage(self):
		return self.damage

	def get_location(self):
		return self.location

	def get_degrees(self):
		return self.degrees


	def initialize(self, tower, target):
		self.location = tower.get_location()			# Set missile's location according to the location of the tower that created it
		self.target = target 							# Set missile's target to the enemy to which it was shot
		self.target_location[:] = target.get_location()	# Set missile's target location to the enemy's current location, see also function move()

		"""
		if self.static_target:
			self.target_location = target.get_location()	# Target will not change even if the target enemy moves
		else:
			self.target = target 				# Target will change when the target enemy moves"""

		self.damage = tower.get_damage() 		# Missile gets its damage from the tower that created it


	# Move the missile, returns True if missile should be deleted (it has hit its target or missile target is not static
	#	and the enemy has been deleted and False if otherwise
	def move(self, enemies, gui):
		if self.target == None:					# If target has been deleted, return True to indicate that the missile should be deleted
			return True


		# If the specified target is not static, move the missile towards its target (enemy)
		# 	otherwise move towards to the previously defined point where the enemy was when missile was initialized
		if not self.static_target:
			self.target_location = self.target.get_location()

		# Calculate the distance between missile and target
		if distance(self.location, self.target_location) <= self.speed:

			# If missile's type is static, check which enemies are in missile's explosion radius
			if self.static_target:
				for enemy in enemies:
					# If the distance between the explosion location and the enemy's location, reduce enemy's hitpoints
					if distance(self.target_location, enemy.get_location()) <= self.radius: 
						enemy.reduce_hitpoints(self.damage)

				gui.add_explosion_graphics_item(self.target_location, self.type, self.explosion_time)

				return True 					# Return True to indicate that the missile has hit its target and should be deleted
			else:
				self.target.reduce_hitpoints(self.damage)
				return True

		self.location = new_location(self.location, self.target_location, self.speed)
		self.degrees = direction(self.location, self.target_location, self.degrees)
		return False