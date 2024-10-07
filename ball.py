from UI import *

class Ball:
    def __init__(self, pos, health):
        self.speed = 10
        self.health = health

        self.surface = pygame.surface.Surface((50, 50))

        self.rect = self.surface.get_rect(center = pos)
        self.gravity = 0.6
        self.current_gravity = 0
        self.speed_y, self.speed_x = random.randint(-10, 10), random.randint(-10, 10)
        self.color = get_randomColor()


    def draw(self):
        pygame.draw.circle(SCREEN, self.color, self.rect.center, 25)


    def move(self):
        self.rect.x += self.speed_x
        self.speeed = self.speed_y + self.current_gravity
        self.rect.y += self.speeed

    def addGravity(self):
        self.current_gravity += self.gravity





    def collision(self):



        if self.rect.y <= 0:
            self.current_gravity = - self.current_gravity
            self.speed_y = -self.speed_y

            Channel2.play(BOUNCE_SOUND)

        if self.rect.x + self.surface.get_height() >= WIDTH:
            self.speed_x = - self.speed_x
            self.speed_x *= 1.01
            self.speed_y *= 1.01

            Channel3.play(BOUNCE_SOUND)

        if self.rect.x <= 0:

            self.speed_x = - self.speed_x
            self.speed_x *= 1.01
            self.speed_y *= 1.01

            Channel4.play(BOUNCE_SOUND)


    def update(self):
        self.draw()
        self.move()

        self.collision()
        self.addGravity()
