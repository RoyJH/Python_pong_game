from turtle import Turtle
R_SCORE = (75, 200)
L_SCORE = (-75, 200)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.speed("fastest")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def score_setup(self):
        self.divider()
        self.goto(L_SCORE)
        self.write(arg=f"{0}", align="center", font=("Courier", 60, "bold"))
        self.goto(R_SCORE)
        self.write(arg=f"{0}", align="center", font=("Courier", 60, "bold"))

    def update_score(self, side):
        self.clear()
        if side == "left":
            self.r_score += 1
        elif side == "right":
            self.l_score += 1
        self.goto(L_SCORE)
        self.write(arg=f"{self.l_score}", align="center", font=("Courier", 60, "bold"))
        self.goto(R_SCORE)
        self.write(arg=f"{self.r_score}", align="center", font=("Courier", 60, "bold"))
        self.divider()

    def divider(self):
        self.pensize(width=3)
        self.goto(0, 300)
        for num in range(0, int(600 / 15)):
            current = self.ycor() - 15
            self.pendown()
            self.sety(current)
            self.penup()
            current = self.ycor() - 15
            self.sety(current)
