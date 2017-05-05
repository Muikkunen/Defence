from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QPushButton, QGraphicsSceneMouseEvent, QGraphicsTextItem, QLabel
from PyQt5.QtGui import QBrush, QColor, QFont
from PyQt5.QtCore import QTimer

from enemy_graphics_item import EnemyGraphicsItem
from tower_graphics_item import TowerGraphicsItem
from missile_graphics_item import MissileGraphicsItem
from explosion_graphics_item import ExplosionGraphicsItem
from board_graphics_item import BoardGraphicsItem
from menu_graphics_item import MenuGraphicsItem
from text_item import TextItem
from player_name import PlayerName
from load_high_scores import LoadHighScores
from build_tower_graphics_item import BuildTowerGraphicsItem
from building_slot_graphics_item import BuildingSlotGraphicsItem

from add_board_graphics import add_board_graphics
from add_high_score import add_high_score



from PyQt5.QtWidgets import QWidget, QLineEdit, QApplication



class GUI(QtWidgets.QMainWindow):

	def __init__(self, game, high_scores, high_scores_data):
		super().__init__()
		self.scene = QtWidgets.QGraphicsScene()
		self.window_size = [1900, 1200]

		self.scene.setSceneRect(0, 0, self.window_size[0], self.window_size[1])

		self.view = QtWidgets.QGraphicsView(self.scene, self)
		self.view.setBackgroundBrush(QBrush(QColor("Black")))	# Set background to black
		self.view.adjustSize()
		#self.view.show()

		self.setCentralWidget(self.view)


		#self.setCentralWidget(QtWidgets.QWidget()) 			# QMainWindown must have a centralWidget to be able to add layouts

		self.showFullScreen()
		self.showMaximized()
		self.setWindowTitle("Defence")
		#self.show()

		self.play_text_items			=	[]
		self.high_scores_text_items 	=	[]
		self.board_graphics_items 		=	[]
		self.enemy_graphics_items 		=	[]
		self.tower_base_graphics_items 	= 	[]
		self.tower_graphics_items 		=	[]
		self.missile_graphics_items 	=	[]
		self.explosion_graphics_items 	= 	[]
		self.menu_graphics_items 		=	[]
		self.buildable_graphics_items 	= 	[]
		self.building_slots 			= 	[]

		self.game = game
		self.high_scores = high_scores
		self.high_scores_data = high_scores_data
		self.square_size = game.get_board().get_square_size()
		self.main_menu_item = MenuGraphicsItem(self, "images/main_menu.png", self.window_size[0] / 10 * 9, self.window_size[1] / 10 * 9, "Main Menu")

		self.next_wave_timer = QTimer()

		self.main_menu()

		#self.init_buttons()

		#self.play()

	def get_game(self):
		return self.game


	def add_all_graphics(self):
		squares = self.game.get_board().get_squares()
		self.board_graphics_items = add_board_graphics(self.game.get_board().get_difficulty(), squares, self.square_size, self.scene)

		self.add_text_graphics_items()
		self.add_buildable_tower_graphics_items()


	def add_enemies(self):
		self.enemies_to_be_added = self.game.next_wave()

		if self.game.get_board().get_current_wave() % 10 == 0:
			current_interval = self.game.get_enemy_spawn_interval()
			new_interval = int(current_interval / 2)
			self.game.set_enemy_spawn_interval(new_interval)
			

	def add_enemy_graphics_item(self):
		enemy = self.enemies_to_be_added[0]
		self.enemies_to_be_added.remove(enemy)
		if self.enemies_to_be_added == []:					# If all enemies have been added, indicate that new ones can be added
			self.game.get_board().set_enemies_added()

		enemy = self.game.get_board().add_enemy(enemy, self.game.get_board().get_enemy_start_location())
		enemy_graphics_item = EnemyGraphicsItem(enemy, self.square_size)
		if enemy_graphics_item.has_shadow():
			self.scene.addItem(enemy_graphics_item.get_shadow())
		self.enemy_graphics_items.append(enemy_graphics_item)
		self.scene.addItem(enemy_graphics_item)
		self.new_enemy_timer.setSingleShot(True)
		self.new_enemy_timer.start(self.game.get_enemy_spawn_interval())


	def add_tower_base_graphics_item(self, tower):
		for item in self.buildable_graphics_items:
			item.set_building(False)

		tower_base_graphics_item = TowerGraphicsItem(tower, self.square_size)
		self.tower_base_graphics_items.append(tower_base_graphics_item)
		self.scene.addItem(tower_base_graphics_item)

		for item in self.building_slots:
			self.scene.removeItem(item)
		self.building_slots = []


	def add_explosion_graphics_item(self, location, explosion_type, time):
		explosion_graphics_item = ExplosionGraphicsItem(location, explosion_type, time, self.square_size)
		self.explosion_graphics_items.append(explosion_graphics_item)
		self.scene.addItem(explosion_graphics_item)

	def add_text_graphics_items(self):
		self.qLabel = QLabel(self)
		self.qLabel.setStyleSheet("QLabel {color : white; }")
		self.qLabel.setText("Hover over an object to receive information about it")
		self.qLabel.move(1600, 1150)
		self.qLabel.setFixedWidth(1000)
		self.qLabel.show()


		font_size = 15
		level = TextItem("Level: " + str(self.game.get_board().get_current_wave()), font_size, 20, 800)
		#time = TextItem("Time until next wave: 0", font_size, 20, 900)
		points = TextItem("Points: \n" + str(self.game.get_points()), font_size, 20, 1000)
		money = TextItem("Money: \n" + str(self.game.get_money()), font_size, 200, 1000)
		lives = TextItem("Lives: \n" + str(self.game.get_lives()), font_size, 380, 1000)
		tower_building_information = TextItem("Build a tower:", font_size, 700, 800)

		text_items = [level, points, money, lives, tower_building_information]

		for item in text_items:
			self.scene.addItem(item)
			self.play_text_items.append(item)


	def add_buildable_tower_graphics_items(self):
		cannon = BuildTowerGraphicsItem(self.game.get_tower_types()["Cannon"], 700, 900, self.square_size, self)
		machine_gun = BuildTowerGraphicsItem(self.game.get_tower_types()["MachineGun"], 900, 900, self.square_size, self)
		rocket_launcher = BuildTowerGraphicsItem(self.game.get_tower_types()["RocketLauncher"], 1100, 900, self.square_size, self)
		double_rocket_launcher = BuildTowerGraphicsItem(self.game.get_tower_types()["DoubleRocketLauncher"], 700, 1000, self.square_size, self)
		tank = BuildTowerGraphicsItem(self.game.get_tower_types()["Tank"], 900, 1000, self.square_size, self)
		leopard = BuildTowerGraphicsItem(self.game.get_tower_types()["Leopard"], 1100, 1000, self.square_size, self)

		tower_graphics_items = [cannon, machine_gun, rocket_launcher, double_rocket_launcher, tank, leopard]
		
		for item in tower_graphics_items:
			self.scene.addItem(item)
			self.buildable_graphics_items.append(item)

	def add_building_slots(self, tower_type):
		for item in self.buildable_graphics_items:
			item.set_building(True)

		squares = self.game.get_board().get_squares()
		for squares_list in squares:
			i = squares.index(squares_list)
			for square in squares_list:
				j = squares_list.index(square)
				if square.contains() == 0:
					slot = BuildingSlotGraphicsItem(tower_type, i, j, self.square_size, "Building_slot.png", self)
					self.scene.addItem(slot)
					self.building_slots.append(slot)


	def update_all(self):
		self.is_game_over()
		self.update_enemies()										# Firstly the enemies move
		self.update_towers(self.game.get_board().get_towers())		# Then  the towers shoot according to their targets
		self.update_missiles(self.game.get_board().get_missiles())	# Lastly the missiles that were created as well as the previously created ones move
		self.update_explosions()									# Update explosion effects
		self.update_text_graphics_items()							# Update text's that indicate game information
		


	def update_enemies(self):
		if self.enemies_to_be_added != []:
			if self.new_enemy_timer.remainingTime() < 0:
				self.add_enemy_graphics_item()

		enemies = self.game.get_board().get_enemies()

		if enemies == []:
			if not self.game.get_board().is_adding_enemies():		# Do not add new enemies if enemies are currently being added
				self.game.get_board().set_adding_enemies()
				self.next_wave_timer.singleShot(self.game.get_time_between_waves(), self.add_enemies)
		else:
			enemies[:] = [enemy for enemy in enemies if not enemy.is_dead()] 	# Check which enemies are dead
			enemies[:] = [enemy for enemy in enemies if not enemy.move()]		# Move the enemies

			enemy_graphics_items_to_be_removed = []

			for enemy_graphics_item in self.enemy_graphics_items:
				if enemy_graphics_item.get_enemy() in enemies:
					enemy_graphics_item.update_graphics()
				else:
					self.scene.removeItem(enemy_graphics_item)
					if enemy_graphics_item.has_shadow():
						self.scene.removeItem(enemy_graphics_item.get_shadow())
					enemy_graphics_items_to_be_removed.append(enemy_graphics_item)

			for item in enemy_graphics_items_to_be_removed:
				self.enemy_graphics_items.remove(item)

	def update_towers(self, towers):
		for tower in towers:							# Iterate through towers
			missile = tower.shoot()						# Tower shoots and creates a missile
			if missile != None:							
				missile_graphics_item = MissileGraphicsItem(missile, self.square_size)			# Create graphics item for missile
				self.missile_graphics_items.append(missile_graphics_item)
				self.scene.addItem(missile_graphics_item)

		for tower_base_graphics_item in self.tower_base_graphics_items:
			tower_base_graphics_item.update_graphics()
			if tower_base_graphics_item.build():
				tower_graphics_item = TowerGraphicsItem(tower_base_graphics_item.get_tower(), self.square_size)
				self.tower_graphics_items.append(tower_graphics_item)
				self.scene.addItem(tower_graphics_item)

		for tower_graphics_item in self.tower_graphics_items:
			tower_graphics_item.update_graphics()

	def update_missiles(self, missiles):
		# Move missiles and remove those, which have reached their target or whose target has reached goal
		missiles[:] = [missile for missile in missiles if not missile.move(self.game.get_board().get_enemies(), self)]

		new_missile_graphics_items = []

		for missile_graphics_item in self.missile_graphics_items:
			if missile_graphics_item.get_missile() in missiles:
				missile_graphics_item.update_graphics()
				new_missile_graphics_items.append(missile_graphics_item)
			else:
				self.scene.removeItem(missile_graphics_item)

		self.missile_graphics_items = new_missile_graphics_items

	def update_explosions(self):
		items_to_be_removed = []
		for item in self.explosion_graphics_items:
			if item.time_passed() <= 0:
				items_to_be_removed.append(item)

		for item in items_to_be_removed:
			self.scene.removeItem(item)
			self.explosion_graphics_items.remove(item)

	def update_text_graphics_items(self):
		for item in self.buildable_graphics_items:
			if item.isUnderMouse(): 
				tower = item.get_tower()
				information = "Costs: " + str(tower[5]) + ", Range: " + str(tower[2]) + ", Damage: " + str(tower[1]) \
					+ ", Builds in: " + str(tower[4] / 1000) + " s" + ", Reloads in: " + str(tower[3] / 1000) + " s"
				self.qLabel.setText(information)

		for item in self.enemy_graphics_items:
			if item.isUnderMouse():
				enemy = item.get_enemy()
				information = "Type: " + str(enemy.get_type()) + ", Hitpoints: " + str(enemy.get_hitpoints()) + ", Speed: " \
					+ str(enemy.get_speed()) + ", Worth: " + str(enemy.get_worth())
				self.qLabel.setText(information)

		for item in self.tower_graphics_items:
			if item.isUnderMouse():
				target_type = item.get_tower().get_target_type()
				if target_type == 0:
					target = "first"
				elif target_type == 1:
					target = "closest"
				elif target_type == 2:
					target = "strongest"
				else:
					target = "weakest"
				information = "Tower has been set to shoot the " + target + " enemy"
				self.qLabel.setText(information)

		self.qLabel.show()

		updated_texts = ["Level: " + str(self.game.get_board().get_current_wave()), "Points: \n" + str(self.game.get_points()),
		"Money: \n" + str(self.game.get_money()), "Lives: \n" + str(self.game.get_lives()), "Build a tower:"]

		for item in self.play_text_items:
			item.set_text(updated_texts[self.play_text_items.index(item)])

	def is_game_over(self):
		if self.game.get_lives() <= 0:
			self.timer.stop()

			self.qLabel.setText("")

			for item in self.play_text_items:
				self.scene.removeItem(item)
			self.play_text_items = []
			for item in self.board_graphics_items:
				self.scene.removeItem(item)
			self.board_graphics_items = []
			for item in self.enemy_graphics_items:
				self.scene.removeItem(item)
			self.enemy_graphics_items = []
			for item in self.tower_graphics_items:
				self.scene.removeItem(item)
			self.tower_graphics_items = []
			for item in self.missile_graphics_items:
				self.scene.removeItem(item)
			self.missile_graphics_items = []
			for item in self.tower_base_graphics_items:
				self.scene.removeItem(item)
			self.tower_base_graphics_items = []
			for item in self.explosion_graphics_items:
				self.scene.removeItem(item)
			self.explosion_graphics_items = []
			for item in self.menu_graphics_items:
				self.scene.removeItem(item)
			self.menu_graphics_items = []
			for item in self.buildable_graphics_items:
				self.scene.removeItem(item)
			self.buildable_graphics_items = []
			for item in self.building_slots:
				self.scene.removeItem(item)
			self.building_slots = []


			self.level = self.game.get_board().get_current_wave()
			self.points = self.game.get_points()

			self.qLineEdit = PlayerName(self)
			text = "Game over, enter username and hit Enter. Maximum 15 charactes, whitespace not allowed"
			text_item = TextItem(text, 40, 200, 200)
			self.scene.addItem(text_item)
			self.menu_graphics_items.append(text_item)

	
	def check_points(self):
		name = self.qLineEdit.get_text()
		name = "".join(name.split())
		add_high_score(self.high_scores_data, "#" + self.game.get_board().get_difficulty(), name, self.level, self.points)
		self.qLineEdit.setParent(None)
		self.game.initialize()

		self.show_high_scores()


	def main_menu(self):
		# If high scores have been viewed, remove them from the scene
		for item in self.high_scores_text_items:
			self.scene.removeItem(item)
		self.high_scores_items = []
		if self.scene.items() != []:
			self.scene.removeItem(self.main_menu_item)

		font = QFont("Comic Sans", 40)					# Set font for menu instructions
		color = QColor("White")							# Set font color
		text = "Click one of the icons to proceed"		# Set the instruction text
		menu_text = QGraphicsTextItem(text)				# Create the actual text item
		menu_text.setFont(font)
		menu_text.setDefaultTextColor(color)
		menu_text.setPos(200, 900)
		self.scene.addItem(menu_text)


		play_item = MenuGraphicsItem(self, "images/play.png", self.window_size[0] / 4, self.window_size[1] / 2, "Play")
		high_scores_item = MenuGraphicsItem(self, "images/high_scores.png", self.window_size[0] / 4 * 3, self.window_size[1] / 2, "High Scores")
		self.scene.addItem(play_item)
		self.scene.addItem(high_scores_item)

		self.menu_graphics_items.append(menu_text)
		self.menu_graphics_items.append(play_item)
		self.menu_graphics_items.append(high_scores_item)


	def choose_difficulty(self):
		# Remove menu items from scene
		for item in self.menu_graphics_items:
			self.scene.removeItem(item)
		self.menu_graphics_items = []

		easy = MenuGraphicsItem(self, "images/Easy.png", self.window_size[0] / 10, self.window_size[1] / 2, "Easy")
		medium = MenuGraphicsItem(self, "images/Medium.png", self.window_size[0] / 10 * 5, self.window_size[1] / 2, "Medium")
		hard = MenuGraphicsItem(self, "images/Hard.png", self.window_size[0] / 10 * 9, self.window_size[1] / 2, "Hard")
		self.menu_graphics_items.append(easy)
		self.menu_graphics_items.append(medium)
		self.menu_graphics_items.append(hard)

		size = 30
		instructions = ["Choose difficulty:", 50, 400, 10]
		text_for_easy = ["Easy", size, easy.pos().x(), easy.pos().y() + easy.height()]
		text_for_medium	= ["Medium", size, medium.pos().x(), medium.pos().y() + medium.height()]
		text_for_hard = ["Hard", size, hard.pos().x(), hard.pos().y() + hard.height()]
		texts = [instructions, text_for_easy, text_for_medium, text_for_hard]

		for text in texts:
			text_item = TextItem(text[0], text[1], text[2], text[3])
			self.menu_graphics_items.append(text_item)


		for item in self.menu_graphics_items:
			self.scene.addItem(item)


	def play(self):
		for item in self.menu_graphics_items:
			self.scene.removeItem(item)
		self.menu_graphics_items = []

		self.enemies_to_be_added = []
		self.new_enemy_timer = QTimer()

		self.add_all_graphics()
		self.update_all()

		# Set a timer to call the update function periodically
		self.timer = QTimer()
		self.timer.start(self.game.get_fps()) 				# Milliseconds
		self.timer.timeout.connect(self.update_all)



	def show_high_scores(self):
		for item in self.menu_graphics_items:
			self.scene.removeItem(item)
		
		headers = ["Easy", "Medium", "Hard"]
		x = 20
		
		for header in headers:
			text_item = TextItem(header, 30, x, 200)
			self.high_scores_text_items.append(text_item)
			self.scene.addItem(text_item)
			x += 600

		self.high_scores = LoadHighScores().load(self.high_scores_data)
		
		font_size = 12
		y = 300
		x_increment = 0

		for header in headers:
			for scores in self.high_scores[header]:
				x = 20 + x_increment
				for text in scores:
					text_item = TextItem(text, font_size, x, y)
					self.high_scores_text_items.append(text_item)
					self.scene.addItem(text_item)
					if scores.index(text) == 0:
						x += 225
					elif scores.index(text) == 1:
						x += 120
				y += font_size + 30
			x_increment += 600
			y = 300

		self.scene.addItem(self.main_menu_item)