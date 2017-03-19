import coordinates

class Tower(object):

	def __init__ (self, location, damage, shoot_range, relay_time, build_time):
		self.location = location
		self.damage = damage
		self.shoot_range = shoot_range
		self.relay_time = relay_time
		self.build_time = build_time

"""
	def enemy_in_range(self, enemys):
		for enemy in enemys:
			if distance(enemy.get_location(), location) <= shoot_range:
				self.shoot(enemy.get_location())

	def shoot(self, target):
		missile = Missile(target)
		game.add_missile(missile, target)


def main():
	tower = Tower((1, 1), 100, 10, 10, 10)


main()"""