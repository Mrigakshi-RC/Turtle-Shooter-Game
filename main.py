import time
from turtle import Screen
from player import Player
from enemy_manager import TurtleManager
from scoreboard import Scoreboard
from ray import RayManager
from wall import *
from scoreboard import*

deter_score=10

screen = Screen()
screen.setup(width=600, height=650)
screen.tracer(0) #with this, we dont have to the initial setup of screen and the placing of various elements.

player=Player()
enemies=TurtleManager()
rays=RayManager()
wall=Wall()
score=Scoreboard()

def perform_up():
    player.go_up()
    rays.go_up()

def perform_down():
    player.go_down()
    rays.go_down()

def perform_left():
    player.go_left()
    rays.go_left()

def perform_right():
    player.go_right()
    rays.go_right()


screen.listen()
screen.onkey(perform_up, "Up")
screen.onkey(perform_right, "Right")
screen.onkey(perform_left, "Left")
screen.onkey(perform_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update() #keeps each frame for 0.1 secs and updates to another frame after that

    enemies.create_tur()
    enemies.move_tur()


    rays.create_ray()
    rays.shift_ray(player.xcor(),player.ycor()) #makes the rays originate near the body of the player
    rays.move_ray()

    for ray in rays.all_ray:
        for tur in enemies.all_tur:
            if tur.distance(ray)<20: #diminishes the enemy turtle hit by the ray
                tur.ht()
                enemies.all_tur.remove(tur)
                score.increase()
                

    for tur in enemies.all_tur: #when any turtle manages to get past the wall
        if tur.ycor()<-300:
            score.game_over()
            game_is_on=False

    if score.score==deter_score: #levelling up
        enemies.level_up()
        deter_score+=10



screen.exitonclick()
