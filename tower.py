from coordinates import distance
from missile import Missile

from PyQt5 import QtCore
#from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QSound


class Tower(object):
	FIRST = 0
	CLOSEST = 1
	STRONGEST = 2
	WEAKEST = 3


	#def __init__ (self, tower_type, damage, shoot_range, reload_time, build_time, sound_effect, game):

	def __init__ (self, tower_information):	
		self.type = tower_information[0]
		self.damage = tower_information[1]
		self.shoot_range = tower_information[2]
		self.reload_time = tower_information[3]
		self.build_time = tower_information[4]
		#self.sound_effect = QSound(sound_effect)
		self.game = tower_information[6]
		self.target_type = Tower.FIRST 					# As default the tower shoots the enemy that is first released
		self.location = None							# Location will be set when player puts the tower to the board
														# 	it defines the coordinates where the Tower is
		self.reloading = False							# Indicate whether the tower is reloading or not
		self.reload_timer = QtCore.QTimer()				# Timer to keep on track the reloading time

		self.building = True 							# Indicate whether the tower is still building or not
		self.build_timer = QtCore.QTimer()				# Timer to measure tower building
		self.build_timer.setSingleShot(True)			# Set timer to measure time only once since tower will be built only once


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

	def get_location(self):
		return self.location

	def get_building(self):
		return self.building


	# Tower shoots according to the specified target
	def select_target(self):
		enemies_in_range = []

		# Find enemies that the Tower is able to shoot
		for enemy in self.game.get_board().get_enemies():
			if distance(self.location, enemy.get_location()) <= self.shoot_range:
				enemies_in_range.append(enemy)
		

		if enemies_in_range == []:								# Tower does not shoot, because zero enemies are in range
			return

		if self.target_type == Tower.FIRST:						# Tower shoots the first enemy in its range
			return self.shoot_first_enemy(enemies_in_range)
		elif self.target_type == Tower.CLOSEST:					# Tower shoots the enemy to which the distance is shortest
			return self.shoot_closest_enemy(enemies_in_range)
		elif self.target_type == Tower.STRONGEST:				# Tower shoots the strongest enemy in its range
			return self.shoot_strongest_enemy(enemies_in_range)
		elif self.target_type == Tower.WEAKEST:					# Tower shoots the weakest enemy in its range
			return self.shoot_weakest_enemy(enemies_in_range)


	def shoot_first_enemy(self, enemies):
		return enemies[0]


	def shoot_closest_enemy(self, enemies):
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

		return enemy_to_be_shot

	# See the method closest_enemy() for details of this method
	def shoot_strongest_enemy(self, enemies):
		enemy_to_be_shot = enemies[0]

		# Iterate through enemies to find the strongest one
		for enemy in enemies[1:]:
			if enemy_to_be_shot.get_hitpoints() < enemy.get_hitpoints():
				enemy_to_be_shot = enemy

		return enemy_to_be_shot

	# See the method closest_enemy() for details of this method
	def shoot_weakest_enemy(self, enemies):
		enemy_to_be_shot = enemies[0]

		# Iterate through enemies to find the weakest one
		for enemy in enemies[1:]:
			if enemy_to_be_shot.get_hitpoints() > enemy.get_hitpoints():
				enemy_to_be_shot = enemy

		return enemy_to_be_shot


	def shoot(self):
		if self.reloading or self.building:								# Tower does not shoot if it is reloading or building
			return

		target = self.select_target()
		if target == None:												# Tower does not shoot if zero enemies are in its range
			return None													# Return None to indicate that a missile was not created

		missile = Missile(self.game.get_missile_types()[self.type])		# Select the missile type from game's dictionary
		missile.initialize(self, target)								# Initialize the missile's information; target and damage
		self.game.get_board().add_missile(missile)						# Add missile to board

		# Set reloading indicator to True to indicate that tower cannot shoot reloading time has passed
		self.reloading = True
		self.reload_timer.start(self.reload_time)						# Start reload_timer for reloading

		# When reload_timer has finished, change indicator value to False to indicate that the tower can shoot again
		self.reload_timer.timeout.connect(self.stop_reloading)
		#self.sound_effect.play()

		return missile 													# Return the created missile

	def stop_reloading(self):
		self.reloading = False


	def set_location(self, location):
		self.location = location

		# When tower is placed on the board, start timer to measure when tower is built and therefore ready to shoot
		self.build_timer.start(self.build_time)
		self.build_timer.timeout.connect(self.build)
		

	def build(self):
		self.building = False