from coordinates import distance, new_location, direction

class Enemy(object):
	
	def __init__ (self, enemy_information):
		self.enemy_type = enemy_information[0]
		self.name = enemy_information[1]
		self.hitpoints = enemy_information[2]
		self.armour = enemy_information[3]
		self.speed = enemy_information[4]
		self.worth = enemy_information[5]
		self.image = enemy_information[6]
		self.shadow = enemy_information[7]
		self.game = enemy_information[8]
		self.location = None						# When initialized, enemy's current location has not been set
		self.destination = None						# When initialized, enemy does not have destination
		self.degrees = None 						# Therefore enemy lacks also the direction to which it is going

	# Next methods will return the Enemy class's data
	def get_type(self):
		return self.enemy_type

	def get_hitpoints(self):
		return self.hitpoints

	def get_armour(self):
		return self.armour

	def get_speed(self):
		return self.speed

	def get_worth(self):
		return self.worth

	def get_image(self):
		return self.image

	def get_shadow(self):
		return self.shadow

	def get_position(self):
		return self.location

	def get_location(self):
		return self.location

	def get_degrees(self):
		return self.degrees


	def set_location(self, location):
		square_size = self.game.get_board().get_square_size()
		self.location = [square_size * location[0], square_size * location[1]]

	"""def set_location(self, position):
		square_size = self.game.get_board().get_square_size()
		self.location = [position[0] * square_size, position[0] * square_size]"""

	
	# Move the enemy
	def move(self, speed = 0):
		if speed == 0:
			speed = self.speed

		# Set destination, if it has not been set
		if self.destination == None:
			self.set_next_destination()

		"""
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
			second_indicator = -1"""

		# Calculate the remaining distance between the current position and the next destination
		remaining_distance = distance(self.location, self.destination)

		# If enemy will reach next route point on it's way, move to the next coordinate point
		#	and then change go to the second coordinate point as much as there's 'speed' left
		if remaining_distance < speed:
			self.location = self.destination

			# Set the next destination, if the set_next_destination() function returns True, Enemy has reached its goal
			if self.set_next_destination():

				# If Enemy has reached its goal, function returns True to indicate that the Enemy should be killed
				return True

			self.move(speed - remaining_distance)		# Call function again to move remaining amount of the speed
			return False								# Enemy is still alive

		self.location = new_location(self.location, self.destination, self.speed)
		self.degrees = direction(self.location, self.destination, self.degrees)		# Calculate the direction to which the enemy is going to

		# Finally actually move the enemy and convert to int to avoid decimal numbers which occur due to multiplying with -1
		#self.location[first_indicator] += int(speed * (second_indicator))

		#print("Enemy's location: {}".format(self.location))
		#print("Enemy's hitpoints: {}".format(self.hitpoints))


	def set_next_destination(self):
		square_size = self.game.get_board().get_square_size()

		route_point_coordinates = []

		for destination in self.game.get_board().get_route_points():
			destination_coordinates = [square_size * destination[0], square_size * destination[1]]
			route_point_coordinates.append(destination_coordinates)

		#route_point_coordinates = [i * square_size for i in self.game.get_board().get_route_points()]

		# If destination has not been set, set it to the board's second route point (first is the starting point)
		if self.destination == None:
			self.destination = route_point_coordinates[1]
			return False


		# If current destination is the last route point, the Enemy has reached it's goal and should be deleted,
		#	in the event points and money should not be increased but one life from game should be deleted
		if self.destination == route_point_coordinates[-1]:
			self.game.lose_life()
			return True

		# Implemet catching ValueError HERE which will be raised when the position will not be found IF NEEDED-------------------------------------
		
		# Find the position of the current destination in the board's route_points list and add one to it to get the next destination
		self.destination = route_point_coordinates[route_point_coordinates.index(self.destination) + 1]
		return False


	# Returns boolean value whether the enemy is dead (True) or not (False)
	def is_dead(self):
		if self.hitpoints <= 0:
			# Increase player's money and points by enemy's worth
			self.game.increase_money(self.worth)
			self.game.increase_points(self.worth)
			return True
		else:
			return False


	# In case enemy is hit, lower its hitpoints
	def reduce_hitpoints(self, damage):

		# If enemy's armour is greater than the damage, do nothing
		if damage < self.armour:
			return

		self.hitpoints -= (damage - self.armour)
		return