import math

import pygame

from UI import *

class Collector:
    def __init__(self, number, color):
        self.number = number * 0.6

        self.surface = pygame.surface.Surface((75, 10))
        self.surface.fill(color)
        self.rect = self.surface.get_rect(center = (WIDTH/2, HEIGHT - 15))

    def move(self):
        self.rect.centerx = WIDTH/2 +  (WIDTH/2 - self.surface.get_width()/2) * math.sin(self.number * pygame.time.get_ticks()/1000)

    def draw(self):
        SCREEN.blit(self.surface, self.rect)
    def update(self):
        self.move()
        self.draw()