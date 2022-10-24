from turtle import *

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shapesize(stretch_wid=2, stretch_len=2)
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90) #giving the turtle its attributes

    def go_up(self):
        self.forward(20)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_down(self):
        self.backward(20)

