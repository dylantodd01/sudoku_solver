import pygame

class Button:

	def __init__(self, gui, msg):
		"""Initialise button attributes"""
		self.screen = gui.screen

		#Set the dimensions and properties of the button
		self.size = (160, 55)
		self.unpressed_button_colour = (40, 40, 40)
		self.pressed_button_colour = (40, 150, 40)
		self.button_position = (110, 680)
		self.text_colour = (255, 255, 255)
		self.font = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuilight', 40)

		#Build the button's rect object and centre it
		self.rect = pygame.Rect((0, 0), self.size)
		self.rect.center = self.button_position

		#Prepping the button
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Turn msg into a rendered image and centre text on the button"""
		self.msg_image = self.font.render(msg, True, self.text_colour)#, self.button_colour)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center


	def draw_button(self, clicked):
		"""Draw blank button then draw message"""
		button_colour = self.pressed_button_colour if clicked else self.unpressed_button_colour
		self.screen.fill(button_colour, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)