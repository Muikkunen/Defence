from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap

class EnemyGraphicsItem(QtWidgets.QGraphicsPixmapItem):

	def __init__(self, enemy, square_size):
		# Call init of the parent object
		super(EnemyGraphicsItem, self).__init__()

		self.enemy = enemy
		self.square_size = square_size

		if self.enemy.get_type() == "KILLER1":
			self.setPixmap(QPixmap("images/Enemy_1.png"))
		elif self.enemy.get_type() == "KILLER2":
			self.setPixmap(QPixmap("images/Enemy_2.png"))


		self.width = self.pixmap().width()
		self.height = self.pixmap().height()

		self.setTransformOriginPoint(self.width / 2, self.height / 2)

		self.update_graphics()

	def get_enemy(self):
		return self.enemy


	def update_graphics(self):
		self.updatePosition()
		self.updateRotation()

	def updatePosition(self):
		location = self.enemy.get_location()
		self.setPos(location[0] - ((self.width - self.square_size) / 2), location[1] - ((self.height - self.square_size) / 2))


	def updateRotation(self):
		rotation = self.enemy.get_degrees()

		if rotation != None:
			self.setRotation(self.enemy.get_degrees())