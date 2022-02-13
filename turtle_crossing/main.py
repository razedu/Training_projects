import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
score=Scoreboard()
cars=CarManager()


screen.listen()
screen.onkey(player.move_up,"Up")
screen.onkey(player.move_down,"Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()
    cars.add_car()
    if player.finish():
        score.score_up()
        cars.incres_move()

    for car in cars.cars:
        if car.distance(player)<20:
            score.game_over()
            game_is_on=False

screen.exitonclick()



