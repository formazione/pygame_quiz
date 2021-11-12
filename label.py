
import pygame



pygame.init()
def fontsize(size):
	font = pygame.font.SysFont("Arial", size)
	return font

font_default = fontsize(20)


labels = []
class Label:

	''' CLASS FOR TEXT LABELS ON THE WIN SCREEN SURFACE '''
	def __init__(self, screen, text, x, y, size=20, color="white"):
		if size != 20:
			self.font = fontsize(size)
		else:
			self.font = font_default
		self.image = self.font.render(text, 1, color)
		_, _, w, h = self.image.get_rect()
		self.rect = pygame.Rect(x, y, w, h)
		self.screen = screen
		self.text = text
		labels.append(self)

	def change_text(self, newtext, color="white"):
		self.image = self.font.render(newtext, 1, color)

	def change_font(self, font, size, color="white"):
		self.font = pygame.font.SysFont(font, size)
		self.change_text(self.text, color)

	def draw(self):
		self.screen.blit(self.image, (self.rect))


def show_labels():
	for _ in labels:
		_.draw()


'''     when you import this module
text1 = Text(win, "Ciao a tutti", 100, 100) # out of loop
text.draw() # into the loop
'''

if __name__ == '__main__':
	# TEXT TO SHOW ON THE SCREEN AT POS 100 100
	win = pygame.display.set_mode((600, 600))
	clock = pygame.time.Clock()


	Label(win, "Hello World", 100, 100, 36)
	second = Label(win, "GiovanniPython", 100, 200, 24, color="yellow")
	second.change_font("Arial", 40, "yellow")
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
		show_labels()
		pygame.display.update()
		clock.tick(60)

	pygame.quit()
