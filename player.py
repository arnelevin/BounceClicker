from UI import *


class Player:
    def __init__(self, pos):
        self.width = 200
        self.surface = pygame.surface.Surface((self.width, 15))
        self.surface.fill("red")
        self.rect = self.surface.get_rect(center = pos)

    def move(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]


    def draw(self):
        SCREEN.blit(self.surface, self.rect)

    def update(self):
        self.move()
        self.draw()
        self.surface = pygame.surface.Surface((self.width, 15))
        self.surface.fill("red")
        self.rect = self.surface.get_rect(center = (pygame.mouse.get_pos()[0], HEIGHT-40 ))