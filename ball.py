from turtle import Turtle
import time
import random
START = [(10, 10), (10, -10), (-10, 10), (-10, -10)]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10

    def make(self):
        self.goto(0, 0)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_pos(self):
        self.setpos(0, 0)
        self.x_move *= -1
        time.sleep(0.3)

    def start(self):
        self.x_move *= random.choice((1, -1))
        self.y_move *= random.choice((1, -1))
