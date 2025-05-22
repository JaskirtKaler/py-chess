import sys
from PyQt5.QtWidgets import QApplication
from gui import MainMenu # Import MainMenu from gui.py

class ChessPiece:
	def __init__(self, color, piece_type):
		self.color = color
		self.piece_type = piece_type

	def __str__(self):
		return f"{self.color} {self.piece_type}"

class GameBoard:
	def __init__(self, width=8, height=8):
		self.width = width
		self.height = height
		self.matrix = [[None for _ in range(width)] for _ in range(height)]

	def place_piece(self, piece, x ,y):
		if 0 <= x < self.width and 0 <= y < self.height:
			self.matrix[y][x] = piece 

	def display_board(self): # This is a console display method, will be unused by GUI
		for row in self.matrix:
			row_display = []
			for cell in row:
				if cell is None:
					row_display.append("---")
				else:
					row_display.append(str(cell))
			print(" ".join(row_display))

if __name__ == "__main__":
	app = QApplication(sys.argv)
	main_menu = MainMenu()
	main_menu.show_menu() 
	sys.exit(app.exec_())
