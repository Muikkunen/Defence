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

	new_location = [i * speed for i in unit_vector]							# Calculate the new coordinates to which the object should move
	return new_location