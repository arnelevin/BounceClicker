from UI import *
from collector import Collector
from button import Button

MONEY = 20

BALL_HEALTH = 1

BALL_COOLDOWN = 3000

SPAWN_AMOUNT = 1

PLAYER_SPEED = 20

COLLECTORS = []

COLLECTOR_NUMBER = 1

def exit(number):
    pass

def add_BallHealth(number):
    global BALL_HEALTH
    BALL_HEALTH += number

def decrease_BallCooldown(number):
    global  BALL_COOLDOWN
    BALL_COOLDOWN -= number

def add_Speed(number):
    global PLAYER_SPEED
    PLAYER_SPEED += number

def increase_Spawn(number):
    global SPAWN_AMOUNT
    SPAWN_AMOUNT += number

def add_collector(number):
    global COLLECTOR_NUMBER
    COLLECTORS.append(Collector(COLLECTOR_NUMBER, get_randomColor()))
    COLLECTOR_NUMBER += number

global buttons
buttons = []

health_button = Button("Health", (300, 300), 5, add_BallHealth, 1)
buttons.append(health_button)
cooldown_button = Button("Cooldown", (600, 300), 10, decrease_BallCooldown, 1000)
buttons.append(cooldown_button)
speed_button = Button("Speed", (50, 300), 5, add_Speed, 1)
buttons.append(speed_button)






