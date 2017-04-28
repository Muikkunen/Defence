from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QPushButton, QGraphicsSceneMouseEvent
from PyQt5.QtGui import QBrush, QColor, QFont

from enemy_graphics_item import EnemyGraphicsItem
from tower_graphics_item import TowerGraphicsItem
from missile_graphics_item import MissileGraphicsItem
from board_graphics_item import BoardGraphicsItem
from menu_graphics_text_item import MenuGraphicsTextItem

from add_board_graphics import add_board_graphics

class GUI(QtWidgets.QMainWindow):

	def __init__(self, game):
		super().__init__()
		self.scene = QtWidgets.QGraphicsScene()
		self.scene.setSceneRect(0, 0, 1900, 1050)
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

		self.board_graphics_items = []
		self.enemy_graphics_items = []
		self.tower_graphics_items = []
		self.missile_graphics_items = []

		self.game = game
		self.square_size = game.get_board().get_square_size()

		self.main_menu()

		#self.init_buttons()

		#self.play()



	def add_all_graphics(self):
		squares = self.game.get_board().get_squares()
		self.board_graphics_items = add_board_graphics(squares, self.square_size, self.scene)


		# REMOVE THESE: -----------------------------------------------------------
		rocket = self.game.get_tower_types()["Rocket"]
		cannon = self.game.get_tower_types()["Cannon"]
		position1 = [10, 5]
		position2 = [13, 5]
		self.game.get_board().add_tower(rocket, position1)
		self.game.get_board().add_tower(cannon, position2)
		"""cannon = self.game.get_tower_types()["Cannon"]
		position = [10, 10]
		self.game.get_board().add_tower(cannon, position)"""
		#---------------------------------------------------------------


		self.add_enemy_graphics_items()
		self.add_tower_graphics_items()
		#self.add_missiles_graphics_items()





	def add_enemy_graphics_items(self):
		enemies = self.game.get_board().get_enemies()

		for enemy in enemies:
			enemy_graphics_item = EnemyGraphicsItem(enemy, self.game.get_board().get_square_size())
			self.enemy_graphics_items.append(enemy_graphics_item)
			self.scene.addItem(enemy_graphics_item)

	def add_tower_graphics_items(self):
		towers = self.game.get_board().get_towers()

		for tower in towers:
			tower_graphics_item = TowerGraphicsItem(tower, self.game.get_board().get_square_size())
			self.tower_graphics_items.append(tower_graphics_item)
			self.scene.addItem(tower_graphics_item)



	def update_all(self):
		self.update_enemies(self.game.get_board().get_enemies())	# Firstly the enemies move
		self.update_towers(self.game.get_board().get_towers())		# Then  the towers shoot according to their targets
		self.update_missiles(self.game.get_board().get_missiles())	# Lastly the missiles that were created as well as the previously created ones move

	def update_enemies(self, enemies):
		# ADD WAVE HERE TO CHECK THAT NEW ENEMIES GET GRAPHICS ITEMS AND TO GET THE GAME LOGIC TO WORK

		enemies[:] = [enemy for enemy in enemies if not enemy.is_dead()] 	# Check which enemies are dead
		enemies[:] = [enemy for enemy in enemies if not enemy.move()]		# Move the enemies

		#print(self.enemy_graphics_items)

		new_enemy_graphics_items = []

		for enemy_graphics_item in self.enemy_graphics_items:
			if enemy_graphics_item.get_enemy() in enemies:
				enemy_graphics_item.update_graphics()
				new_enemy_graphics_items.append(enemy_graphics_item)
			else:
				self.scene.removeItem(enemy_graphics_item)

		self.enemy_graphics_items = new_enemy_graphics_items


	def update_towers(self, towers):

		for tower in towers:
			missile = tower.shoot()
			if missile != None:
				missile_graphics_item = MissileGraphicsItem(missile, self.game.get_board().get_square_size())
				self.missile_graphics_items.append(missile_graphics_item)
				self.scene.addItem(missile_graphics_item)


		for tower_graphics_item in self.tower_graphics_items:
			tower_graphics_item.update_graphics()

	def update_missiles(self, missiles):
		missiles[:] = [missile for missile in missiles if not missile.move(self.game.get_board().get_enemies())]

		new_missile_graphics_items = []

		for missile_graphics_item in self.missile_graphics_items:
			if missile_graphics_item.get_missile() in missiles:
				missile_graphics_item.update_graphics()
				new_missile_graphics_items.append(missile_graphics_item)
			else:
				self.scene.removeItem(missile_graphics_item)

		self.missile_graphics_items = new_missile_graphics_items


	def main_menu(self):
		font = QFont("Comic Sans", 75)
		color = QColor("White")
		self.play_text_item = MenuGraphicsTextItem(self, "Play", font, color)
		self.high_scores_text_item = MenuGraphicsTextItem(self, "High Scores", font, color)

		self.play_text_item.setPos(0, 300)
		self.play_text_item.adjustSize()
		print(self.play_text_item.textWidth())
		self.high_scores_text_item.setPos(0, 600)
		self.high_scores_text_item.adjustSize()
		print(self.high_scores_text_item.textWidth())

		self.scene.addItem(self.play_text_item)
		self.scene.addItem(self.high_scores_text_item)

		#if play_text_item.mousePressEvent(event):
		#	self.play()

		#elif high_scores_text_item.mousePressEvent():
		#	self.show_high_scores()


	def play(self):
		self.scene.removeItem(self.play_text_item)			# Remove Play text button from scene
		self.scene.removeItem(self.high_scores_text_item)	# Remove High Scores text button from scene

		self.add_all_graphics()
		self.update_all()

		# Set a timer to call the update function periodically
		self.timer = QtCore.QTimer()
		self.timer.start(16) # Milliseconds - 16 milliseconds to get to 60 frames per second
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


	#def show_high_scores():
