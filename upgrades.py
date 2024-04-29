from UI import *


class Upgrades:
    def __init__(self):
        self.ball_health = 1
        self.ball_cooldown = 5000
        self.spawn_amount = 1


        self.player_speed = 5

    def add_BallHealth(self, number):
        self.ball_health += number

    def decrease_BallCooldown(self, number):
        self.ball_cooldown -= number

    def add_Speed(self, number):
        self.player_speed += number

    def increase_Spawn(self, number):
        self.spawn_amount += number

