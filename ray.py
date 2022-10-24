from turtle import *
import random
from player import *

COLOR = "red"
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class RayManager:
    def __init__(self):
        self.all_ray=[]
        self.new_rays=[]
        self.flag=1

    def create_ray(self):
        self.new_rays.clear()
        if self.flag==1:

            new_lray= Turtle()
            new_lray.penup()
            new_lray.setheading(90)
            new_lray.left(45)
            new_lray.color(COLOR)
            new_lray.shape("square")
            new_lray.shapesize(stretch_wid=0.3, stretch_len=3)
            self.all_ray.append(new_lray)
            self.new_rays.append(new_lray)

            new_ray= Turtle()
            new_ray.penup()
            new_ray.setheading(90)
            new_ray.color(COLOR)
            new_ray.shape("square")
            new_ray.shapesize(stretch_wid=0.3, stretch_len=3)
            self.all_ray.append(new_ray)
            self.new_rays.append(new_ray)

            new_rray= Turtle()
            new_rray.penup()
            new_rray.setheading(90)
            new_rray.right(45)
            new_rray.color(COLOR)
            new_rray.shape("square")
            new_rray.shapesize(stretch_wid=0.3, stretch_len=3)
            self.all_ray.append(new_rray)
            self.new_rays.append(new_rray)

        if self.flag!=8:
            self.flag+=1
        else:
            self.flag=1

    def shift_ray(self,x,y):
        for ray in self.new_rays:
            ray.penup()
            ray.goto(x,y+20)

    def move_ray(self):
        for ray in self.all_ray:
            ray.forward(20)
        
    def go_up(self):
        for ray in self.all_ray:
            ray.goto(ray.xcor(), ray.ycor()+25)

    def go_down(self):
        for ray in self.all_ray:
            ray.goto(ray.xcor(), ray.ycor()-25)

    def go_right(self):
        for ray in self.all_ray:
            ray.goto(ray.xcor()+25, ray.ycor())
        
    def go_left(self):
        for ray in self.all_ray:
            ray.goto(ray.xcor()-25, ray.ycor())