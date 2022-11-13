import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Objects
player = Player()
car = CarManager((300, random.randint(-250, 250)))
car.hideturtle()
scoreboard = Scoreboard()

# Game controls
screen.listen()
screen.onkey(player.move_up, "Up")

# Variables
car_number = 0
game_is_on = True

# Game
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_number += 1
    car.move_cars()

    # Checks if a new car should be made
    if car_number == 6:
        car.make_car()
        car_number = 0

    # Checks if player crashes with a car
    for cars in car.car_list:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Checks if player is at finish line and if so takes them to next level
    if player.ycor() >= 280:
        player.go_to_start()
        car.speed_up()
        scoreboard.new_level()


screen.exitonclick()
