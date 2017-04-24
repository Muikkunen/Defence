from board_graphics_item import BoardGraphicsItem

def contains(squares, x, y):
	try:
		return squares[x][y].contains()
	except IndexError:
		return 0


def add_board_graphics(squares, square_size, scene):
	board_graphics_items = []

	for i in range(len(squares)):
		for j in range(len(squares[i])):
			placement = [i, j]					# Square's location on board

			# Examine if the specified square is part of the route
			if contains(squares, i, j):			# Square is part of the route

				# Create BoardGraphicsItem
				board_graphics_item = BoardGraphicsItem("ROUTE", placement, square_size)
			
			# Examine if the square above is part of the route
			elif contains(squares, i, j - 1):
				if contains(squares, i + 1, j):
					board_graphics_item = BoardGraphicsItem("ROUTE_INNER_SOUTH_WEST", placement, square_size)
				elif contains(squares, i - 1, j):
					board_graphics_item = BoardGraphicsItem("ROUTE_INNER_SOUTH_EAST", placement, square_size)
				else:
					board_graphics_item = BoardGraphicsItem("ROUTE_UP", placement, square_size)

			# Examine if the square below is part of the route
			elif contains(squares, i, j + 1):
				if contains(squares, i + 1, j):
					board_graphics_item = BoardGraphicsItem("ROUTE_INNER_NORTH_WEST", placement, square_size)
				elif contains(squares, i - 1, j):
					board_graphics_item = BoardGraphicsItem("ROUTE_INNER_NORTH_EAST", placement, square_size)
				else:
					board_graphics_item = BoardGraphicsItem("ROUTE_DOWN", placement, square_size)

			# Examine if the square on the right is part of the route
			elif contains(squares, i + 1, j):
				board_graphics_item = BoardGraphicsItem("ROUTE_RIGHT", placement, square_size)

			# Examine if the square on the left is part of the route
			elif contains(squares, i - 1, j):
				board_graphics_item = BoardGraphicsItem("ROUTE_LEFT", placement, square_size)

			# Examine if the square on the up-left corner is part of the route
			elif contains(squares, i - 1, j - 1):
				board_graphics_item = BoardGraphicsItem("ROUTE_OUTER_NORTH_WEST", placement, square_size)

			# Examine if the square on the up-right corner is part of the route
			elif contains(squares, i + 1, j - 1):
				board_graphics_item = BoardGraphicsItem("ROUTE_OUTER_NORTH_EAST", placement, square_size)

			# Examine if the square on the down-left corner is part of the route
			elif contains(squares, i - 1, j + 1):
				board_graphics_item = BoardGraphicsItem("ROUTE_OUTER_SOUTH_WEST", placement, square_size)

			# Examine if the square on the down-right corner is part of the route
			elif contains(squares, i + 1, j + 1):
				board_graphics_item = BoardGraphicsItem("ROUTE_OUTER_SOUTH_EAST", placement, square_size)

			else:
				board_graphics_item = BoardGraphicsItem("BOARD", placement, square_size)

			board_graphics_items.append(board_graphics_item)	# Add created item to the GUI's list of these items
			scene.addItem(board_graphics_item)					# Add created item to the scene

	return board_graphics_items