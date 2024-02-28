from UI import *


class Player:
    def __init__(self, pos):
        self.width = 200
        self.speed = 5
        self.surface = pygame.surface.Surface((self.width, 15))
        self.surface.fill("red")
        self.rect = self.surface.get_rect(center = pos)

    def move(self):
        if pygame.key.get_pressed()[pygame.K_a]:
            self.rect.x -= self.speed
        if pygame.key.get_pressed()[pygame.K_d]:
            self.rect.x += self.speed


    def draw(self):
        SCREEN.blit(self.surface, self.rect)

    def update(self):
        self.move()
        self.draw()
        self.surface = pygame.surface.Surface((self.width, 15))
        self.surface.fill("red")
        self.rect = self.surface.get_rect(center = self.rect.center)