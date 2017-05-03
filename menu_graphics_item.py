from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap

class MenuGraphicsItem(QtWidgets.QGraphicsPixmapItem):

	def __init__(self, GUI, file_path, x, y, name):
		# Call init of the parent object
		super(MenuGraphicsItem, self).__init__()

		self.GUI = GUI
		self.name = name
		
		self.setPixmap(QPixmap(file_path))
		self.setPos(x - (self.boundingRect().width() / 2), y - (self.boundingRect().height() / 2))

		#self.setOffset(self.boundingRect().width() / 2, self.boundingRect().height() / 2)


	def mousePressEvent(self, event):
		if self.name == "Play":
			self.GUI.play()
		elif self.name == "High Scores":
			self.GUI.show_high_scores()
		elif self.name == "Main Menu":
			self.GUI.main_menu()