class board:
	def __init__(self, width=8, height=8):
		self.width = width
        	self.height = height
        	self.matrix = [[None for _ in range(width)] for _ in range(height)]

	def place_piece(self, piece, x ,y):
		pass
	def display_board(self):
		pass    
 __name__ == "__main__":
	print("Here in main")
