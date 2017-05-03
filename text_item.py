from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import QSizeF


class TextItem(QGraphicsTextItem):

	def __init__(self, text, size, x, y):
		# Call init of the parent object
		super(TextItem, self).__init__()

		font = QFont("Comic Sans", size)
		color = QColor("White")

		self.setPlainText(text)
		self.setFont(font)
		self.setDefaultTextColor(color)
		self.setPos(x, y)
		self.adjustSize()

	def set_text(self, text):
		self.setPlainText(text)