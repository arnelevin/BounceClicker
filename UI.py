import pygame
import random
pygame.init()
WIDTH = 800
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

BOUNCE_SOUND = pygame.mixer.Sound("Bounce.mp3")
BOUNCE_SOUND.set_volume(0.1)

Channel1 = pygame.mixer.Channel(0)
Channel2 = pygame.mixer.Channel(1)
Channel3 = pygame.mixer.Channel(2)
Channel4 = pygame.mixer.Channel(3)

my_font = pygame.font.SysFont("Arial", 80)
highscore_font = pygame.font.SysFont("Arial", 40)
button_font = pygame.font.SysFont("Arial", 40)
background_image = pygame.image.load("checker.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
def draw_background():
    SCREEN.blit(background_image, (0, 0))


def get_randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)