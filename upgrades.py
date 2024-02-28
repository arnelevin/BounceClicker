from UI import *


class Upgrades:
    def __init__(self):
        self.ball_health = 1
        self.ball_cooldown = 5000

    def add_BallHealth(self, number):
        self.ball_health += number

    def decrease_BallCooldown(self, number):
        self.ball_cooldown -= number

