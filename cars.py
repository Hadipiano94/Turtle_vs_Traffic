from turtle import Turtle
import random

AVERAGE_SPEED = 2
CARS_NUM = 15


def reset_speed():
    global AVERAGE_SPEED
    AVERAGE_SPEED = 2


def speed_up():
    global AVERAGE_SPEED
    AVERAGE_SPEED += 1


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(["red", "blue", "green", "grey", "brown", "yellow"]))
        self.start_position = (random.randint(300, 900), - 240 + random.randint(0, int(480 // 25)) * 25)
        self.goto(self.start_position)
        self.pace = random.randint(AVERAGE_SPEED - 1, AVERAGE_SPEED + 1)
        self.setheading(180)

    def move(self):
        self.forward(self.pace)

    def reset_car(self):
        self.pace = random.randint(AVERAGE_SPEED - 1, AVERAGE_SPEED + 1)
        if self.xcor() < -400:
            self.color(random.choice(["red", "blue", "green", "grey", "brown", "yellow"]))
            self.start_position = (random.randint(300, 500), - 220 + random.randint(0, int(440 // 25)) * 25)
            self.goto(self.start_position)
