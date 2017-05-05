from io import StringIO
from loader_function import get_current_information, EOFReached

def add_high_score(file_name, difficulty, name, level, points):
	file = open(file_name, "r+")

	while True:
		try:
			try:
				current_information = get_current_information(file)
				if current_information[0] == difficulty:
						
					lines_read = 0

					while True:
						last_position = file.tell()
						current_information = get_current_information(file)
					

						if points > int(current_information[2]):
							file.seek(last_position)

							lines = file.read()

							file.seek(last_position)
							characters = len(name)
							spaces = " " * (16 - characters)
							name = name + spaces
							file.writelines(name + str(level) + "\t\t" + str(points) + "\n")
							break

						lines_read += 1

					#print(lines)
					for line in lines:
						file.writelines(line)

					break
			except IndexError:
				print("Player's points are not enough to get to high scores")
				file.close()
				break

		except EOFReached:
			print("File completely read")
			file.close()
			break

	file.close()