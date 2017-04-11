from coordinates import *

class Enemy(object):

	def __init__ (self, enemy_type, name, hitpoints, armour, speed, worth, game):
		# (Pass these for subclass)
		self.enemy_type = enemy_type
		self.name = name
		self.hitpoints = hitpoints
		self.armour = armour
		self.speed = speed
		self.worth = worth
		self.game = game
		self.location = None
		self.destination = None

	
	# Move the enemy
	def move(self, speed):

		# If destination has not been set, set it to the board's second route point (first is the starting point)
		if self.destination == None:
			self.destination = list(self.game.get_board().get_route_points()[1])

		# If the enemy should move vertically, set first_indicator to 0 and if horizontally, set it to 1
		if self.location[0] == self.destination[0]:
			first_indicator = 1
		else:
			first_indicator = 0

		# If the enemy should move to positive coordinate direction (down or right) set indicator to 1
		#	and if to negative coordinate direction (up or left) set it to -1
		if self.location[first_indicator] < self.destination[first_indicator]:
			second_indicator = 1
		else:
			second_indicator = -1

		# Calculate the distance between the current location and the next destination
		distance = distance_between(self.location, self.destination)

		# If enemy will reach next route point on it's way, move to the next coordinate point
		#	and then change go to the second coordinate point as much as there's 'speed' left
		if distance < speed:
			self.location = self.destination

			# Set the next destination, if the set_next_destination() function returns True, Enemy has reached its goal
			if self.set_next_destination():

				# If Enemy has reached its true, function returns True to indicate that the Enemy should be killed
				return True							

			self.move(speed - distance)				# Call function again to move remaining amount of the speed
			return False							# Enemy is still alive

		# Finally actually move the enemy and convert to int to avoid decimal numbers which occur due to multiplying with -1
		self.location[first_indicator] += int(speed * (second_indicator))


	def set_next_destination(self):
		route_points = self.game.get_board().get_route_points()

		# If current destination is the last route point, the Enemy has reached it's goal and should be deleted,
		#	in the event points and money should not be increased but one life from game should be deleted
		if self.destination == list(route_points[-1]):
			self.game.lose_life()
			return True

		# Implemet catching ValueError HERE which will be raised when the position will not be found IF NEEDED--------------------------
		
		# Find the position of the current destination in the board's route_points list and add one to it to get the next destination
		next_destination = list(route_points[route_points.index(tuple(self.destination)) + 1])

		self.destination = next_destination
		return False


	# Next four methods will return the Enemy class's data
	def get_hitpoints(self):
		return self.hitpoints

	def get_armour(self):
		return self.armour

	def get_speed(self):
		return self.speed

	def get_type(self):
		return self.type

	def get_worth(self):
		return self.worth

	def set_location(self, location):
		self.location = location




	# In case enemy is hit, lower it's hitpoints
	def reduce_hitpoints(self, damage):

		# If enemy's armour is greater than the damage, do nothing
		if damage < armour:
			return

		self.hitpoints -= (damage - armour)
		return



	"""
	hitpoints = property(get_hitpoints)
	armour = property(get_armour)
	speed = property(get_speed)
	enemy_type = property(get_type)"""