import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill("green")
pygame.display.update()

class Rectangle():

    def __init__(self, colour, dimensions):
            self.screen = screen
            self.colour = colour
            self.dimensions = dimensions

    def draw(self):
         self.drawrect = pygame.draw.rect(self.screen, self.colour, self.dimensions)
         
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    red_rectangle = Rectangle("red", (50, 20, 150, 70))
    red_rectangle.draw()
