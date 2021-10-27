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

class Button(pygame.sprite.Sprite):
    
    def __init__(self, position, text, size,
        colors="white on blue",
        hover_colors="red on green",
        style=1,
        borderc=(255,255,255),
        command=lambda: print("No command activated for this button")):

        # the hover_colors attribute needs to be fixed
        super().__init__()
        global num


        self.text = text

        self.command = command
        # --- colors ---
        self.colors = colors
        self.original_colors = colors
        self.fg, self.bg = self.colors.split(" on ")

        if hover_colors == "red on green":
            self.hover_colors = f"{self.bg} on {self.fg}"
        else:
            self.hover_colors = hover_colors

        self.style = style
        self.borderc = borderc # for the style2
        # font
        self.font = pygame.font.SysFont("Arial", size)
        self.render(self.text)
        self.x, self.y, self.w , self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, 500, self.h)
        self.position = position
        self.pressed = 1
        # the groups with all the buttons
        buttons.add(self)

    def render(self, text):
        # we have a surface
        self.text_render = self.font.render(text, 1, self.fg)
        # memorize the surface in the image attributes
        self.image = self.text_render

    def update(self):
        self.fg, self.bg = self.colors.split(" on ")
        if self.style == 1:
            self.draw_button1()
        elif self.style == 2:
            self.draw_button2()
        if self.command != None:
            self.hover()
            self.click()

    def draw_button1(self):
        ''' draws 4 lines around the button and the background '''
        # horizontal up
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y), (self.x + self.w , self.y), 5)
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y - 2), (self.x, self.y + self.h), 5)
        # horizontal down
        pygame.draw.line(screen, (50, 50, 50), (self.x, self.y + self.h), (self.x + self.w , self.y + self.h), 5)
        pygame.draw.line(screen, (50, 50, 50), (self.x + self.w , self.y + self.h), [self.x + self.w , self.y], 5)
        # background of the button
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w , self.h))  

    def draw_button2(self):
        ''' a linear border '''
        pygame.draw.rect(screen, self.bg, (self.x - 50, self.y, 500 , self.h))
        pygame.gfxdraw.rectangle(screen, (self.x - 50, self.y, 500 , self.h), self.borderc)

    def check_collision(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            # you can change the colors when the pointer is on the button if you want
            self.colors = self.hover_colors
            # pygame.mouse.set_cursor(*pygame.cursors.diamond)
        else:
            self.colors = self.original_colors
            # pygame.mouse.set_cursor(*pygame.cursors.arrow)


    def hover(self):
        ''' checks if the mouse is over the button and changes the color if it is true '''
        # if self.style == 1:
        #     self.check_collision()
        #     # self.render()
        #     # buttons.draw()

        # else:
        self.check_collision()

    def click(self):
        ''' checks if you click on the button and makes the call to the action just one time'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                print("The answer is:'" + self.text + "'")
                self.command()
                self.pressed = 0
                time.sleep(1)
            if pygame.mouse.get_pressed() == (0,0,0):
                self.pressed = 1


'''     when you import this module
text1 = (win, "Ciao a tutti", 100, 100) # out of loop
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
