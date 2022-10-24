from turtle import *
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class TurtleManager:
    def __init__(self):
        self.all_tur=[]
        self.tur_speed=STARTING_MOVE_DISTANCE

    def create_tur(self):
        random_chance=random.randint(1,6) #creates turtles when odds match
        if random_chance==1:
            new_tur= Turtle()
            new_tur.penup()
            new_tur.shapesize(stretch_wid=1.5, stretch_len=1.5)
            new_tur.setheading(270)
            new_tur.color(random.choice(COLORS))
            new_tur.shape("turtle")
            random_x= random.randint(-250, 250)
            new_tur.goto(random_x, 320)
            self.all_tur.append(new_tur)

    def move_tur(self): 
        for tur in self.all_tur:
            tur.forward(self.tur_speed)

    def level_up(self): 
        self.tur_speed+=MOVE_INCREMENT
