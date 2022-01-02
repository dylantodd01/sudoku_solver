import sys, pygame
from button import Button
from output_text import OutputText

class Gui:

	def __init__(self):

		pygame.init()
		self.screen_size = (650, 720)
		self.background_colour = (230,250,250)
		self.screen = pygame.display.set_mode(self.screen_size)
		self.screen.fill(self.background_colour)
		self.screen_update_speed = 0.000 # Number of seconds between updates

		pygame.display.set_caption('Sudoku Solver')
		self.icon = pygame.image.load('sudoku_icon.png')
		pygame.display.set_icon(self.icon)
		self.font = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuilight', 46, bold=True)

		self.solve_button = Button(self, 'Solve')
		self.text = OutputText(self.screen)


	def update_screen(self, board, current_entry, backtracked, solved, clicked=False, cell_loc=(-100,-100)):
		self.screen.fill(self.background_colour)
		self.draw_grid()
		self.populate_grid(board)
		self.colour_current_entry(current_entry, backtracked)
		self.solve_button.draw_button(clicked)
		self.check_events()
		if cell_loc[0] < 9:
			self.colour_cell(cell_loc)
        
		if solved:
			self.output_solved_text()

		pygame.display.flip()


	def check_events(self, play=True):
		"""Solve when the user clicks the solve button"""
		for event in pygame.event.get():

			if event.type == pygame.KEYDOWN and play == False:
				try:
					if event.unicode == '0':
						return 'zero'
					number = int(event.unicode)
					return number
				except:
					pass

			if event.type == pygame.MOUSEBUTTONDOWN and play == False:
				mouse_pos = pygame.mouse.get_pos()
				button_clicked = self.solve_button.rect.collidepoint(mouse_pos)
				if button_clicked:
					return 'play'

			if event.type == pygame.QUIT:
				sys.exit()



	def draw_grid(self):
		self.screen.fill(self.background_colour)
		colour = (40, 40, 40)
		pygame.draw.rect(self.screen, colour, pygame.Rect(10, 10, 630, 630),  True)
		for i in range(1,9):
			line_thickness = 3 if i%3 == 0 else 1
			pygame.draw.rect(self.screen, colour, pygame.Rect((10+i*70), 10, line_thickness, 630))
			pygame.draw.rect(self.screen, colour, pygame.Rect(10, (10+i*70), 630, line_thickness))


	def populate_grid(self, grid):
		for r, row in enumerate(grid):
			for c, number in enumerate(row):
				loc = (45+70*c, 45+70*r)
				number = str(number) if number != 0 else ''
				self.text.draw_text(str(number), loc)

	def colour_cell(self, cell_loc):
		r, c = cell_loc
		r = 11 + r * 70
		c = 11 + c * 70

		green = (100, 230, 100)
		pygame.draw.rect(self.screen, green, pygame.Rect(c, r, 69, 69))



	def colour_current_entry(self, current_entry, backtracked):
		colour = (0,190,0) if not backtracked else (200,0,0)
		number = current_entry[0]
		loc = (45+70*current_entry[2], 45+70*current_entry[1])
		self.text.draw_text(str(number), loc, colour)


	def output_solved_text(self):
		self.text.draw_text('Solved!', (325, 675))

	def input_number(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				print(event.unicode)




		        
 
