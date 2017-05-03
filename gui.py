from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QPushButton, QGraphicsSceneMouseEvent, QGraphicsTextItem
from PyQt5.QtGui import QBrush, QColor, QFont
from PyQt5.QtCore import QTimer

from enemy_graphics_item import EnemyGraphicsItem
from tower_graphics_item import TowerGraphicsItem
from missile_graphics_item import MissileGraphicsItem
from explosion_graphics_item import ExplosionGraphicsItem
from board_graphics_item import BoardGraphicsItem
from menu_graphics_item import MenuGraphicsItem
from text_item import TextItem

from add_board_graphics import add_board_graphics

class GUI(QtWidgets.QMainWindow):

	def __init__(self, game, high_scores):
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

		self.game = game
		self.high_scores = high_scores
		self.square_size = game.get_board().get_square_size()
		self.main_menu_item = MenuGraphicsItem(self, "images/main_menu.png", self.window_size[0] / 10 * 9, self.window_size[1] / 10 * 9, "Main Menu")


		self.main_menu()

		#self.init_buttons()

		#self.play()



	def add_all_graphics(self):
		squares = self.game.get_board().get_squares()
		self.board_graphics_items = add_board_graphics(squares, self.square_size, self.scene)


		# REMOVE THESE: -----------------------------------------------------------
		rocket = self.game.get_tower_types()["RocketLauncher"]
		cannon = self.game.get_tower_types()["Cannon"]
		machine_gun = self.game.get_tower_types()["MachineGun"]
		double_rocket = self.game.get_tower_types()["DoubleRocketLauncher"]
		tank = self.game.get_tower_types()["Tank"]
		leopard = self.game.get_tower_types()["Leopard"]
		position1 = [10, 5]
		position2 = [2, 3]
		position3 = [5, 6]
		position4 = [2, 5]
		position5 = [2, 7]
		position6 = [2, 4]
		self.game.get_board().add_tower(rocket, position1)
		self.game.get_board().add_tower(cannon, position2)
		self.game.get_board().add_tower(machine_gun, position3)
		self.game.get_board().add_tower(double_rocket, position4)
		self.game.get_board().add_tower(tank, position5)
		self.game.get_board().add_tower(leopard, position6)
		"""cannon = self.game.get_tower_types()["Cannon"]
		position = [10, 10]
		self.game.get_board().add_tower(cannon, position)"""
		#---------------------------------------------------------------

		print(self.game.get_board().get_towers())

		self.add_tower_base_graphics_item(self.game.get_board().get_towers()[0])
		self.add_tower_base_graphics_item(self.game.get_board().get_towers()[1])
		self.add_tower_base_graphics_item(self.game.get_board().get_towers()[2])
		self.add_tower_base_graphics_item(self.game.get_board().get_towers()[3])
		self.add_tower_base_graphics_item(self.game.get_board().get_towers()[4])
		self.add_tower_base_graphics_item(self.game.get_board().get_towers()[5])

		self.add_text_graphics_items()

		#self.scene.addItem(self.main_menu_item)


	def add_enemies(self):
		self.enemies_to_be_added = self.game.next_wave()

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
		tower_base_graphics_item = TowerGraphicsItem(tower, self.square_size)
		self.tower_base_graphics_items.append(tower_base_graphics_item)
		self.scene.addItem(tower_base_graphics_item)


	def add_explosion_graphics_item(self, location, explosion_type, time):
		explosion_graphics_item = ExplosionGraphicsItem(location, explosion_type, time, self.square_size)
		self.explosion_graphics_items.append(explosion_graphics_item)
		self.scene.addItem(explosion_graphics_item)

	def add_text_graphics_items(self):
		font_size = 15
		level = TextItem("Level: " + str(self.game.get_board().get_current_wave()), font_size, 20, 800)
		points = TextItem("Points: \n" + str(self.game.get_points()), font_size, 20, 1000)
		money = TextItem("Money: \n" + str(self.game.get_money()), font_size, 200, 1000)
		lives = TextItem("Lives: \n" + str(self.game.get_lives()), font_size, 380, 1000)

		text_items = [level, points, money, lives]

		for item in text_items:
			self.scene.addItem(item)
			self.play_text_items.append(item)

	def update_all(self):
		self.update_enemies()										# Firstly the enemies move
		self.update_towers(self.game.get_board().get_towers())		# Then  the towers shoot according to their targets
		self.update_missiles(self.game.get_board().get_missiles())	# Lastly the missiles that were created as well as the previously created ones move
		self.update_explosions()
		self.update_text_graphics_items()


	def update_enemies(self):
		# ADD WAVE HERE TO CHECK THAT NEW ENEMIES GET GRAPHICS ITEMS AND TO GET THE GAME LOGIC TO WORK
		if self.enemies_to_be_added != []:
			if self.new_enemy_timer.remainingTime() < 0:
				self.add_enemy_graphics_item()

		enemies = self.game.get_board().get_enemies()

		if enemies == []:
			if not self.game.get_board().is_adding_enemies():		# Do not add new enemies if enemies are currently being added
				self.game.get_board().set_adding_enemies()
				self.next_wave_timer = QTimer()
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
		for tower in towers:
			missile = tower.shoot()
			if missile != None:
				missile_graphics_item = MissileGraphicsItem(missile, self.square_size)
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
		updated_texts = ["Level: " + str(self.game.get_board().get_current_wave()), "Points: \n" + str(self.game.get_points()),
			 "Money: \n" + str(self.game.get_money()), "Lives: \n" + str(self.game.get_lives())]

		for item in self.play_text_items:
			item.set_text(updated_texts[self.play_text_items.index(item)])


	def main_menu(self):
		# If high scores have been viewed, remove them from the scene
		for item in self.high_scores_text_items:
			self.scene.removeItem(item)
		if self.scene.items() != []:
			self.scene.removeItem(self.main_menu_item)

		font = QFont("Comic Sans", 40)					# Set font for menu instructions
		color = QColor("White")							# Set font color
		text = "Click one of the icons to proceed"		# Set the instruction text
		self.menu_text = QGraphicsTextItem(text)		# Create the actual text item
		self.menu_text.setFont(font)
		self.menu_text.setDefaultTextColor(color)
		self.menu_text.setPos(200, 900)
		self.scene.addItem(self.menu_text)


		self.play_item = MenuGraphicsItem(self, "images/play.png", self.window_size[0] / 4, self.window_size[1] / 2, "Play")
		self.high_scores_item = MenuGraphicsItem(self, "images/high_scores.png", self.window_size[0] / 4 * 3, self.window_size[1] / 2, "High Scores")
		self.scene.addItem(self.play_item)
		self.scene.addItem(self.high_scores_item)

		#self.high_scores_text_item = MenuGraphicsItem(self, self.scene, "High Scores", font, color)

		#self.play_text_item.get_text().setPos(0, 300)
		#self.play_text_item.get_text().adjustSize()


		#self.high_scores_text_item.get_text().setPos(0, 600)
		#self.high_scores_text_item.get_text().adjustSize()




		#self.scene.addItem(self.play_text_item.get_text())
		#self.scene.addItem(self.high_scores_text_item)

		#if play_text_item.mousePressEvent(event):
		#	self.play()

		#elif high_scores_text_item.mousePressEvent():
		#	self.show_high_scores()


	def play(self):
		self.scene.removeItem(self.menu_text)				# Remove menu's text field fron scene
		self.scene.removeItem(self.play_item)				# Remove Play text button from scene
		self.scene.removeItem(self.high_scores_item)		# Remove High Scores text button from scene

		self.enemies_to_be_added = []
		self.new_enemy_timer = QTimer()

		self.add_all_graphics()
		self.update_all()

		# Set a timer to call the update function periodically
		self.timer = QTimer()
		self.timer.start(self.game.get_fps()) 				# Milliseconds
		self.timer.timeout.connect(self.update_all)



		#self.vertical_board = QtWidgets.QVBoxLayout() 			# Horizontal main layout
		#self.centralWidget().setLayout(self.vertical_board)
		
		#self.horizontal_controls = QtWidgets.QVBoxLayout()
		#self.centralWidget().setLayout(self.horizontal_controls)



		#self.setGeometry(100, 50, 20, 1300)#----------------------------------------------IMPLEMENT TO READ VALUES FROM PLAYERS WINDOW


		# Add a scene for drawing 2d objects------------------------------------------------------------REMOVE
		#self.scene = QtWidgets.QGraphicsScene()
		#self.scene.setSceneRect(0, 0, 2736, 1824)
		#self.scene.setSceneRect(0, 0, 1900, 1050)

		# Add a view for showing the scene------------------------------------------------------------REMOVE
		"""self.view = QtWidgets.QGraphicsView(self.scene, self)
		self.view.adjustSize()
		self.view.show()"""
		#self.vertical_board.addWidget(self.view)


	def show_high_scores(self):
		self.scene.removeItem(self.menu_text)				# Remove menu's text field fron scene
		self.scene.removeItem(self.play_item)				# Remove Play text button from scene
		self.scene.removeItem(self.high_scores_item)		# Remove High Scores text button from scene
		
		headers = ["Easy", "Medium", "Hard"]
		x = 20
		
		for header in headers:
			text_item = TextItem(header, 30, x, 200)
			self.high_scores_text_items.append(text_item)
			self.scene.addItem(text_item)
			x += 600

		font_size = 15
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