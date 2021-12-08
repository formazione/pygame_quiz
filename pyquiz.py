import pygame
import pygame.gfxdraw
import sys
import time
import random
from textwidget import Text


pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
buttons = pygame.sprite.Group()
num = 1
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
        if self.style == 1:
            self.check_collision()
            self.render()
        else:
            self.check_collision()

    def click(self):
        ''' checks if you click on the button and makes the call to the action just one time'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                print("The answer is:'" + self.text + "'")
                self.command()
                self.pressed = 0
            if pygame.mouse.get_pressed() == (0,0,0):
                self.pressed = 1




# FUNCTIONS for the buttons on click
# I used this convention ... on_+text of the button

def on_click():
    print("Click on one answer")

def on_run():
    print("Ciao bello questo è RUN")

def on_save():
    print("This is Save")

def on_right():
    print("Right")
    score.change_text("100")
    forward()

def on_false():
    print("Wrong")
    forward()

def forward():
    global qnum
    
    screen.fill(0)
    if qnum < len(questions):
        time.sleep(.3)
        qnum += 1
        question(qnum)



questions = [
    ["What is Italy's Capital?", ["Rome", "Paris", "Tokyo", "Madrid"]],
    ["What is France's Capital?", ["Paris", "Rome", "Tokyo", "Madrid"]],
    ["What is England's Capital?", ["London", "Rome", "Tokyo", "Madrid"]],
]


def question(qnum):
    ''' put your buttons here '''

    for sprites in buttons:
        sprites.kill()

    pos = [100, 150, 200, 250]
    random.shuffle(pos)
    # this is a label, a button with no border does nothing: command = None
    Button((0, 0), str(qnum-1), 20, "white on black",
        hover_colors="blue on orange", style=2, borderc=(0,0,0),
        command=None)

    Button((10, 10), questions[qnum-1][0], 55, "white on black",
        hover_colors="blue on orange", style=2, borderc=(0,0,0),
        command=None)

    # ______------_____ BUTTONS FOR ANSWERS _____------______ #

    Button((10, 100), "1. ", 36, "red on yellow",
        hover_colors="blue on orange", style=2, borderc=(255,255,0),
        command=None)
    Button((10, 150), "2. ", 36, "red on yellow",
        hover_colors="blue on orange", style=2, borderc=(255,255,0),
        command=None)
    Button((10, 200), "3. ", 36, "red on yellow",
        hover_colors="blue on orange", style=2, borderc=(255,255,0),
        command=None)
    Button((10, 250), "4. ", 36, "red on yellow",
        hover_colors="blue on orange", style=2, borderc=(255,255,0),
        command=None)

    Button((50, pos[0]), questions[qnum-1][1][0], 36, "red on yellow",
        hover_colors="blue on orange", style=2, borderc=(255,255,0),
        command=on_right)


    Button((50, pos[1]), questions[qnum-1][1][1], 36, "red on yellow",
        hover_colors="blue on orange", style=2, borderc=(255,255,0),
        command=on_false)

    Button((50, pos[2]), questions[qnum-1][1][2], 36, "red on yellow",
        hover_colors="blue on orange", style=2, borderc=(255,255,0),
        command=on_false)

    Button((50, pos[3]), questions[qnum-1][1][3], 36, "red on yellow",
        hover_colors="blue on orange", style=2, borderc=(255,255,0),
        command=on_false)

# ======================= this code is just for example, start the program from the main file
# in the main folder, I mean, you can also use this file only, but I prefer from the main file
# 29.8.2021
score = Text(screen, "Punteggio", 100, 300)
qnum = 1
if __name__ == '__main__':
    pygame.init()
    game_on = 0
    def loop():
        # BUTTONS ISTANCES
        global qnum


        game_on = 1
        question(qnum)
        while True:
            screen.fill(0)
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    game_on = 0
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        game_on = 0
            if game_on:
                buttons.update()
                buttons.draw(screen)
            else:
                pygame.quit()
                sys.exit()
            buttons.draw(screen)
            score.draw()
            clock.tick(60)
            pygame.display.update()
        pygame.quit()




    loop()