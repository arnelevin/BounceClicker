import pygame

from UI import *
from upgrades import *


class Button:

    def __init__(self, name, pos, cost, upgrade, number):
        self.name = name
        self.surface = pygame.surface.Surface((200, 50))
        self.surface.fill("red")
        self.level = 1
        self.rect = self.surface.get_rect(center=pos)
        self.text = button_font.render(f'{self.name} Lv - {self.level}', 0, "white")
        self.cost = cost
        self.upgrade = upgrade
        self.number = number





    def draw(self):
        SCREEN.blit(self.surface, self.rect)
        SCREEN.blit(self.text, self.rect.topleft)

    def action(self):
        self.upgrade(self.number)
        self.level += 1

    def checkClick(self):

        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and self.cost <= self.money:
            self.action()
            self.money -= self.cost


    def update(self):
        self.draw()
        self.text = button_font.render(f'{self.name} Lv - {self.level}', 0, "white")
        self.checkClick()



