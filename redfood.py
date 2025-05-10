from turtle import Turtle
import random
import time

class Redfood(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        self.hideturtle()  # Hide initially
        self.active = False



    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.showturtle()
        self.active = True

    def hide(self):
        self.hideturtle()
        self.active = False







