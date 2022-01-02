import pygame

class OutputText:

	BLACK = (0,0,0)

	def __init__(self, screen):

		self.font = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuilight', 46, bold=True)
		self.screen = screen
		

	def draw_text(self, text='example text', loc=(0,0), colour=BLACK):
		text = self.font.render(text, True, colour)
		text_rect = text.get_rect()
		text_rect.center = loc
		self.screen.blit(text, text_rect)