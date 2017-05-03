from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap

class MissileGraphicsItem(QtWidgets.QGraphicsPixmapItem):

	def __init__(self, missile, square_size):
		# Call init of the parent object
		super(MissileGraphicsItem, self).__init__()
		
		self.missile = missile
		self.square_size = square_size

		self.setPixmap(QPixmap("images/" + str(self.missile.get_image())))

		"""if self.missile.get_type() == "Rocket":
			self.setPixmap(QPixmap("images/Missile_1.png"))
		elif self.missile.get_type() == "Cannon":
			self.setPixmap(QPixmap("images/Missile_2.png"))"""

		self.width = self.pixmap().width()
		self.height = self.pixmap().height()

		self.setTransformOriginPoint(self.width / 2, self.height / 2)

		self.update_graphics()


	def get_missile(self):
		return self.missile


	def update_graphics(self):
		self.updatePosition()
		self.updateRotation()

	def updatePosition(self):
		location = self.missile.get_location()
		self.setPos(location[0]  - ((self.width - self.square_size) / 2), location[1] - ((self.height - self.square_size) / 2))


	def updateRotation(self):
		rotation = self.missile.get_degrees()

		if rotation != None:
			self.setRotation(self.missile.get_degrees())