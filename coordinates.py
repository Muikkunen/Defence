import math

def distance(start, end):
	# Returns distance between two specified coordinates
	distance_x = end[0] - start[0]
	distance_y = end[1] - start[1]

	distance = (distance_x**2 + distance_y**2)**(0.5)
	return distance


def new_location(current_location, target_location, speed):
	# Returns new location which is calculated by moving a specified length from current coordinates to the target coordinates

	# Construct a vector to point from current coordinates to the target coordinates
	vector = [target_location[0] - current_location[0], target_location[1] - current_location[1]]

	vector_length = (vector[0]**2 + vector[1]**2)**(0.5)					# Calculate the vector's length
	unit_vector = [vector[0] / vector_length, vector[1] / vector_length]	# Calculate a unit vector

	transition = [i * speed for i in unit_vector]							# Calculate the transition

	# Calculate the new coordinates to which the object should move by summing the transition vector to current location
	new_location = [current_location[0] + transition[0], current_location[1] + transition[1]]
	return new_location


def direction(current_location, target_location, current_direction):
	movement_x_axis = target_location[0] - current_location[0]				# Calculate the movement distance on x-axis
	movement_y_axis = target_location[1] - current_location[1]				# Calculate the movement distance on y-axis

	# If object does not move on x-axis, the direction is either 90 (up) or 270 (down) degrees
	if movement_x_axis == 0:
		if movement_y_axis > 0:
			return 90
		else:
			return 270

	# Similarly on y-axis, the direction is either 0 (right) or 180 (left) degrees
	if movement_y_axis == 0:
		if movement_x_axis > 0:
			return 0
		else:
			return 180
		

	# To prevent ZeroDivisionError, return previous direction if the enemy will not move when this function is called
	try:
		# Calculate the direction by taking inverse tangent from the division of y- and x-movements and then converting it
		#	from radians to degrees
		direction = math.degrees(math.atan(movement_y_axis / movement_x_axis))	

		# If the object should move to north-west or south-west, add 180 degrees to calculate the direction right
		if (movement_x_axis < 0 and movement_y_axis > 0) or (movement_x_axis < 0  and movement_y_axis < 0):
			direction += 180

		return direction
	except ZeroDivisionError:
		return current_direction

