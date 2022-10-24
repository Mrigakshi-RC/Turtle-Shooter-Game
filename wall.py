from turtle import *

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_wid=28, stretch_len=0.1)
        self.penup()
        self.goto(0,-310)
        self.setheading(90)