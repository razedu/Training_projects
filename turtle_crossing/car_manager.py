from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.cars=[]

    def add_car(self):
        chance=random.randint(1,6)
        if chance == 1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.xpos = 300
            new_car.ypos = random.randint(-280, 280)
            new_car.color(random.choice(COLORS))
            new_car.goto(new_car.xpos, new_car.ypos)
            new_car.setheading(180)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)


    def incres_move(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
