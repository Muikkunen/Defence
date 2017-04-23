from PyQt5 import QtWidgets, QtCore, QtGui

from enemy_graphics_item import EnemyGraphicsItem
from tower_graphics_item import TowerGraphicsItem
from missile_graphics_item import MissileGraphicsItem

class GUI(QtWidgets.QMainWindow):

	def __init__(self, game):
		super().__init__()
		self.setCentralWidget(QtWidgets.QWidget()) 			# QMainWindown must have a centralWidget to be able to add layouts
		self.horizontal = QtWidgets.QHBoxLayout() 			# Horizontal main layout
		self.centralWidget().setLayout(self.horizontal)
		self.game = game
		self.square_size = game.get_board().get_square_size()
		self.init_window()
		"""self.init_buttons()
		self.add_robot_world_grid_items()
		self.add_robot_graphics_items()
		self.update_robots()"""


		self.enemy_graphics_items = []
		self.tower_graphics_items = []
		self.missile_graphics_items = []

		
		self.add_all_graphics()
		self.update_all()

		# Set a timer to call the update function periodically
		self.timer = QtCore.QTimer()
		self.timer.start(16) # Milliseconds - 16 milliseconds to get to 60 frames per second
		self.timer.timeout.connect(self.update_all)

		


	def add_all_graphics(self):
		self.add_enemy_graphics_items()
		self.add_tower_graphics_items()
		#self.add_missiles_graphics_items()

		self.add_board_graphics()


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

	def add_board_graphics(self):
		squares = self.game.get_board().get_squares()

		for inner_list in squares:
			for square in inner_list:
				# Examine whether the specified sqúare is part of the route or not
				if square.contains() == 1:			# Square is part of the route
					continue
					print("asdfasdf")
				else:								# Square is not part of the route
					continue
					print("Piirretään myöhemmin!")


	def update_all(self):
		#print(self.game.get_board().get_missiles())
		self.update_enemies()										# Firstly the enemies move
		self.update_towers(self.game.get_board().get_towers())		# Then  the towers shoot according to their targets
		self.update_missiles(self.game.get_board().get_missiles())	# Lastly the missiles that were created as well as the previously created ones move

	def update_enemies(self):
		enemies = self.game.get_board().get_enemies()
		enemies[:] = [enemy for enemy in enemies if not enemy.move()]

		for enemy_graphics_item in self.enemy_graphics_items:
			enemy_graphics_item.update_graphics()

	def update_towers(self, towers):
		towers[:] = [tower for tower in towers if not tower.shoot()]

		for tower_graphics_item in self.tower_graphics_items:
			tower_graphics_item.update_graphics()

	def update_missiles(self, missiles):
		missiles[:] = [missile for missile in missiles if not missile.move()]

		for missile_graphics_item in self.missile_graphics_items:
			missile_graphics_item.update_graphics()


	def init_window(self):
		self.setGeometry(100, 100, 1820, 1100)#----------------------------------------------IMPLEMENT TO READ VALUES FROM PLAYERS WINDOW
		self.setWindowTitle("Defence")
		self.show()

		# Add a scene for drawing 2d objects------------------------------------------------------------REMOVE
		self.scene = QtWidgets.QGraphicsScene()
		self.scene.setSceneRect(0, 0, 1720, 1000)

		# Add a view for showing the scene------------------------------------------------------------REMOVE
		self.view = QtWidgets.QGraphicsView(self.scene, self)
		self.view.adjustSize()
		self.view.show()
		self.horizontal.addWidget(self.view)