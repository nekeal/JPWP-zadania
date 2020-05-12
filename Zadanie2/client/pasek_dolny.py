#ok
import pygame
from przyciski import Przycisk,PrzyciskTekstowy
import time as t


class PasekDolny:


    def __init__(self, x, y, gra):
        self.x = x
        self.y = y
        self.SZEROKOSC = 720
        self.WYSOKOSC = 100
        self.OBRAMOWANIE = 5
        self.gra = gra
        self.czysc_button = PrzyciskTekstowy(810, 490 ,110 ,55, (128,128,128), "Czyść")
        self.gumka_button = PrzyciskTekstowy(925,490,110, 55, (128,128,128), "Gumka")
        self.flaga = True
        self.color = (0, 0, 0)

    def rysuj(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.SZEROKOSC, self.WYSOKOSC), self.OBRAMOWANIE)
        self.czysc_button.rysuj(win)
        self.gumka_button.rysuj(win)



    def obsluga_przyciskow(self):
        
        mouse = pygame.mouse.get_pos()

        if self.czysc_button.klikniecie(*mouse):
            self.gra.tablica.czyszczenie()
            self.gra.connection.send({10:[]})

        if self.gumka_button.klikniecie(*mouse):
          ### Napisz kod do zadania nr 2
            if self.color == (0, 0, 0):
                self.color = (255, 255, 255)
            else:
                self.color = (0, 0, 0)
