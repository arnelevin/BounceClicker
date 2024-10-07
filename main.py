
from UI import *
from ball import Ball
from player import Player
from upgrades import *
from button import Button
from collector import Collector
class Game:
    def __init__(self):

        self.clock = pygame.time.Clock()


        self.run = True
        self.shopping = True
        self.leveling = True



        self.player = Player((pygame.mouse.get_pos()[0], HEIGHT - 40))


        self.balls = []
        self.collectors = []
        self.money = 20


        self.cooldown_time = 0



        highscore_file = open("highscore.txt", "r")
        self.highscore = int(highscore_file.read())
        highscore_file.close()


    def gameState(self):
        while self.run:
            while self.leveling:
                self.level()
            while self.shopping:
                self.shop()
    def shop(self):

        self.clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        draw_background()



        if pygame.key.get_pressed()[pygame.K_TAB]:
            self.shopping = False
            pygame.time.wait(150)
            self.leveling = True


        for button in buttons:
            button.update()


        pygame.display.update()

    def level(self):


        self.clock.tick(60)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        draw_background()



        self.collision()
        self.addBalls()

        if pygame.key.get_pressed()[pygame.K_TAB]:
            pygame.time.wait(150)
            self.shopping = True
            self.leveling = False



        self.player.update()
        for ball in self.balls:
            ball.update()
        for collector in self.collectors:
            collector.update()

        highscore_text = highscore_font.render(f'HIGHSCORE: {self.highscore}', 0, "white")
        SCREEN.blit(highscore_text, (0, 0))

        money_text = my_font.render(f"{self.money}", 0, "blue")
        SCREEN.blit(money_text, (WIDTH/2 - money_text.get_width()/2, 200))



        pygame.display.update()

    def collision(self):
        def changeVel(ball):
            ball.rect.y = HEIGHT - ball.surface.get_height() - 40
            ball.speed_y = 0.96 * (- ball.speed_y - ball.current_gravity)
            ball.current_gravity = 0
            ball.speed_x *= 1.01
            ball.speed_y *= 1.01

        for ball in self.balls:
            if self.player.rect.colliderect(ball.rect):
                changeVel(ball)

                self.money += 1

                ball.health -= 1
                Channel1.play(BOUNCE_SOUND)

                if ball.health <= 0:
                    self.balls.remove(ball)

            if ball.rect.y >= HEIGHT:
                self.balls.remove(ball)


                if self.money > self.highscore:
                    highscore_file = open("highscore.txt", "w")
                    highscore_file.write(f'{self.money}')
                    highscore_file.close()
                    highscore_file = open("highscore.txt", "r")
                    self.highscore = int(highscore_file.read())
                    highscore_file.close()
            for collector in self.collectors:
                if collector.rect.colliderect(ball.rect):
                    changeVel(ball)

                    self.money += 1
                    ball.health -= 1

    def addBalls(self):
        currentime = pygame.time.get_ticks()
        if currentime - self.cooldown_time > BALL_COOLDOWN:
            i = 0
            while i < SPAWN_AMOUNT:
                self.balls.append(Ball((SCREEN.get_width()/2, 200), BALL_HEALTH))
                i += 1
            self.cooldown_time = pygame.time.get_ticks()




game = Game()
game.gameState()