from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap

class EnemyGraphicsItem(QtWidgets.QGraphicsPixmapItem):

	def __init__(self, enemy, square_size):
		# Call init of the parent object
		super(EnemyGraphicsItem, self).__init__()

		self.enemy = enemy
		self.square_size = square_size
		self.shadow = None

		self.setPixmap(QPixmap("images/" + self.enemy.get_image()))
		
		self.width = self.pixmap().width()
		self.height = self.pixmap().height()

		if self.enemy.get_type() == "Plane" or self.enemy.get_type() == "Fighter":
			self.shadow = QGraphicsPixmapItem()
			self.shadow.setPixmap(QPixmap("images/" + self.enemy.get_shadow()))
			self.shadow.setTransformOriginPoint(self.width / 2, self.height / 2)

		self.setTransformOriginPoint(self.width / 2, self.height / 2)

		self.update_graphics()

	def get_enemy(self):
		return self.enemy

	def get_shadow(self):
		return self.shadow

	def has_shadow(self):
		if self.shadow == None:
			return False
		return True


	def update_graphics(self):
		self.updatePosition()
		self.updateRotation()
		if self.enemy.get_type() == "Plane" or self.enemy.get_type() == "Fighter":
			self.update_shadow()

	def updatePosition(self):
		location = self.enemy.get_location()
		self.setPos(location[0] - ((self.width - self.square_size) / 2), location[1] - ((self.height - self.square_size) / 2))


	def updateRotation(self):
		rotation = self.enemy.get_degrees()

		if rotation != None:
			self.setRotation(self.enemy.get_degrees())

	def update_shadow(self):
		self.shadow.setPos(self.pos().x() - self.width / 2, self.pos().y() - self.height / 2)
		self.shadow.setRotation(self.rotation())