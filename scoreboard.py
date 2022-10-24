from turtle import *

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle): #because everything display unit is a turtle
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(-280,270)
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def increase(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)