from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time


def l_scored():
    score.update_score("left")
    for _ in range(0, 5):
        l_paddle.flash(screen)
        screen.update()
        time.sleep(0.05)
    ball.reset_pos()
    time.sleep(0.01)
    ball.start()


def r_scored():
    score.update_score("right")
    for _ in range(0, 5):
        r_paddle.flash(screen)
        screen.update()
        time.sleep(0.05)
    ball.reset_pos()
    time.sleep(0.01)
    ball.start()


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
screen.listen()
score = Scoreboard()
score.score_setup()
l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))
ball = Ball()
ball.make()
l_points = 0
r_points = 0
sleep = 0.1
screen.onkey(fun=l_paddle.paddle_up, key="w")
screen.onkey(fun=l_paddle.paddle_down, key="s")
screen.onkey(fun=r_paddle.paddle_up, key="Up")
screen.onkey(fun=r_paddle.paddle_down, key="Down")
running = True
ball.start()
while running:
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()
    if ball.distance(l_paddle) <= 50 and ball.xcor() <= -360 or ball.distance(r_paddle) <= 50 and ball.xcor() >= 360:
        ball.bounce_x()
        sleep -= 0.01
    if ball.xcor() < -380:
        l_scored()
        sleep = 0.1
    elif ball.xcor() > 380:
        r_scored()
        sleep = 0.1
    screen.update()
    ball.move()
    time.sleep(sleep)
screen.exitonclick()
