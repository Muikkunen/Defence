from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication

#def asdf():
#	print("asdfasdfasdf")

class PlayerName(QWidget):
	
	def __init__(self, GUI):
		super().__init__()
		self.qLineEdit = QLineEdit(self)
		self.qLineEdit.move(70, 50)
		self.qLineEdit.returnPressed.connect(GUI.check_points)
		self.qLineEdit.setMaxLength(13)
		
		self.setGeometry(50, 50, 300, 200)
		self.show()

	def get_text(self):
		return self.qLineEdit.text()