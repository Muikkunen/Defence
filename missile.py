from coordinates import *

class Missile(object):

	#def __init__ (self, missile_type, speed):

	def __init__ (self, missile_information):
		if missile_information[0] in ["Cannon"]:			# If type is defined here, the missile moves to the point where the enemy was when it was shot
			self.static_target = True
		elif missile_information[0] in ["Rocket"]:		# If type is defined here, the missile moves towards the enemy
			self.static_target = False
		else:									# If neither case is true, the type of the missile is not defined here and should be added
			raise SystemExit(missile_type + " is a type of missile that is not "\
				"defined in class Missile and should be added before playing.")

		self.type = missile_information[0]
		self.speed = missile_information[1]

		self.damage = None
		self.location = None


	def get_damage(self):
		return self.damage


	def initialize(self, tower, target):		# Set the target, location and damage for missile
		self.location = tower.get_location()	# Set missile's location according to the location of the tower that created it

		# Missile either moves to a specified location or changes its destination on every update
		#	according to whether the static_target value is True or False
		if self.static_target:
			self.target = target.get_location()	# Target will not change even if the target enemy moves
		else:
			self.target = target 				# Target will change when the target enemy moves

		self.damage = tower.get_damage() 		# Missile gets its damage from the tower that created it


	# Move the missile, returns True if missile should be deleted (it has hit its target or missile target is not static
	#	and the enemy has been deleted and False if otherwise
	def move(self):
		if self.target == None:					# If target has been deleted, return True to indicate that the missile should be deleted
			return True							#	---Might not work-----------

		if self.static_target:					# If the specified target is static, move the missile towards to the point where the enemy was
			target = self.target 				#	when missile was initialized
		else:									# If the specified target is not static, move the target towards missile's target (enemy)
			target = self.target.get_location()	

		if distance(self.location, target) <= self.speed:
			self.target.reduce_hitpoints(self.damage)
			return True 						# Return True to indicate that the missile has hit its target and should be deleted
		

		self.location = new_location(self.location, target, self.speed)