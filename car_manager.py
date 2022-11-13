from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self, start_pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.goto(start_pos)
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        car = CarManager((300, random.randint(-250, 250)))
        self.car_list.append(car)

    def move_cars(self):
        for cars in self.car_list:
            cars.forward(self.car_speed)

        # for cars in range(len(self.car_list)):
        #     self.car_list[cars].forward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
