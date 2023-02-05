from turtle import Turtle
import time
UP = ("W", "Up")
DOWN = ("D", "Down")
PAD_UP = 90
PAD_DOWN = 270
LEFT_START_POS = [(-380, 0), (-380, 20), (-380, -20), (-380, 40), (-380, -40)]
RIGHT_START_POS = [(380, 0), (380, 20), (380, -20), (380, 40), (380, -40)]


class Paddle(Turtle):

    def __init__(self, start_pos):
        self.blocks = None
        self.direction = start_pos
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.goto(start_pos)

    def add_block(self, position):
        new_block = Turtle("square")
        new_block.color("white")
        new_block.speed("fastest")
        new_block.shapesize(stretch_len=120, stretch_wid=20)
        new_block.penup()
        new_block.goto(position)
        self.blocks.append(new_block)

    def paddle_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def paddle_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

    def paddle_move(self, direction):
        if direction == UP:
            self.paddle_up()
        elif direction == DOWN:
            self.paddle_down()

    def flash(self, screen):
        self.hideturtle()
        screen.update()
        time.sleep(0.1)
        self.showturtle()
