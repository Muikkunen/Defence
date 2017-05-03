from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

class ExplosionGraphicsItem(QtWidgets.QGraphicsPixmapItem):

	def __init__(self, location, explosion_type, explosion_time, square_size):
		# Call init of the parent object
		super(ExplosionGraphicsItem, self).__init__()
		
		self.type = explosion_type

		#if self.type == "Rocket":
		#	self.setPixmap(QPixmap("images/Explosion_1.png"))
		if self.type == "Cannon":
			self.setPixmap(QPixmap("images/Explosion_2.png"))
		if self.type == "DoubleRocketLauncher":
			self.setPixmap(QPixmap("images/Double_rocket_launcher_explosion.png"))

		width = self.pixmap().width()
		height = self.pixmap().height()

		self.setTransformOriginPoint(width / 2, height / 2)

		self.timer = QTimer()
		self.timer.setSingleShot(True)
		self.timer.start(explosion_time)
		self.setPos(location[0]  - ((width - square_size) / 2), location[1] - ((height - square_size) / 2))

	def time_passed(self):
		return self.timer.remainingTime()