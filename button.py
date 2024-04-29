
from UI import *

class Button:
    def __init__(self, name, pos, cost):
        self.surface = pygame.surface.Surface((200, 50))
        self.surface.fill("red")
        self.rect = self.surface.get_rect(center=pos)
        self.text = button_font.render(name, 0, "white")
        self.cost = cost


    def draw(self):
        SCREEN.blit(self.surface, self.rect)
        SCREEN.blit(self.text, self.rect.topleft)

    def checkClick(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False
    def update(self):
        self.draw()
