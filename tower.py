import coordinates

class Tower(object):
	FIRST = 0
	CLOSEST = 1
	STRONGEST = 2
	WEAKEST = 3


	def __init__ (self, location, damage, shoot_range, relay_time, build_time, game):
		self.location = location
		self.damage = damage
		self.shoot_range = shoot_range
		self.relay_time = relay_time
		self.build_time = build_time
		self.game = game
		self.target_type = Tower.FIRST 				# As default the Tower shoots the enemy that is first released

	# Tower shoots according to the specified target
	def select_target(self):
		enemies_in_range = []

		for enemy in self.game.
			enemies_in_range.append(enemy)


		if self.target_type == Tower.FIRST:			# Tower shoots the first enemy
			self.shoot_first_enemy()
		elif self.target_type == Tower.CLOSEST:		# Tower shoots the enemy to which the distance is shortest
			self.shoot_closest_enemy()
		elif self.target_type == Tower.STRONGEST:	# Tower shoots the strongest enemy in its range
			self.shoot_strongest_enemy()
		elif self.target_type == Tower.WEAKEST:		# Tower shoots the weakest enemy in its range
			self.shoot_weakest_enemy()


	def closest_enemy(self, enemies):
		for enemy in enemies:
			if distance(self.location, enemy.get_location()) <= self.shoot_range:
				self.shoot(enemy.get_location())

	def shoot(self, target):
		missile = Missile(target)
		game.add_missile(missile, target)

