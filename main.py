import pygame.time

from UI import *
from ball import Ball
from player import Player
from upgrades import Upgrades

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

        exit_surface = pygame.surface.Surface((50, 50))
        exit_surface.fill("red")
        exit_rect = exit_surface.get_rect(center = (SCREEN.get_width() -100, 50))

        SCREEN.blit(exit_surface, exit_rect)

        if exit_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            self.shopping = False
            self.leveling = True

        add_health_surface = pygame.surface.Surface((50, 50))
        add_health_surface.fill("red")
        add_health_rect = add_health_surface.get_rect(center=(300, HEIGHT/2))

        SCREEN.blit(add_health_surface, add_health_rect)

        if add_health_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and self.money >= 5:
            self.money -= 5
            self.upgrades.add_BallHealth(1)

        decrease_cooldown_surface = pygame.surface.Surface((50, 50))
        decrease_cooldown_surface.fill("red")
        decrease_cooldown_rect = add_health_surface.get_rect(center=(400, HEIGHT / 2))

        SCREEN.blit(decrease_cooldown_surface, decrease_cooldown_rect)

        if decrease_cooldown_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and self.money >= 10:
            self.money -= 10
            self.upgrades.decrease_BallCooldown(2500)
            self.ball_cooldown = self.upgrades.ball_cooldown




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
            self.balls.append(Ball((SCREEN.get_width()/2, 200), self.upgrades.ball_health))
            self.cooldown_time = pygame.time.get_ticks()



game = Game()
game.gameState()