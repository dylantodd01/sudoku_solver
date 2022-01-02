import pygame, sys

class PrepBoard:

	def __init__(self):

		# Initialising an empty board
		self.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

	def add_numbers(self):
		for row in self.board:
			for col in row:
				self.print_board()
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.unicode.isnumeric():
							self.board[row][col] = int(event.unicode)
							break
	def input_number(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				print(event.unicode)

			if event.type == pygame.QUIT:
				sys.exit()


	def print_board(self):
		for row in self.board:
			print(row)

board = PrepBoard()
board.input_number()
#board.add_numbers()
