from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QPushButton, QGraphicsSceneMouseEvent

class MenuGraphicsTextItem(QtWidgets.QGraphicsTextItem):

	def __init__(self, GUI, text, font, color):
		# Call init of the parent object
		super(MenuGraphicsTextItem, self).__init__()

		self.GUI = GUI
		self.setPlainText(text)
		self.setFont(font)
		self.setDefaultTextColor(color)

	def mousePressEvent(self, event):
		if self.toPlainText() == "Play":
			self.GUI.play()
		elif self.toPlainText() == "High Scores":
			print("TOTEUTA")