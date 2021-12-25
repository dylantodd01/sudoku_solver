import sys, pygame
from button import Button

class Gui:

	def __init__(self):

		pygame.init()
		self.screen_size = (650, 720)
		self.background_colour = (230,250,250)
		self.screen = pygame.display.set_mode(self.screen_size)
		self.screen.fill(self.background_colour)
		self.screen_update_speed = 0.01 # Number of seconds between updates

		pygame.display.set_caption('Suduko Solver')
		self.icon = pygame.image.load('suduko_icon.png')
		pygame.display.set_icon(self.icon)
		self.font = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuilight', 46, bold=True)

		self.solve_button = Button(self, 'Solve')


	def update_screen(self, board, current_entry, backtracked, solved, clicked=False):
		self.screen.fill(self.background_colour)
		self.draw_grid()
		self.populate_grid(board)
		self.colour_current_entry(current_entry, backtracked)
		self.solve_button.draw_button(clicked)
		self.check_quit()
        
		if solved:
			self.output_solved_text()

		pygame.display.flip()


	def check_play_button(self):
		"""Solve when the user clicks the solve button"""
		for event in pygame.event.get():
			self.check_quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				button_clicked = self.solve_button.rect.collidepoint(mouse_pos)
				if button_clicked:
					return True

	def check_quit(self):
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sys.exit()


	def draw_grid(self):
		self.screen.fill(self.background_colour)
		colour = (40, 40, 40)
		pygame.draw.rect(self.screen, colour, pygame.Rect(10, 10, 630, 630),  1)
		for i in range(1,9):
			line_thickness = 3 if i%3 == 0 else 1
			pygame.draw.rect(self.screen, colour, pygame.Rect((10+i*70), 10, line_thickness, 630))
			pygame.draw.rect(self.screen, colour, pygame.Rect(10, (10+i*70), 630, line_thickness))


	def draw_number(self, loc, number, colour):
		text = self.font.render(number, True, colour)
		text_rect = text.get_rect()
		text_rect.center = (loc)
		self.screen.blit(text, text_rect)


	def populate_grid(self, grid):
		black = (0,0,0)
		for r, row in enumerate(grid):
			for c, number in enumerate(row):
				loc = (45+70*c, 45+70*r)
				number = str(number) if number != 0 else ''
				self.draw_number(loc, str(number), black)


	def colour_current_entry(self, current_entry, backtracked):
		colour = (0,190,0) if not backtracked else (200,0,0)
		number = current_entry[0]
		loc = (45+70*current_entry[2], 45+70*current_entry[1])
		self.draw_number(loc, str(number), colour)


	def output_solved_text(self):
		font = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuilight', 46)
		text = font.render('Solved!', True, (0, 0, 0))
		text_rect = text.get_rect()
		text_rect.center = (325, 675)
		self.screen.blit(text, text_rect)



		        
 
