from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap

class TowerGraphicsItem(QtWidgets.QGraphicsPixmapItem):

	def __init__(self, tower, square_size):
		# Call init of the parent object
		super(TowerGraphicsItem, self).__init__()

		self.tower = tower
		self.square_size = square_size
		self.is_tower_base = False


		if self.tower.is_building():
			self.setPixmap(QPixmap("images/" + self.tower.get_base_image()))
			self.is_tower_base = True
			self.is_built = False
		else:
			self.setPixmap(QPixmap("images/" + self.tower.get_image()))

		self.width = self.pixmap().width()
		self.height = self.pixmap().height()

		self.setTransformOriginPoint(self.width / 2, self.height / 2)

		self.update_graphics()

	def get_tower(self):
		return self.tower

	def update_graphics(self):
		self.updatePosition()
		if not self.is_tower_base:
			self.updateRotation()

	def build(self):
		if not self.is_built:
			if not self.tower.is_building():
				self.is_built = True
				return True

	def updatePosition(self):
		location = self.tower.get_location()
		self.setPos(location[0] - (self.width / 2), location[1] - (self.height / 2))
		#self.setPos(location[0] - ((self.width - self.square_size) / 2), location[1] - ((self.height - self.square_size) / 2))


	def updateRotation(self):
		rotation = self.tower.get_degrees()

		if rotation != None:
			self.setRotation(self.tower.get_degrees())

	def mousePressEvent(self, event):
		self.tower.change_target_type()