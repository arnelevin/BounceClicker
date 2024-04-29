
from UI import *
from ball import Ball
from player import Player
from upgrades import Upgrades
from button import Button

class Game:
    def __init__(self):

        self.clock = pygame.time.Clock()


        self.run = True
        self.shopping = True
        self.leveling = True

        self.upgrades = Upgrades()

        self.player = Player((pygame.mouse.get_pos()[0], HEIGHT - 40))

        self.money = 0
        self.balls = []


        self.ball_cooldown = self.upgrades.ball_cooldown
        self.cooldown_time = 0

        self.spawn_amount = self.upgrades.spawn_amount

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

        SCREEN.fill("green")

        exit_button = Button("Exit", (WIDTH - 200, 50), 0)
        exit_button.update()
        if exit_button.checkClick():
            self.shopping = False
            self.leveling = True


        health_button = Button("Health", (300, 300), 5)
        health_button.update()

        if health_button.checkClick() and self.money >= health_button.cost:
            self.money -= health_button.cost
            self.upgrades.add_BallHealth(1)

        cooldown_button = Button("Cooldown", (500, 300), 10)
        cooldown_button.update()

        if cooldown_button.checkClick() and self.money >= cooldown_button.cost:
            self.money -= cooldown_button.cost
            self.upgrades.decrease_BallCooldown(1000)
            self.ball_cooldown = self.upgrades.ball_cooldown

        cooldown_button = Button("Cooldown", (500, 300), 10)
        cooldown_button.update()

        if cooldown_button.checkClick() and self.money >= cooldown_button.cost:
            self.money -= cooldown_button.cost
            self.upgrades.decrease_BallCooldown(1000)
            self.ball_cooldown = self.upgrades.ball_cooldown

        speed_button = Button("Speed", (50, 300), 5)
        speed_button.update()

        if speed_button.checkClick() and self.money >= speed_button.cost:
            self.money -= speed_button.cost
            self.upgrades.add_Speed(1)
            self.player.speed = self.upgrades.player_speed

        amount_button = Button("Speed", (50, 100), 15)
        amount_button.update()

        if amount_button.checkClick() and self.money >= amount_button.cost:
            self.money -= amount_button.cost
            self.upgrades.increase_Spawn(1)
            self.spawn_amount= self.upgrades.spawn_amount

        pygame.display.update()

    def level(self):


        self.clock.tick(60)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        SCREEN.fill("blue")



        self.collision()
        self.addBalls()

        if pygame.key.get_pressed()[pygame.K_TAB]:
            self.shopping = True
            self.leveling = False

        self.player.update()
        for ball in self.balls:
            ball.update()

        highscore_text = highscore_font.render(f'HIGHSCORE: {self.highscore}', 0, "white")
        SCREEN.blit(highscore_text, (0, 0))

        score_text = my_font.render(f"{self.money}", 0, "white")
        SCREEN.blit(score_text, (WIDTH/2 - score_text.get_width()/2, 200))

        pygame.display.update()

    def collision(self):

        for ball in self.balls:
            if self.player.rect.colliderect(ball.rect):
                ball.rect.y = HEIGHT - ball.surface.get_height() - 40
                ball.speed_y = 0.96 * (- ball.speed_y - ball.current_gravity)
                ball.current_gravity = 0
                ball.speed_x *= 1.01
                ball.speed_y *= 1.01


                self.money += 1
                self.player.width -= 1
                ball.health -= 1
                Channel1.play(BOUNCE_SOUND)

                if ball.health <= 0:
                    self.balls.remove(ball)

            if ball.rect.y + ball.surface.get_height() >= HEIGHT:
                self.balls.remove(ball)

                self.player.width = 200
                if self.money > self.highscore:
                    highscore_file = open("highscore.txt", "w")
                    highscore_file.write(f'{self.money}')
                    highscore_file.close()
                    highscore_file = open("highscore.txt", "r")
                    self.highscore = int(highscore_file.read())
                    highscore_file.close()



    def addBalls(self):
        currentime = pygame.time.get_ticks()
        if currentime - self.cooldown_time > self.ball_cooldown:
            i = 0
            while i < self.spawn_amount:
                self.balls.append(Ball((SCREEN.get_width()/2, 200), self.upgrades.ball_health))
                i += 1
            self.cooldown_time = pygame.time.get_ticks()



game = Game()
game.gameState()