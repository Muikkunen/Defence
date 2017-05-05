from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap

class BuildingSlotGraphicsItem(QtWidgets.QGraphicsPixmapItem):

	def __init__(self, tower_type, x, y, square_size, image, GUI):
		# Call init of the parent object
		super(BuildingSlotGraphicsItem, self).__init__()

		self.tower_type = tower_type
		self.GUI = GUI
		self.x = x
		self.y = y
		self.square_size = square_size

		self.setPixmap(QPixmap("images/" + image))
		self.setPos(self.x * self.square_size, self.y * self.square_size)

	def get_tower_type(self):
		return self.tower_type

	def mousePressEvent(self, event):
		tower_information = self.GUI.get_game().get_tower_types()[self.tower_type]
		location = [self.x, self.y]
		tower = self.GUI.get_game().get_board().add_tower(tower_information, location)
		self.GUI.add_tower_base_graphics_item(tower)