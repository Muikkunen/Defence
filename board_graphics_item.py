from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap

class BoardGraphicsItem(QtWidgets.QGraphicsPixmapItem):

	def __init__(self, difficulty, type, placement, square_size):
		# Call init of the parent object
		super(BoardGraphicsItem, self).__init__()

		self.type = type

		if self.type == "ROUTE":
			self.setPixmap(QPixmap("images/" + difficulty + "/Route.png"))
		elif self.type == "ROUTE_UP":
			self.setPixmap(QPixmap("images/" + difficulty + "/Route_up.png"))
		elif self.type == "ROUTE_DOWN":
			self.setPixmap(QPixmap("images/" + difficulty + "/Route_down.png"))
		elif self.type == "ROUTE_LEFT":
			self.setPixmap(QPixmap("images/" + difficulty + "/Route_left.png"))
		elif self.type == "ROUTE_RIGHT":
			self.setPixmap(QPixmap("images/" + difficulty + "/Route_right.png"))
		elif self.type == "ROUTE_INNER_NORTH_EAST":
			self.setPixmap(QPixmap("images/" + difficulty + "/Route_inner_north_east"))
		elif self.type == "ROUTE_INNER_NORTH_WEST":
			self.setPixmap(QPixmap("images/" + difficulty + "/Route_inner_north_west"))
		elif self.type == "ROUTE_INNER_SOUTH_EAST":
			self.setPixmap(QPixmap("images/" + difficulty + "/Route_inner_south_east"))
		elif self.type == "ROUTE_INNER_SOUTH_WEST":
			self.setPixmap(QPixmap("images/" + difficulty + "/Route_inner_south_west"))
		elif self.type == "ROUTE_OUTER_NORTH_EAST":
			self.setPixmap(QPixmap("images/" + difficulty + "/Route_outer_north_east"))
		elif self.type == "ROUTE_OUTER_NORTH_WEST":
			self.setPixmap(QPixmap("images/" + difficulty + "/Route_outer_north_west"))
		elif self.type == "ROUTE_OUTER_SOUTH_EAST":
			self.setPixmap(QPixmap("images/" + difficulty + "/Route_outer_south_east"))
		elif self.type == "ROUTE_OUTER_SOUTH_WEST":
			self.setPixmap(QPixmap("images/" + difficulty + "/Route_outer_south_west"))
		elif self.type == "BOARD":
			self.setPixmap(QPixmap("images/" + difficulty + "/Board.png"))


		"""if self.square.get_type() == "KILLER1":
			self.setPixmap(QPixmap("images/Board_1.png"))
		elif self.square.get_type() == "KILLER2":
			self.setPixmap(QPixmap("images/Board_2.png"))"""

		location = [placement[0] * square_size, placement[1] * square_size]
		self.setPos(location[0], location[1])