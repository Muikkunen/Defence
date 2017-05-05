from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap

class MenuGraphicsItem(QtWidgets.QGraphicsPixmapItem):

	def __init__(self, GUI, file_path, x, y, name):
		# Call init of the parent object
		super(MenuGraphicsItem, self).__init__()

		self.GUI = GUI
		self.name = name
		
		self.pixmap = QPixmap(file_path)
		self.setPixmap(self.pixmap)
		self.setPos(x - (self.boundingRect().width() / 2), y - (self.boundingRect().height() / 2))

		#self.setOffset(self.boundingRect().width() / 2, self.boundingRect().height() / 2)


	def mousePressEvent(self, event):
		if self.name == "Play":
			self.GUI.choose_difficulty()
		elif self.name == "High Scores":
			self.GUI.show_high_scores()
		elif self.name == "Main Menu":
			self.GUI.main_menu()
		elif self.name == "Easy":
			game = self.GUI.get_game()
			board = game.get_board()
			board.set_route_points(game.routes[0][1], game.routes[0][0])
			board.add_route()
			self.GUI.play()
		elif self.name == "Medium":	
			game = self.GUI.get_game()
			board = game.get_board()
			board.set_route_points(game.routes[1][1], game.routes[1][0])
			board.add_route()
			self.GUI.play()
		elif self.name == "Hard":
			game = self.GUI.get_game()
			board = game.get_board()
			board.set_route_points(game.routes[2][1], game.routes[2][0])
			board.add_route()
			self.GUI.play()

	def height(self):
		return self.pixmap.height()