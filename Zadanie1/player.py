import pygame

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        ###############
        #KOD DO ZADANIA 1.3
        ##############

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)