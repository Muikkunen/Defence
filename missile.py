class Missile(object):

	def __init__ (self, missile_type, speed):
		self.missile_type = missile_type
		self.speed = speed


	def initialize(self, target, damage):		# Set the target and damage for missile
		self.target = target
		self.damage = damage