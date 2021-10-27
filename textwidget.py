import pygame
import random


pygame.init()
font = pygame.font.SysFont("Arial", 20)
class Label:
	''' CLASS FOR TEXT LABELS ON THE WIN SCREEN SURFACE '''
	def __init__(self, screen, text, x, y, color="white"):
		self.image = font.render(text, 1, color)
		_, _, w, h = self.image.get_rect()
		self.rect = pygame.Rect(x, y, w, h)
		self.screen = screen

	def change_text(self, newtext):
		self.image = font.render(newtext, 1, "white")

	def draw(self):
		self.screen.blit(self.image, (self.rect))


'''     when you import this module
text1 = Text(win, "Ciao a tutti", 100, 100) # out of loop
text.draw() # into the loop
'''

if __name__ == '__main__':
	# TEXT TO SHOW ON THE SCREEN AT POS 100 100
	win = pygame.display.set_mode((600, 600))
	clock = pygame.time.Clock()
	score = Label(win, "Ciao a tutti", 100, 100)

	# LOOP TO MAKE THINGS ON THE SCRREEN
	loop = 1
	while loop:
		win.fill(0) # CLEAN THE SCREEN EVERY FRAME
		# CODE TO CLOSE THE WINDOW
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop = 0
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					loop = 0
		# CODE TO SHOW TEXT EVERY FRAME
		score.draw()
		pygame.display.update()
		clock.tick(60)

	pygame.quit()