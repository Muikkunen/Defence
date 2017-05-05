from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap

class BuildTowerGraphicsItem(QtWidgets.QGraphicsPixmapItem):

	def __init__(self, tower, x, y, square_size, GUI):
		# Call init of the parent object
		super(BuildTowerGraphicsItem, self).__init__()

		self.tower = tower
		self.square_size = square_size
		self.GUI = GUI
		self.building = False

		self.setPixmap(QPixmap("images/" + self.tower[6]))

		self.width = self.pixmap().width()
		self.height = self.pixmap().height()
		self.setTransformOriginPoint(self.width / 2, self.height / 2)
		self.setPos(x - ((self.width - self.square_size) / 2), y - ((self.height - self.square_size) / 2))

	def get_tower(self):
		return self.tower

	def set_building(self, boolean):
		self.building = boolean

	def mousePressEvent(self, event):
		if self.building:
			return
		game = self.GUI.get_game()
		if game.get_money() >= self.tower[5]:
			game.buy(self.tower[5])
			self.GUI.add_building_slots(self.tower[0])