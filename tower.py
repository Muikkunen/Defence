import coordinates

class Tower(object):
	FIRST = 0
	CLOSEST = 1
	STRONGEST = 2
	WEAKEST = 3


	def __init__ (self, tower_type, damage, shoot_range, reload_time, build_time, game):
		self.type = tower_type
		self.damage = damage
		self.shoot_range = shoot_range
		self.reload_time = reload_time
		self.build_time = build_time
		self.game = game
		self.target_type = Tower.FIRST 				# As default the Tower shoots the enemy that is first released


	def get_type(self):
		return self.type

	def get_damage(self):
		return self.damage

	def get_shoot_range(self):
		return self.shoot_range

	def get_reload_time(self):
		return self.reload_time

	def get_build_time(self):
		return self.build_time

	def get_target_type(self):
		return self.target_type


	# Tower shoots according to the specified target
	def select_target(self):
		enemies_in_range = []

		# Find enemies that the Tower is able to shoot
		for enemy in self.game.get_board().get_enemies():
			if distance(self.location, enemy.get_location()) <= self.range:
				enemies_in_range.append(enemy)

		if enemies_in_range == []:					# Tower does not shoot, because zero enemies are in range
			return

		if self.target_type == Tower.FIRST:			# Tower shoots the first enemy in its range
			self.shoot_first_enemy(enemies_in_range)
		elif self.target_type == Tower.CLOSEST:		# Tower shoots the enemy to which the distance is shortest
			self.shoot_closest_enemy(enemies_in_range)
		elif self.target_type == Tower.STRONGEST:	# Tower shoots the strongest enemy in its range
			self.shoot_strongest_enemy(enemies_in_range)
		elif self.target_type == Tower.WEAKEST:		# Tower shoots the weakest enemy in its range
			self.shoot_weakest_enemy(enemies_in_range)


	def first_enemy(self, enemies):
		self.shoot(enemies[0])


	def closest_enemy(self, enemies):
		distance_to_selected_enemy = None	# Set variable for shortest distance
		enemy_to_be_shot = enemies[0]		# Set variable to store the Enemy with shortest distance to Tower

		# Use slicing to generate new list without first key to prevent from comparing first key to itself and
		#	iterate through enemies to find the closest enemy
		for enemy in enemies[1:]:
			distance_to_current_enemy = distance(self.location, enemy.get_location())

			# If the current distance is shorter than the distance to the selected Enemy, replace the selected distance with current distance
			if distance_to_current_enemy < distance_to_selected_enemy:
				distance_to_selected_enemy = distance_to_current_enemy
				enemy_to_be_shot = enemy

		self.shoot(enemy_to_be_shot)

	# See the method closest_enemy() for details of this method
	def shoot_strongest_enemy(self, enemies):
		enemy_to_be_shot = enemies[0]

		# Iterate through enemies to find the strongest one
		for enemy in enemies[1:]:
			if enemy_to_be_shot.get_hitpoints() < enemy.get_hitpoints():
				enemy_to_be_shot = enemy

		self.shoot(enemy_to_be_shot)

	# See the method closest_enemy() for details of this method
	def shoot_weakest_enemy(self, enemies):
		enemy_to_be_shot = enemies[0]

		# Iterate through enemies to find the weakest one
		for enemy in enemies[1:]:
			if enemy_to_be_shot.get_hitpoints() > enemy.get_hitpoints():
				enemy_to_be_shot = enemy

		self.shoot(enemy_to_be_shot)


	def shoot(self, target):
		missile = Missile(target)
		game.get_board().add_missile(missile)


	def set_location(self, location):
		self.location = location