from PyQt5 import QtWidgets, QtGui, QtCore

class EnemyGraphicsItem(QtWidgets.QGraphicsPolygonItem):
	'''
	The class RobotGraphicsItem extends QGraphicsPolygonItem to link it together to the physical
	representation of a Robot. The QGraphicsPolygonItem handles the drawing, while the
	Robot knows its own location and status.

	NOTE: unfortunately the PyQt5 uses different naming conventions than the rest
	of this project. We are also overriding the mousePressEvent()-method, whose
	name cannot be changed. Therefore, this class has a different style of naming the
	method names. (for example: updatePosition() vs update_position())
	'''
	def __init__(self, enemy, square_size):
		# Call init of the parent object
		super(EnemyGraphicsItem, self).__init__()

		# Do other stuff
		self.enemy = enemy
		self.square_size = square_size
		brush = QtGui.QBrush(1) # 1 for even fill
		self.setBrush(brush)
		self.constructTriangleVertices()
		self.update_graphics()

	def constructTriangleVertices(self):

		# Create a new QPolygon object
		triangle = QtGui.QPolygonF()

		# Add the corners of a triangle to the the polygon object
		triangle.append(QtCore.QPointF(self.square_size/2, 0)) # Tip
		triangle.append(QtCore.QPointF(0, self.square_size)) # Bottom-left
		triangle.append(QtCore.QPointF(self.square_size, self.square_size)) # Bottom-right
		triangle.append(QtCore.QPointF(self.square_size/2, 0)) # Tip

		self.setPolygon(triangle)

		self.setTransformOriginPoint(self.square_size/2, self.square_size/2)

	def update_graphics(self):
		self.updatePosition()
		self.updateRotation()
		self.updateColor()

	def updatePosition(self):
		location = self.enemy.get_location()
		self.setPos(location[0], location[1])


	def updateRotation(self):
		#rotation = direction.get_degrees(self.robot.get_facing())

		self.setRotation(0)


	def updateColor(self):
		red = QtGui.QColor(255, 0, 0)
		brush = QtGui.QBrush(1)

		brush.setColor(red)
	
		self.setBrush(brush)


	"""def mousePressEvent(self, *args, **kwargs):
		self.robot.fix()"""